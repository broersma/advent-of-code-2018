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

day = 9
if __file__.endswith("_2"):
    m = __import__(day + "_1")

def high_score(num_players, last_marble_score):
    circle = deque([0])
    lowest_numbered_remaining_marble = 1
    player_scores = defaultdict(int)
    for i in range(last_marble_score):
        #print(circle, end='')
        if lowest_numbered_remaining_marble % 23 == 0:
            player_scores[i % num_players] += lowest_numbered_remaining_marble
            circle.rotate(7)
            player_scores[i % num_players] += circle.popleft()
            #print('wierd', end='')
        else:
            circle.rotate(-2)
            circle.appendleft(lowest_numbered_remaining_marble)
        #print('->', circle)
        lowest_numbered_remaining_marble += 1

    return max(player_scores.values())



def answer(input):
    """
    >>> answer("9 players; last marble is worth 25 points")
    32
    """
    """
    >>> answer("10 players; last marble is worth 1618 points")
    8317
    """
    lines = input.split('\n')
    for line in lines:
        match = re.search(r"(\d+) players; last marble is worth (\d+) points", line)
        num_players = int(match[1])
        last_marble_score = int(match[2])
        return high_score(num_players, last_marble_score*100)


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
