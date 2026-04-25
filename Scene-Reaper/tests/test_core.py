import pytest
from scene_reaper.core import SceneDetector

def test_scene_detector_init():
    detector = SceneDetector(threshold=25.0)
    assert detector.threshold == 25.0

# TODO: Add more tests
