#!/usr/bin/env python3
"""
Scene-Reaper: A tool for scene detection and extraction.
"""
import argparse
from .core import SceneDetector

def main():
    parser = argparse.ArgumentParser(description="Scene-Reaper: Detect and extract scenes from media.")
    parser.add_argument("--input", "-i", help="Input media file path", required=True)
    parser.add_argument("--output", "-o", help="Output directory for extracted scenes", default="scenes")
    parser.add_argument("--threshold", "-t", type=float, help="Scene detection threshold", default=30.0)
    args = parser.parse_args()
    
    detector = SceneDetector(threshold=args.threshold)
    detector.process(args.input, args.output)

if __name__ == "__main__":
    main()
