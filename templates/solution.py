from pathlib import Path

# find directory where solution.py is
SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_PATH = SCRIPT_DIR / "input.txt"
SAMPLE_PATH = SCRIPT_DIR / "sample.txt"

# Day X: 

def part1(input_path: str) -> int:

    with open(input_path, "r") as file:
        for line in file:
            pass
    
    return

def part2(input_path: str) -> int:

    with open(input_path, "r") as file:
        for line in file:
            pass

    return

if '__main__'==__name__:
    print(f'Part 1 - sample: {part1(SAMPLE_PATH)}')
    print(f'Part 1 - input: {part1(INPUT_PATH)}')
    print(f'Part 2 - sample: {part2(SAMPLE_PATH)}')
    print(f'Part 2 - input: {part2(INPUT_PATH)}')