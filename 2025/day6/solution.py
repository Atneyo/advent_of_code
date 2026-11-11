from pathlib import Path
import operator

# find directory where solution.py is
SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_PATH = SCRIPT_DIR / "input.txt"
SAMPLE_PATH = SCRIPT_DIR / "sample.txt"

# Day 6: Trash Compactor

operators = {'+': operator.add, '*' : operator.mul}
neutral_value = {'+' : 0, '*' : 1}

def part1(input_path: str) -> int:

    result = 0
    problems = []
    with open(input_path, "r") as file:
        for line in file:
            problems.append(line.split())
    for i in range(len(problems[0])):
        sub_result = neutral_value[problems[-1][i]]
        for j in range(len(problems)-1):
            sub_result = operators[problems[-1][i]](sub_result, int(problems[j][i]))
        result+=sub_result
    return result

def part2(input_path: str) -> int:
    result=0

    problems = []
    with open(input_path, "r") as file:
        line_list = list(file)
        for line in line_list[:len(line_list)-1]:
            problems.append(list(line))
        op = line_list[-1].split()
    
    numbers = []
    op_count = len(op)-1
    for i in range(len(problems[0])-1):
        number = ""
        for j in range(len(problems)):
            if not problems[j][len(problems[0])-i-2]==' ':
                number+=problems[j][len(problems[0])-i-2]
        if number=="":
            sub_result = neutral_value[op[op_count]]
            for n in numbers:
                sub_result = operators[op[op_count]](sub_result,n)
            result+=sub_result
            numbers=[]
            op_count-=1
        else:
            numbers.append(int(number))
    sub_result = neutral_value[op[op_count]]
    for n in numbers:
        sub_result = operators[op[op_count]](sub_result,n)
    result+=sub_result
    numbers=[]
    op_count-=1
    return result

if '__main__'==__name__:
    print(f'Part 1 - sample: {part1(SAMPLE_PATH)}')
    print(f'Part 1 - input: {part1(INPUT_PATH)}')
    print(f'Part 2 - sample: {part2(SAMPLE_PATH)}')
    print(f'Part 2 - input: {part2(INPUT_PATH)}')