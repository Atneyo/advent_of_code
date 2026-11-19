from pathlib import Path
from functools import cache

# find directory where solution.py is
SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_PATH = SCRIPT_DIR / "input.txt"
SAMPLE_PATH = SCRIPT_DIR / "sample.txt"

# Day 7: Laboratories

def part1(input_path: str) -> int:

    beams=[]
    split_nb = 0

    with open(input_path, "r") as file:
        for line in file:
            # find the first beam
            if beams==[]:
                for index in range(len(line)):
                    if line[index]=='S':
                        beams.append(index)
                        break

            else:
                new_beams=[]
                for index in beams:
                    if line[index]=='^':
                        split_nb+=1
                        if (new_beams==[]) or (new_beams[-1] != (index-1)):
                            new_beams.append(index-1)
                        new_beams.append(index+1)
                    else:
                        if (new_beams==[]) or (new_beams[-1] != (index)):
                            new_beams.append(index)
                beams=new_beams
    
    return split_nb

class TreeNode:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

def part2(input_path: str) -> int:

    beams=[]

    with open(input_path, "r") as file:
        for line in file:
            # find the first beam
            if beams==[]:
                for index in range(len(line)):
                    if line[index]=='S':
                        root=TreeNode(index)
                        beams.append(root)
                        break

            else:
                new_beams=[]
                for node in beams:
                    if line[node.data]=='^':
                        if (new_beams==[]) or (new_beams[-1].data != (node.data-1)):
                            left = TreeNode(node.data-1)
                            new_beams.append(left)
                            node.left=left
                        else:
                            node.left=new_beams[-1]
                        right=TreeNode(node.data+1)
                        new_beams.append(right)
                        node.right=right
                    else:
                        if (new_beams==[]) or (new_beams[-1].data != (node.data)):
                            left=TreeNode(node.data)
                            new_beams.append(left)
                            node.left=left
                        else:
                            node.left=new_beams[-1]
                beams=new_beams
    print("finished_tree")
    return count_all_paths_from_tree(root)

@cache
def count_all_paths_from_tree(node: TreeNode):
    if  node==None:
        return 0
    if node.left==None and node.right==None:
        return 1
    else:
        return count_all_paths_from_tree(node.left)+count_all_paths_from_tree(node.right)

if '__main__'==__name__:
    print(f'Part 1 - sample: {part1(SAMPLE_PATH)}')
    print(f'Part 1 - input: {part1(INPUT_PATH)}')
    print(f'Part 2 - sample: {part2(SAMPLE_PATH)}')
    print(f'Part 2 - input: {part2(INPUT_PATH)}')