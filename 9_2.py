import little_helper
import re

high_score = __import__('9_1').high_score


def answer(input):
    match = re.search(r"(\d+) players; last marble is worth (\d+) points", input)
    num_players = int(match[1])
    last_marble_score = int(match[2])
    return high_score(num_players, last_marble_score*100)


if __name__ == '__main__':
    print(answer(little_helper.get_input(9)))
