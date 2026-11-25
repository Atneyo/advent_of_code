from pathlib import Path

# find directory where solution.py is
SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_PATH = SCRIPT_DIR / "input.txt"
SAMPLE_PATH = SCRIPT_DIR / "sample.txt"

# Day 9: Movie Theater 

def part1(input_path: str) -> int:

    tiles = []

    with open(input_path, "r") as file:
        for line in file:
            tiles.append([int(i) for i in line.strip().split(',')])

    bottom_right_corner = tiles[0]
    top_right_corner = tiles[0]
    bottom_left_corner = tiles[0]
    top_left_corner = tiles[0]

    for tile in tiles:
        if tile[0]+tile[1]<=top_left_corner[0]+top_left_corner[1]:
            top_left_corner=tile
        if tile[0]+tile[1]>=bottom_right_corner[0]+bottom_right_corner[1]:
            bottom_right_corner=tile
        if tile[0]-tile[1]>=top_right_corner[0]-top_right_corner[1]:
            top_right_corner=tile
        if tile[1]-tile[0]>=bottom_left_corner[1]-bottom_left_corner[0]:
            bottom_left_corner=tile
    
    return max(area(top_left_corner,bottom_right_corner), area(bottom_left_corner,top_right_corner))

def area(tile1: list, tile2: list) -> int:
    h = abs(tile1[1]-tile2[1])+1
    w = abs(tile1[0]-tile2[0])+1
    return h * w

def part2(input_path: str) -> int:

    tiles = []
    
    with open(input_path, "r") as file:
        for line in file:
            tiles.append([int(i) for i in line.strip().split(',')])

    max_area=0

    for i in range(len(tiles)):
        for j in range(i, len(tiles)):
            current_area=area(tiles[i],tiles[j])
            if current_area>max_area:
                if in_polygone([tiles[i],tiles[j]], tiles):
                    max_area=current_area

    return max_area

def in_polygone(opposite_corners: list, polygon: list) -> bool:
    xr = max(opposite_corners[0][0], opposite_corners[1][0])
    xl = min(opposite_corners[0][0], opposite_corners[1][0])
    y_bottom = max(opposite_corners[0][1], opposite_corners[1][1])
    y_top = min(opposite_corners[0][1], opposite_corners[1][1])

    edges_crossed_BR = 0
    edges_crossed_TR = 0
    edges_crossed_BL = 0
    edges_crossed_TL = 0
    
    for i in range(len(polygon)):
        
        p1 = polygon[i]
        p2 = polygon[(i+1) % len(polygon)]

        # vertical edge
        if p1[0]==p2[0]:

            # count how many polygon edges the ray crosses
            if p1[0]>xr:
                if y_bottom<max(p1[1],p2[1]) and y_bottom>min(p1[1],p2[1]):
                    edges_crossed_BR+=1
                if y_top<max(p1[1],p2[1]) and y_top>min(p1[1],p2[1]):
                    edges_crossed_TR+=1
            if p1[0]>xl:
                if y_bottom<max(p1[1],p2[1]) and y_bottom>min(p1[1],p2[1]):
                    edges_crossed_BL+=1
                if y_top<max(p1[1],p2[1]) and y_top>min(p1[1],p2[1]):
                    edges_crossed_TL+=1

            # check if the polygon edge crosses the rectangle
            if xl<p1[0] and xr>p1[0]:
                if max(p1[1],p2[1])>y_top and min(p1[1],p2[1])<y_bottom:
                    return False
            
        # horizontal edge
        else:
            # check if the polygon edge crosses the rectangle
            if y_bottom>p1[1] and y_top<p1[1]:
                if max(p1[0],p2[0])>xl and min(p1[0],p2[0])<xr:
                    return False

    # check if corners are in the polygon
    if edges_crossed_TL%2==0 or edges_crossed_TR%2==0 or edges_crossed_BL%2==0 or edges_crossed_BR%2==0:
        return False

    return True

if '__main__'==__name__:
    print(f'Part 1 - sample: {part1(SAMPLE_PATH)}')
    print(f'Part 1 - input: {part1(INPUT_PATH)}')
    print(f'Part 2 - sample: {part2(SAMPLE_PATH)}')
    print(f'Part 2 - input: {part2(INPUT_PATH)}')