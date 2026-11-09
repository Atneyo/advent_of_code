from pathlib import Path
import numpy as np

# find directory where solution.py is
SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_PATH = SCRIPT_DIR / "input.txt"
SAMPLE_PATH = SCRIPT_DIR / "sample.txt"

# Day 4: Printing Department 

def part1(input_path: str) -> int:

    file_array = np.loadtxt(input_path, dtype=str)

    n = len(file_array)
    m = len(file_array[0])

    result = 0
    for i in range(0,n):
        for j in range(0,m):
            if file_array[i][j]=='@':
                neighbors = [(i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1), (i+1,j-1), (i+1,j), (i+1,j+1)]
                paper_nb = 0
                for neighbor_i, neighbor_j in neighbors:
                    if not (neighbor_i<0 or neighbor_i>=n or neighbor_j<0 or neighbor_j>=m):           
                        if file_array[neighbor_i][neighbor_j]=='@':
                            paper_nb+=1
                if paper_nb<4:
                    result+=1

    return result

def part2(input_path: str) -> int:
    with open(input_path,"rt") as infile:
        next_file_array =  np.matrix([list(line.strip()) for line in infile.readlines()])

    file_array = np.matrix([])
    
    n = np.size(next_file_array,0)
    m = np.size(next_file_array,1)
    
    result = 0
    while not np.array_equal(next_file_array,file_array):
        file_array=np.copy(next_file_array)
        for i in range(n):
            for j in range(m):
                if file_array[i][j]=='@':
                    neighbors = [(i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1), (i+1,j-1), (i+1,j), (i+1,j+1)]
                    paper_nb = 0
                    for neighbor_i, neighbor_j in neighbors:
                        if not (neighbor_i<0 or neighbor_i>=n or neighbor_j<0 or neighbor_j>=m):           
                            if file_array[neighbor_i][neighbor_j]=='@':
                                paper_nb+=1
                    if paper_nb<4:
                        result+=1
                        next_file_array[i,j]='.'
    
    return result

if '__main__'==__name__:
    print(f'Part 1 - sample: {part1(SAMPLE_PATH)}')
    print(f'Part 1 - input: {part1(INPUT_PATH)}')
    print(f'Part 2 - sample: {part2(SAMPLE_PATH)}')
    print(f'Part 2 - input: {part2(INPUT_PATH)}')