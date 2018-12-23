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

day = 23
if __file__.endswith("_2.py"):
    m = __import__(str(day) + "_1")

def in_range(a, b):
    distance = abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])
    
    return distance <= a[3]
    
def answer(input):
    """
    >>> answer("1234")
    1234
    """
    lines = input.split('\n')
    bots = []
    for line in lines:
        m = re.search(r"pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)",line)
        x,y,z,r = (int(w) for w in m.groups())
        bots.append((x,y,z,r))
    
    largest_bot = max(bots, key=lambda b: b[3])
    
    print(largest_bot)
    
    count = 0
    for bot in bots:
        if in_range(largest_bot, bot):
            count += 1
    return count


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
