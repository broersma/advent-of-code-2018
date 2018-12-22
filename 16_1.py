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

day = 16
if __file__.endswith("_2.py"):
    m = __import__(str(day) + "_1")

registers = [0, 0, 0, 0]

def addr(a, b, c):
    registers[c] = registers[a] + registers[b]
def addi(a, b, c):
    registers[c] = registers[a] + b

def mulr(a, b, c):
    registers[c] = registers[a] * registers[b]
def muli(a, b, c):
    registers[c] = registers[a] * b
    
def banr(a, b, c):
    registers[c] = registers[a] & registers[b]
def bani(a, b, c):
    registers[c] = registers[a] & b
    
def borr(a, b, c):
    registers[c] = registers[a] | registers[b]
def bori(a, b, c):
    registers[c] = registers[a] | b
    
def setr(a, b, c):
    registers[c] = registers[a]
def seti(a, b, c):
    registers[c] = a
    
def gtir(a, b, c):
    registers[c] = 1 if a > registers[b] else 0
def gtri(a, b, c):
    registers[c] = 1 if registers[a] > b else 0
def gtrr(a, b, c):
    registers[c] = 1 if registers[a] > registers[b] else 0

def eqir(a, b, c):
    registers[c] = 1 if a == registers[b] else 0
def eqri(a, b, c):
    registers[c] = 1 if registers[a] == b else 0
def eqrr(a, b, c):
    registers[c] = 1 if registers[a] == registers[b] else 0

ops = [addr, addi, mulr, muli,
       banr, bani, borr, bori,
       setr, seti, gtir, gtri,
       gtrr, eqir, eqri, eqrr]

def answer(input):
    """
    >>> answer("1234")
    1234
    """
    num_samples_behave_like_three_or_more = 0
    for match in re.findall(r"Before: \[\d+, \d+, \d+, \d+\]\n\d+ \d+ \d+ \d+\nAfter:  \[\d+, \d+, \d+, \d+\]", input):
        #print(match)
        m = re.search(r"Before: \[(\d+), (\d+), (\d+), (\d+)\]", match, flags=re.M)
        b0, b1, b2, b3 = (int(x) for x in m.groups())
        m = re.search(r"^(\d+) (\d+) (\d+) (\d+)$", match, re.M)
        o, a, b, c = (int(x) for x in m.groups())
        m = re.search(r"After:  \[(\d+), (\d+), (\d+), (\d+)\]", match, flags=re.M)
        a0, a1, a2, a3 = (int(x) for x in m.groups())
        
        print(b0, b1, b2, b3, "--", o, a, b, c, "->", a0, a1, a2, a3)
        
        num_matching_ops = 0
        for op in ops:
            registers[0] = b0
            registers[1] = b1
            registers[2] = b2
            registers[3] = b3
            
            op(a, b, c)
            
            if registers[0] == a0 and \
               registers[1] == a1 and \
               registers[2] == a2 and \
               registers[3] == a3:
               num_matching_ops += 1
        if num_matching_ops >= 3:
            num_samples_behave_like_three_or_more += 1
    return num_samples_behave_like_three_or_more

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
