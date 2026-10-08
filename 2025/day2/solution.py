from pathlib import Path

# find directory where solution.py is
SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_PATH = SCRIPT_DIR / "input.txt"
SAMPLE_PATH = SCRIPT_DIR / "sample.txt"

# Day 2: Gift Shop

def part1(input_path: str) -> int:

    file = open(input_path, 'r')

    result = 0

    for line in file:
        ID_ranges = line.split(',')
        for ID_range in ID_ranges:
            begin,end = ID_range.split('-')
            begin = int(begin)
            end = int(end)
            for i in range(begin, end+1):
                if not is_valid(i):
                    result+=i

    file.close()

    return result

def is_valid(id_num: int) -> bool:
    id_string = str(id_num)
    n = len(id_string)
    if n%2 != 0 :
        return True
    elif id_string[0:n//2] == id_string[n//2:]:
        return False
    else:
        return True

def part2(input_path: str) -> int:
    file = open(input_path, 'r')
    
    result = 0

    for line in file:
        ID_ranges = line.split(',')
        for ID_range in ID_ranges:
            begin,end = ID_range.split('-')
            begin = int(begin)
            end = int(end)
            for i in range(begin, end+1):
                if not is_valid_part2_alternative(i):
                    result+=i

    file.close()

    return result

def is_valid_part2(id_num: int)-> bool:
    id_string = str(id_num)
    n = len(id_string)

    for i in range(n//2, 0, -1):
        if n%i==0:
            is_valid_for_i = False
            last_part = id_string[:i]
            for j in range (i, n-i+1, i):
                part = id_string[j:j+i]
                if part!=last_part:
                    is_valid_for_i = True
                    break
                else:
                    last_part=part
            if not is_valid_for_i:
                return False
    return True

def is_valid_part2_alternative(id_num: int) -> bool:
    id_string = str(id_num)
    n = len(id_string)

    for i in range(n//2, 0, -1):
        if n%i==0:
            if (id_string[:i]*(n//i)==id_string):
                return False
    return True

    

if '__main__'==__name__:
    print(f'Part 1 - sample: {part1(SAMPLE_PATH)}')
    print(f'Part 1 - input: {part1(INPUT_PATH)}')
    print(f'Part 2 - sample: {part2(SAMPLE_PATH)}')
    print(f'Part 2 - input: {part2(INPUT_PATH)}')