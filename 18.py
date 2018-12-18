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

day = 18
if __file__.endswith("_2"):
    m = __import__(day + "_1")

def get_adjacents(grid, x,y,w,h):
    r'''
    >>> list(get_adjacents("...\n###\n|||\n".split("\n"), 1, 1,3 ,3))
    ['.', '.', '.', '#', '#', '|', '|', '|']
    >>> list(get_adjacents("...\n###\n|||\n".split("\n"), 0, 0,3,3))
    ['.', '#', '#']
    '''
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            nx = x+dx
            ny = y+dy
            if (nx,ny) != (x,y) and 0 <= nx < w and 0 <= ny < h:
                yield grid[ny][nx]

def answer(input):
    grid = input.split('\n')
    h = len(grid)
    grida = []
    gridb = []
    for y,line in enumerate(grid):
        grida.append([])
        gridb.append([])
        for c in line:
            grida[y].append(1 if c == '|' else 2 if c == '#' else 0)
            gridb[y].append(1 if c == '|' else 2 if c == '#' else 0)
        w = len(line)
        #print(line)
    
    grid = grida
    new_grid = gridb
    for i in range(1000000000):
        for y,line in enumerate(grid):
            for x,c in enumerate(line):
                adjs = list(get_adjacents(grid,x,y,w,h))
                if c == 0:
                    if adjs.count(1) >= 3:
                        new_grid[y][x] = 1
                    else:
                        new_grid[y][x] = 0
                elif c == 1:
                    if adjs.count(2) >= 3:
                        new_grid[y][x] = 2
                    else:
                        new_grid[y][x] = 1
                elif c == 2:
                    adjs_list = list(adjs)
                    if 2 in adjs_list and 1 in adjs_list:
                        new_grid[y][x] = 2
                    else:
                        new_grid[y][x] = 0
        grid, new_grid = new_grid, grid
        if i > 10000:
            woods = 0
            yards = 0
            for line in new_grid:
                woods += line.count(1)
                yards += line.count(2)
            print(i, woods * yards)
            """
            for line in new_grid:
                for c in line:
                    if c == 0:
                        print('.', end='')
                    elif c == 1:
                        print('|', end='')
                    elif c == 2:
                        print('#', end='')
                print()
            """
        
    woods = 0
    yards = 0
    for line in grid:
        woods += line.count(1)
        yards += line.count(2)
        for c in line:
            if c == 0:
                print('.', end='')
                
            elif c == 1:
                print('|', end='')
            elif c == 2:
                print('#', end='')

        print()
    return woods * yards

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('level', type=int, default=-1, nargs='?')
    args = parser.parse_args()
    level = args.level

    input = little_helper.get_input(day)
    the_answer = answer(input)

    if level == -1:
        print(the_answer)
    else:
        print("Submitting", the_answer, "for day", day,"star", level)
        print(little_helper.submit(the_answer, level, day))
