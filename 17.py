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

day = 17
if __file__.endswith("_2"):
    m = __import__(day + "_1")

def answer(input):
    """
    >>> answer("1234")
    1234
    """
    lines = input.split('\n')
    clays = set()
    for line in lines:
        xs,ys = line.split(', ')
        c1=xs[0]
        xs=xs[2:]
        ys=ys[2:]
        c = int(xs)
        ys=ys.split('..')
        cmin = int(ys[0])
        cmax = int(ys[1])
        if c1 == 'x':
            for y in range(cmin, cmax+1):
                clays.add((c,y))
        elif c1 == 'y':
            for x in range(cmin, cmax+1):
                clays.add((x,c))
        #print(c1, c,cmin, cmax)

    minx = min(c[0] for c in clays)
    maxx = max(c[0] for c in clays)
    miny = 0
    maxy = max(c[1] for c in clays)

    #print(clays)

    for y in range(0, maxy - miny + 1):
        for x in range(0, maxx - minx + 1):
            if (x+minx,y+miny) == (500,0):
                print('+', end='')
            elif (x+minx,y+miny) in clays:
                print('#', end='')
            else:
                print('.', end='')
        print()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('level', type=int, default=-1, nargs='?')
    args = parser.parse_args()
    level = args.level

    input = little_helper.get_input(day)
    the_answer = answer(input)

    if level == -1:
        #print(the_answer)
        pass
    else:
        print("Submitting", the_answer, "for day", day,"star", level)
        print(little_helper.submit(the_answer, level, day))
