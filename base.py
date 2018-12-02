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


def answer(input):
    """
    >>> answer(1234)
    1234
    """
    return input


if __name__ == '__main__':
    input = little_helper.get_input(3)
    print(answer(input))
