from pathlib import Path
from math import sqrt

# find directory where solution.py is
SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_PATH = SCRIPT_DIR / "input.txt"
SAMPLE_PATH = SCRIPT_DIR / "sample.txt"

# Day 8: Playground

def part1(input_path: str) -> int:

    boxes=[]

    with open(input_path, "r") as file:
        for line in file:
            boxes.append([int(i) for i in line.strip().split(",")])

    distances = []
    find_box = {}
    for i in range(len(boxes)):
        for j in range(i+1, len(boxes)):
            d=distance(boxes[i],boxes[j])
            distances.append(d)
            find_box[d]=(boxes[i],boxes[j])

    distances.sort()
    count = 0
    index=0
    circuits={}
    boxes_circuit={}
    last_circuit_added=0
    while(index!=1000):
        box_a,box_b = find_box[distances[index]]
        circuit_a=boxes_circuit.get(tuple(box_a))
        circuit_b=boxes_circuit.get(tuple(box_b))
        if circuit_a!=None and circuit_b!=None and circuit_a==circuit_b:
            index+=1
            continue
        elif circuit_a!=None and circuit_b!=None and circuit_a!=circuit_b:
            for box in circuits[circuit_b]:
                boxes_circuit[box]=circuit_a
                circuits[circuit_a].append(box)
            del circuits[circuit_b]
            count+=1
        elif circuit_a!=None and circuit_b==None:
            circuits[circuit_a].append(tuple(box_b))
            boxes_circuit[tuple(box_b)]=circuit_a
            count+=1
        elif circuit_b!=None and circuit_a==None:
            circuits[circuit_b].append(tuple(box_a))
            boxes_circuit[tuple(box_a)]=circuit_b
            count+=1
        else:
            last_circuit_added+=1
            circuits[last_circuit_added]=[tuple(box_a),tuple(box_b)]
            boxes_circuit[tuple(box_a)]=last_circuit_added
            boxes_circuit[tuple(box_b)]=last_circuit_added
            count+=1
        index+=1

    max1=1
    max2=1
    max3=1
    for value in circuits.values():
        n=len(value)
        if n>max1:
            max3=max2
            max2=max1
            max1=n
        elif n>max2:
            max3=max2
            max2=n
        elif n>max3:
            max3=n
    print(max1,max2,max3)
    return max1*max2*max3

def distance(v1,v2):
    e=(v2[0]-v1[0])**2+(v2[1]-v1[1])**2+(v2[2]-v1[2])**2
    return sqrt(e)

def part2(input_path: str) -> int:

    boxes=[]
    
    with open(input_path, "r") as file:
        for line in file:
            boxes.append([int(i) for i in line.strip().split(",")])

    distances = []
    find_box = {}
    for i in range(len(boxes)):
        for j in range(i+1, len(boxes)):
            d=distance(boxes[i],boxes[j])
            distances.append(d)
            find_box[d]=(boxes[i],boxes[j])

    distances.sort()
    index=0
    circuits={}
    boxes_circuit={}
    last_circuit_added=0
    last_boxes=[]
    stop=False
    while(not stop):
        box_a,box_b = find_box[distances[index]]
        circuit_a=boxes_circuit.get(tuple(box_a))
        circuit_b=boxes_circuit.get(tuple(box_b))
        if circuit_a!=None and circuit_b!=None and circuit_a==circuit_b:
            index+=1
            continue
        elif circuit_a!=None and circuit_b!=None and circuit_a!=circuit_b:
            for box in circuits[circuit_b]:
                boxes_circuit[box]=circuit_a
                circuits[circuit_a].append(box)
            del circuits[circuit_b]
        elif circuit_a!=None and circuit_b==None:
            circuits[circuit_a].append(tuple(box_b))
            boxes_circuit[tuple(box_b)]=circuit_a
        elif circuit_b!=None and circuit_a==None:
            circuits[circuit_b].append(tuple(box_a))
            boxes_circuit[tuple(box_a)]=circuit_b
        else:
            last_circuit_added+=1
            circuits[last_circuit_added]=[tuple(box_a),tuple(box_b)]
            boxes_circuit[tuple(box_a)]=last_circuit_added
            boxes_circuit[tuple(box_b)]=last_circuit_added
        last_boxes=[box_a,box_b]
        index+=1
        if len(circuits.keys())==1 and len(list(circuits.values())[0])==len(boxes):
            stop=True

    return last_boxes[0][0]*last_boxes[1][0]

if '__main__'==__name__:
    # print(f'Part 1 - sample: {part1(SAMPLE_PATH)}')
    print(f'Part 1 - input: {part1(INPUT_PATH)}')
    print(f'Part 2 - sample: {part2(SAMPLE_PATH)}')
    print(f'Part 2 - input: {part2(INPUT_PATH)}')