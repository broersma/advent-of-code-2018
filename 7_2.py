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
    create_graph = __import__(str(day) + "_1").create_graph

def answer(input):
    """
    >>> answer("1234")
    1234
    """
    G = create_graph(input)

    done_nodes = set()

    worker_nodes = dict()
    for i in range(5):
        worker_nodes[i] = None

    time = 0
    while len(done_nodes) != len(G.nodes):
        for node in G.nodes:
            if node not in done_nodes and not any(node == value[0] for value in worker_nodes.values() if value):
                if all(ancestor in done_nodes for ancestor in nx.ancestors(G, node)):
                    for i in worker_nodes:
                        if not worker_nodes[i]:
                            worker_nodes[i] = (node, ord(node) - 4) #-64+60
                            break
        for i in worker_nodes:
            if worker_nodes[i]:
                node, time_left = worker_nodes[i]
                if time_left == 1:
                    done_nodes.add(node)
                    worker_nodes[i] = None
                else:
                    worker_nodes[i] = (node, time_left-1)
        time+=1
    return time

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
