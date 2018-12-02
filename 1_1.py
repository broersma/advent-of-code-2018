import little_helper

def answer(input):
    """
    >>> answer("+3\\n+3\\n+4\\n-2\\n-4")
    4
    """
    y = []
    ins = input.split('\n')
    for x in input.split('\n'):
        y.append(int(x))
    return sum(y)

if __name__ == '__main__':
    input = little_helper.get_input(1)
    print(answer(input))