import argparse
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(
        description="Run a solution of Advent of Code."
    )

    parser.add_argument("year", type=int, help="Year (ex: 2025)")
    parser.add_argument("day", type=int, help="Day (ex: 1)")

    args = parser.parse_args()

    print(f"AOC - Year: {args.year} - Day: {args.day}")

    solution_path = BASE_DIR / str(args.year) / f"day{args.day}" / "solution.py"
    if not solution_path.exists():
        print(f"No solution for this day: {solution_path} not found.")
        return

    subprocess.run([sys.executable, str(solution_path)])

    
if __name__ == "__main__":
    main()