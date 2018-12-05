import little_helper

def react(polymer):
    while True:
        start_polymer = polymer
        for a,b in zip(polymer[:-1], polymer[1:]):
            if a != b:
                if a == b.lower() or a.lower() == b:
                    polymer = polymer.replace(a + b, "")
                    break
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
    lines = input.split('\n')

    polymer = lines[0]

    polymer = react(polymer)
    
    return len(polymer)


if __name__ == '__main__':
    day = 5
    input = little_helper.get_input(5)
    print(answer(input))
