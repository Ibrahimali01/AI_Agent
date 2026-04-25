import pytest
from src.scene_detector import SceneDetector

def test_scene_detector_initialization():
    detector = SceneDetector(threshold=25.0)
    assert detector.threshold == 25.0

def test_scene_detector_config():
    config = {"output": {"save_frames": False}}
    detector = SceneDetector(config=config)
    assert detector.config == config
