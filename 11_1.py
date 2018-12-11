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

day = 11
if __file__.endswith("_2"):
    m = __import__(day + "_1")

def answer(input):
    """
    >>> answer(18)
    '33,45'
    """
    max_power_xy = None
    max_power = 0
    num = int(input)
    for y in range(1,301-2):
        for x in range(1,301-2):
            power = sum(power_level(x+i, y+j, num) for i in range(3) for j in range(3))
            if power > max_power:
                max_power = power
                max_power_xy = (x,y)
            
    return '{},{}'.format(*max_power_xy)

def power_level(x, y, num):
    """
    >>> power_level(3, 5, 8)
    4
    >>> power_level(122, 79, 57)
    -5
    >>> power_level(217, 196, 39)
    0
    >>> power_level(101, 153, 71)
    4
    """
    rack_id = x + 10
    power_level = rack_id * y
    power_level += num
    power_level *= rack_id
    if power_level > 100:
        power_level = (power_level - (power_level % 100))
    else:
        power_level = 0
    if power_level > 1000:
        power_level = power_level - ((power_level // 1000) * 1000)
    power_level = power_level  // 100
    power_level -= 5
    return power_level


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
