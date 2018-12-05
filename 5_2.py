import little_helper


def answer(input):
    """
    >>> answer("dabAcCaCBAcCcaDA")
    4
    """
    lines = input.split('\n')

    polymer = lines[0]
    types = set(polymer.lower())
    min_len = len(polymer)
    for t in types:
        polymer = lines[0]
        polymer = polymer.replace(t, "")
        polymer = polymer.replace(t.upper(), "")

        while True:
            start_polymer = polymer
            for a,b in zip(polymer[:-1], polymer[1:]):
                if a != b:
                    if a == b.lower() or a.lower() == b:
                        polymer = polymer.replace(a + b, "")
                        break
            if start_polymer == polymer:
                break
        if len(polymer) < min_len:
            min_len = len(polymer)
    return min_len


if __name__ == '__main__':
    input = little_helper.get_input(5)
    print(answer(input))
