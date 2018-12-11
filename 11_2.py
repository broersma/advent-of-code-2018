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

def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func


def answer(input):
    num = int(input)
    max_power_xyz = None
    max_power = 0
    for z in range(1,301):
        for y in range(1, 300 - z + 1):
            for x in range(1, 300 - z + 1):
                power = power_level_area(x, y, z, num)
                if power > max_power:
                    max_power = power
                    max_power_xyz = (x,y,z)
    return '{},{},{}'.format(*max_power_xyz)

@memoize
def power_level_area(x, y, z, num):
    """
    >>> power_level_area(3, 5, 1, 8)
    4
    >>> power_level_area(122, 79, 1, 57)
    -5
    >>> power_level_area(1, 1, 1, 8)
    -3
    >>> power_level_area(1, 2, 1, 8)
    -2
    >>> power_level_area(2, 1, 1, 8)
    -3
    >>> power_level_area(2, 2, 1, 8)
    -2
    >>> power_level_area(1, 1, 1, 8) \
       + power_level_area(1, 2, 1, 8) \
       + power_level_area(2, 1, 1, 8) \
       + power_level_area(2, 2, 1, 8)
    -10
    >>> power_level_area(1, 1, 2, 8)
    -10
    >>> power_level_area(1, 3, 1, 8)
    -1
    >>> power_level_area(2, 3, 1, 8)
    0
    >>> power_level_area(3, 3, 1, 8)
    1
    >>> power_level_area(3, 2, 1, 8)
    -1
    >>> power_level_area(3, 1, 1, 8)
    -3
    >>> power_level_area(1, 1, 3, 8)
    -14
    """
    if z > 1:
        if z % 2 == 0:
            return power_level_area(x, y, z/2, num) \
                 + power_level_area(x+z/2, y, z/2, num) \
                 + power_level_area(x, y+z/2, z/2, num) \
                 + power_level_area(x+z/2, y+z/2, z/2, num)
        return power_level_area(x, y, z-1, num) \
             + power_level(x+z-1,y+z-1,num) \
             + sum(power_level(x+i, y+z-1, num) for i in range(z-1)) \
             + sum(power_level(x+z-1, y+i, num) for i in range(z-1))
    else:
        return power_level(x, y, num)

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
