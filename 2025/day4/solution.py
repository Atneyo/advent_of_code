from pathlib import Path
import numpy as np

# find directory where solution.py is
SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_PATH = SCRIPT_DIR / "input.txt"
SAMPLE_PATH = SCRIPT_DIR / "sample.txt"

# Day 4: Printing Department 

def part1(input_path: str) -> int:

    input = np.loadtxt(input_path, dtype=str)

    n = len(input)
    m = len(input[0])

    result = 0
    for i in range(0,n):
        for j in range(0,m):
            if input[i][j]=='@':
                neighbors = [(i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1), (i+1,j-1), (i+1,j), (i+1,j+1)]
                paper_nb = 0
                for neighbor_i, neighbor_j in neighbors:
                    if not (neighbor_i<0 or neighbor_i>=n or neighbor_j<0 or neighbor_j>=m):           
                        if input[neighbor_i][neighbor_j]=='@':
                            paper_nb+=1
                if paper_nb<4:
                    result+=1

    return result

def part2(input_path: str) -> int:

    file = open(input_path, "r")

    for line in file:
        pass

    file.close()

    return

if '__main__'==__name__:
    print(f'Part 1 - sample: {part1(SAMPLE_PATH)}')
    print(f'Part 1 - input: {part1(INPUT_PATH)}')
    # print(f'Part 2 - sample: {part2(SAMPLE_PATH)}')
    # print(f'Part 2 - input: {part2(INPUT_PATH)}')