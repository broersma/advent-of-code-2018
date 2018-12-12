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

day = 12
if __file__.endswith("_2"):
    m = __import__(day + "_1")

def answer(input):
    """
    >>> answer("1234")
    1234
    """
    split_input = input.split('\n\n')
    initial = split_input[0]
    initial = initial[15:]
    lines = split_input[1].split('\n')
    rules = dict(line.split(' => ') for line in lines)
    print(rules)

    for i in range(20):
        initial = "...." + initial + "...."
        next = ""
        for i in range(len(initial)-4):
            x = initial[i:i+5]
            if x in rules:
                next += rules[x]
            else:
                next += '.'
        initial = next
        print(initial)

    thesum = 0
    for i,c in enumerate(initial):
        print(i-40, c)
        if c == '#':
            thesum+=i-40

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
