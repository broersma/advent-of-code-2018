import little_helper

react = __import__("5_1").react


def answer(input):
    """
    >>> answer("dabAcCaCBAcCcaDA")
    4
    """
    types = set(input.lower())
    min_len = len(input)
    for t in types:
        polymer = input

        polymer = polymer.replace(t, "")
        polymer = polymer.replace(t.upper(), "")

        polymer = react(polymer)

        if len(polymer) < min_len:
            min_len = len(polymer)
    return min_len


if __name__ == '__main__':
    input = little_helper.get_input(5)
    print(answer(input))
