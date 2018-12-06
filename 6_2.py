import little_helper

# defaultdict(list), defaultdict(int), deque.rotate/append
from collections import defaultdict, deque
# functools.reduce(function, iterable[, initializer])
from functools import reduce
# islice(seq, [start,] stop [, step])
from itertools import islice
import re
#import networkx as nx
#from numba import jit
from sys import exit

def distance(coord, x,y ):
    return abs(coord[0] - x) + abs(coord[1] - y)

def is_finite(coord, coords):
    return coord[0] > min(c[0] for c in coords) and coord[1] > min(c[1] for c in coords) and coord[0] < max(c[0] for c in coords) and coord[1] < max(c[1] for c in coords)
def is_nearer_to(coorda, coordb, x, y):
    return distance(coorda, x, y) < distance(coordb, x,y)

def get_all_sets(coords):
    req_dist = 32
    for c in coords:
        xxx = set()
        for x in range(c[0]-req_dist, c[0]+req_dist):
            for y in range(c[1]-req_dist, c[1]+req_dist):
                xxx.add((x,y))
        print(xxx)
        yield xxx

def answer(input):
    """
    >>> answer("1234")
    1234
    """
    lines = input.split('\n')

    coords = []
    for line in lines:
        x,y = line.split(', ')
        x = int(x)
        y = int(y)
        coords.append((x,y))
    

    minx = min(c[0] for c in coords)
    miny = min(c[1] for c in coords)
    maxx = max(c[0] for c in coords)
    maxy = max(c[1] for c in coords)

    areas = dict()

    spanning_coords = [c for c in coords if c[0] == minx or c[0] == maxx or c[1] == miny or c[1] == maxy]
    print(spanning_coords)
    
    center = ((minx+maxx)/2, (miny+maxy)/2)
    #return
    #for x in get_all_sets(coords):
    #    print(x)

    sorted_coords = sorted(coords, key=lambda c: distance(c, center[0], center[1]), reverse=True)
    #print(sorted_coords)
    #safe_coords = reduce(lambda s,t: s.intersection(t), get_all_sets(coords))
    #print(safe_coords)
    #return len(safe_coords)
    
    
    req_dist = 10000
    #req_dist = 32


    desired_region = set()
    for x in range(minx, maxx):
        for y in range(miny, maxy):
            sum_dist = 0
            for coord in sorted_coords:
                sum_dist += distance(coord, x, y)
                if sum_dist >= req_dist:
                    break
            if sum_dist < req_dist:
                desired_region.add((x,y))
    if False:
        for y in range(miny, maxy):
            for x in range(minx, maxx):
                if (x,y) in desired_region:
                    print('#', end='')
                else:
                    print('.', end='')
            print()
    return len(desired_region)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('level', type=int, default=-1, nargs='?')
    args = parser.parse_args()
    level = args.level

    day = 6

    input = little_helper.get_input(day)
    the_answer = answer(input)

    if level == -1:
        print(the_answer)
    else:
        print("Submitting", the_answer, "for day", day,"star", level)
        print(little_helper.submit(the_answer, level, day))
