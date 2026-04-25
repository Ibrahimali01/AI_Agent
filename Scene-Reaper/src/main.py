import argparse
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Scene-Reaper: Detect and extract scenes from video files.")
    parser.add_argument("-i", "--input", type=Path, help="Path to input video file")
    parser.add_argument("-o", "--output", type=Path, default=Path("../output"), help="Output directory for extracted scenes")
    parser.add_argument("-t", "--threshold", type=float, default=0.3, help="Scene detection threshold (0-1)")
    parser.add_argument("--version", action="version", version="Scene-Reaper 0.1.0")
    args = parser.parse_args()

    if not args.input:
        parser.print_help()
        sys.exit(1)

    if not args.input.exists():
        print(f"Error: Input file {args.input} does not exist.")
        sys.exit(1)

    print(f"Scene-Reaper: Processing {args.input}")
    print(f"Output directory: {args.output}")
    print(f"Threshold: {args.threshold}")
    # TODO: Implement scene detection logic here
    print("Scene detection logic not yet implemented. Install OpenCV and update main.py to add functionality.")

if __name__ == "__main__":
    main()