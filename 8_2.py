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

day = 8
if __file__.endswith("_2"):
    m = __import__(day + "_1")


def get_len(node):
    return 2+len(node[0]) + sum(get_len(n) for n in node[1])

    
def get_sum(node):
    if len(node[1]) == 0:
        return sum(node[0])
    sum_node = 0
    for i in node[0]:
        if i <= len(node[1]):
            sum_node += get_sum(node[1][i-1])
    return sum_node


def get_node(nums):
    num_children = nums[0]
    num_meta_data = nums[1]
    remaining_nums = nums[2:]

    children = []
    for i in range(num_children):
        node = get_node(remaining_nums)

        children.append(node)
        remaining_nums = remaining_nums[get_len(node):]

    meta_data = remaining_nums[:num_meta_data]
    return (meta_data, children)

def answer(input):
    """
    >>> answer("0 3 10 11 12")
    33
    >>> answer("2 2 0 3 10 11 12 0 1 5 0 1")
    38
    >>> answer("2 2 0 3 10 11 12 0 1 5 1 1")
    66
    >>> answer("0 1 99")
    99
    >>> answer("1 1 0 1 99 2")
    0
    >>> answer("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2")
    66
    """
    lines = input.split('\n')
    nums = []
    for line in lines:
        for num in line.split():
            nums.append(int(num))
    
    root = get_node(nums)
    return get_sum(root)


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
