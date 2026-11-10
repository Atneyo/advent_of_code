from pathlib import Path

# find directory where solution.py is
SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_PATH = SCRIPT_DIR / "input.txt"
SAMPLE_PATH = SCRIPT_DIR / "sample.txt"

# Day 5: Cafeteria

def part1(input_path: str) -> int:

    intervals = []
    result = 0

    with open(input_path, "r") as file:

        first_part = True
        for line in file:
            if line.isspace():
                first_part = False
                continue
            if first_part:
                a,b = (line.strip()).split('-')
                intervals=insert_interval(int(a),int(b),intervals)
            else:
                id = int(line.strip())
                if binary_search(id, intervals):
                    result+=1

    return result

def insert_interval(interval_a: int, interval_b: int, intervals: list):
    if intervals==[]:
        return [[interval_a,interval_b]]
    new_intervals = []
    for i in range(len(intervals)):
        if intervals[i][1]<interval_a:
            new_intervals.append(intervals[i])
        elif intervals[i][0]>interval_b:
            new_intervals.append([interval_a, interval_b])
            for j in range(i,len(intervals)):
                new_intervals.append(intervals[j])
            return new_intervals
        else:
            interval_a=min(interval_a,intervals[i][0])
            interval_b=max(interval_b,intervals[i][1])

    new_intervals.append([interval_a,interval_b])
    return new_intervals

def binary_search(id, intervals):
    n=len(intervals)
    if n==0:
        return False
    else:
        if intervals[n//2][0]<=id<=intervals[n//2][1]:
            return True
        else:
            if id<intervals[n//2][0]:
                return binary_search(id,intervals[:n//2])
            else:
                return binary_search(id,intervals[n//2+1:])

def part2(input_path: str) -> int:

    intervals = []
    result = 0
    
    with open(input_path, "r") as file:
    
        for line in file:
            if line.isspace():
                for interval in intervals:
                    result+=interval[1]-interval[0]+1
                return result
            a,b = (line.strip()).split('-')
            intervals=insert_interval(int(a),int(b),intervals)
    
    return result

if '__main__'==__name__:
    print(f'Part 1 - sample: {part1(SAMPLE_PATH)}')
    print(f'Part 1 - input: {part1(INPUT_PATH)}')
    print(f'Part 2 - sample: {part2(SAMPLE_PATH)}')
    print(f'Part 2 - input: {part2(INPUT_PATH)}')