from pathlib import Path

# find directory where solution.py is
SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_PATH = SCRIPT_DIR / "input.txt"
SAMPLE_PATH = SCRIPT_DIR / "sample.txt"

# Day 3: Lobby

def part1(input_path: str) -> int:

    file = open(input_path, 'r')

    result = 0
    for line in file:
        line = line.strip()
        first_battery = -1
        second_battery = -1
        for index, battery in enumerate(line):
            battery = int(battery)
            if index == len(line)-1:
                if battery>second_battery:
                    second_battery = battery
            else:
                if battery>first_battery:
                    first_battery=battery
                    second_battery=int(line[index+1])
                elif battery>second_battery:
                    second_battery=battery
        result+=int(str(first_battery)+str(second_battery))

    file.close()
    return result

def part2(input_path: str) -> int:
    nb =12 # number of batteries to find per line
    file = open(input_path, 'r')

    result = 0
    for line in file:
        line = line.strip()
        batteries = [-1]*nb
        for index, battery in enumerate(line):
            battery = int(battery)

            start = 0
            if (len(line)-index<nb):
                start = nb - (len(line)-index)
            for i in range(start, nb):
                if battery>batteries[i]:
                    batteries[i]= battery
                    for j in range (i+1,nb):
                        batteries[j]=-1
                    break
        result+=int("".join([str(i) for i in batteries]))

    file.close()
    return result

if '__main__'==__name__:
    print(f'Part 1 - sample: {part1(SAMPLE_PATH)}')
    print(f'Part 1 - input: {part1(INPUT_PATH)}')
    print(f'Part 2 - sample: {part2(SAMPLE_PATH)}')
    print(f'Part 2 - input: {part2(INPUT_PATH)}')