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

def num_digits(n):
    return len(str(n))#int(math.log10(n))+1

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
        
        for i in range(num_digits(new_recipe))[::-1]:
            recipes.append(get_digit(new_recipe, i))

        if len(recipes) >= input + 10:
            break
        one += (1+one_recipe)
        one %= len(recipes) 
        one_recipe = recipes[one]

        two += (1+two_recipe)
        two %= len(recipes)
        two_recipe = recipes[two]


        #print(one, one_recipe, two, two_recipe)
    #print(recipes)
    return ''.join(str(n) for n in recipes[-10:])


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
