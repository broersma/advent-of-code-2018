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
#from bitarray import bitarray

day = 12
if __file__.endswith("_2"):
    m = __import__(day + "_1")

#@jit
def answer(input):
    """
    >>> answer("1234")
    1234
    """
    split_input = input.split('\n\n')
    initial = split_input[0]
    initial = [c == '#' for c in initial[15:]]
    lines = split_input[1].split('\n')
    rulesss= (line.split(' => ') for line in lines if line.endswith('#'))
    rules = set(tuple(c == '#' for c in a) for a,_ in rulesss)

    offset = 0
    #for i in range(50000000000):
    for i in range(500000):
        # 50000 = 4300349
        # 500000 = 43000349
        # 50000000000 =?= 4300000000349 (wat?)
        initial = [False]*4 + initial + [False]*4
        #used_rules = set()
        first = 0
        last = -1
        for i, x in enumerate(zip(initial, initial[1:], initial[2:], initial[3:], initial[4:])):
            if x in rules:
                #used_rules.add(x)
                if not first:
                    first = i
                initial[i] = True
                last = i
            else:
                initial[i] = False
        #print(len(used_rules))
        initial = initial[first:last+1]
        offset += 2 - first

    thesum = 0
    for i,c in enumerate(initial):
        if c:
            pot = i-offset
            thesum += pot

    return thesum


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
