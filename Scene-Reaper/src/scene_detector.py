import cv2
import os
from pathlib import Path

class SceneDetector:
    def __init__(self, threshold=30.0, config=None):
        self.threshold = threshold
        self.config = config or {}

    def detect_scenes(self, video_path, output_dir):
        print(f"Detecting scenes in {video_path}...")
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)

        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print("Error: Could not open video file.")
            return

        prev_frame = None
        scene_count = 0
        frame_count = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            if prev_frame is not None:
                diff = cv2.absdiff(prev_frame, gray)
                mean_diff = diff.mean()
                if mean_diff > self.threshold:
                    scene_count += 1
                    print(f"Scene {scene_count} detected at frame {frame_count} (diff: {mean_diff:.2f})")
                    if self.config.get("output", {}).get("save_frames", True):
                        frame_path = output_path / f"scene_{scene_count:04d}.jpg"
                        cv2.imwrite(str(frame_path), frame)

            prev_frame = gray
            frame_count += 1

        cap.release()
        print(f"Total scenes detected: {scene_count}")
