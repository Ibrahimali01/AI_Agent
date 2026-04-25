#!/usr/bin/env python3
import argparse
from src.scene_detector import SceneDetector
from src.utils import load_config

def main():
    parser = argparse.ArgumentParser(description="Scene-Reaper: Video Scene Detection Tool")
    parser.add_argument("input", help="Path to input video file")
    parser.add_argument("-o", "--output", help="Output directory for scenes", default="scenes")
    parser.add_argument("-t", "--threshold", type=float, help="Scene detection threshold", default=30.0)
    args = parser.parse_args()

    config = load_config()
    detector = SceneDetector(threshold=args.threshold, config=config)
    detector.detect_scenes(args.input, args.output)

if __name__ == "__main__":
    main()
