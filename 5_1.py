import little_helper

def react(polymer):
    types = set(polymer.lower())
    while True:
        start_polymer = polymer
        for type in types:
            polymer = polymer.replace(type.upper() + type, "")
            polymer = polymer.replace(type + type.upper(), "")
        if start_polymer == polymer:
            return polymer


def answer(input):
    """
    >>> answer("aA")
    0
    >>> answer("abBA")
    0
    >>> answer("abAB")
    4
    >>> answer("aabAAB")
    6
    >>> answer("dabAcCaCBAcCcaDA")
    10
    """
    polymer = input

    polymer = react(polymer)
    
    return len(polymer)


if __name__ == '__main__':
    day = 5
    input = little_helper.get_input(5)
    print(answer(input))
