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
    for line in grid:
        w = len(line)
        print(line)
    
    for i in range(10):
        new_grid = []
        for y,line in enumerate(grid):
            new_grid.append([])
            for x,c in enumerate(line):
                adjs = list(get_adjacents(grid,x,y,w,h))
                if c == '.':
                    if adjs.count('|') >= 3:
                        new_grid[y].append('|')
                    else:
                        new_grid[y].append('.')
                elif c == '|':
                    if adjs.count('#') >= 3:
                        new_grid[y].append('#')
                    else:
                        new_grid[y].append('|')
                elif c == '#':
                    adjs_list = list(adjs)
                    if '#' in adjs_list and '|' in adjs_list:
                        new_grid[y].append('#')
                    else:
                        new_grid[y].append('.')
        grid = new_grid
        
    woods = 0
    yards = 0
    for line in new_grid:
        woods += line.count('|')
        yards += line.count('#')
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
