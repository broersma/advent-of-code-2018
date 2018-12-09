import little_helper
import re
from collections import defaultdict, deque


def high_score(num_players, last_marble_score):
    circle = deque([0])
    lowest_numbered_remaining_marble = 1
    player_scores = defaultdict(int)
    for i in range(last_marble_score):
        if lowest_numbered_remaining_marble % 23 == 0:
            player_scores[i % num_players] += lowest_numbered_remaining_marble
            circle.rotate(7)
            player_scores[i % num_players] += circle.popleft()
        else:
            circle.rotate(-2)
            circle.appendleft(lowest_numbered_remaining_marble)
        lowest_numbered_remaining_marble += 1

    return max(player_scores.values())


def answer(input):
    """
    >>> answer("9 players; last marble is worth 25 points")
    32
    >>> answer("10 players; last marble is worth 1618 points")
    8317
    """
    match = re.search(r"(\d+) players; last marble is worth (\d+) points", input)
    num_players = int(match[1])
    last_marble_score = int(match[2])
    return high_score(num_players, last_marble_score)


if __name__ == '__main__':
    print(answer(little_helper.get_input(9)))
