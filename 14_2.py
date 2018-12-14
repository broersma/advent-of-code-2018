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

day = 14
if __file__.endswith("_2"):
    m = __import__(day + "_1")
import math

def get_digit(number, n):
    return number // 10**n % 10

def answer(input):
    """
    >>> answer("1234")
    1234
    """
    input = int(input)
    recipes = [3,7]
    one = 0
    two = 1
    one_recipe = recipes[one]
    two_recipe = recipes[two]
    while True:
        new_recipe = one_recipe + two_recipe

        d = new_recipe // 10 % 10
        if d > 0:
            recipes.append(d)
            
        d = new_recipe % 10
        recipes.append(d)

        num_recipes = len(recipes)
        one = (one +1+one_recipe)%num_recipes
        one_recipe = recipes[one]

        two = (two+1+two_recipe)%num_recipes
        two_recipe = recipes[two]

        if recipes[-2] == 1 and recipes[-3] == 2 and recipes[-4] == 0 and recipes[-5] == 6 and recipes[-6] == 3 and recipes[-7] == 2:
            return len(recipes) - 7
        if recipes[-1] == 1 and recipes[-2] == 2 and recipes[-3] == 0 and recipes[-4] == 6 and recipes[-5] == 3 and recipes[-6] == 2:
            return len(recipes) - 6

        #print(one, one_recipe, two, two_recipe)
    return -1


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
