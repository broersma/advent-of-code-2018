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

import networkx as nx

day = 7
if __file__.endswith("_2.py"):
    m = __import__(str(day) + "_1")

def answer(input):
    """
    >>> answer("1234")
    1234
    """
    G = create_graph(input)
        #return int(line)
    strrr = ""
    for x in nx.lexicographical_topological_sort(G):
        strrr += x
    return strrr

def create_graph(input):
    lines = input.split('\n')
    G=nx.DiGraph()
    for line in lines:
        #tep B must be finished before step X can begin.
        a,b = line[5], line[36]
        G.add_edge(a,b)
        #return int(line)
    return G


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
