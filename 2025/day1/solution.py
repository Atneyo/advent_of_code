from pathlib import Path

# find directory where solution.py is
SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_PATH = SCRIPT_DIR / "input.txt"
SAMPLE_PATH = SCRIPT_DIR / "sample.txt"

# Day 1: Secret Entrance

def part1(input_path: str) -> int:
    file = open(input_path, "r")

    dial_position = 50
    result = 0

    for line in file:
        direction = line[0]
        rotation = line[1:].strip()
        if direction == "R":
            dial_position = (dial_position + int(rotation)) % 100
        else:
            dial_position = abs((dial_position - int(rotation)) % 100)
        if dial_position == 0:
            result += 1

    file.close()

    return result

def part2(input_path: str) -> int:
    file = open(input_path, "r")
    
    dial_position = 50
    result = 0
    
    for line in file:
        direction = line[0]
        rotation = line[1:].strip()
        if direction == "R":
            result += (dial_position + int(rotation)) // 100
            dial_position = (dial_position + int(rotation)) % 100
            
        else:
            r = int(rotation)
            if dial_position-r<=0:
                # 0 passed at least once
                result+= 1+ (r-dial_position)//100
            if dial_position==0:
                result-=1
            dial_position = (dial_position - int(rotation)) % 100

    file.close()

    return result

if '__main__'==__name__:
    print(f'Part 1 - sample: {part1(SAMPLE_PATH)}')
    print(f'Part 1 - input: {part1(INPUT_PATH)}')
    print(f'Part 2 - sample: {part2(SAMPLE_PATH)}')
    print(f'Part 2 - input: {part2(INPUT_PATH)}')