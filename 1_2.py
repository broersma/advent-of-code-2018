import little_helper

def answer(input):
    """
    >>> answer("+3\\n+3\\n+4\\n-2\\n-4")
    10
    >>> answer("+7\\n+7\\n-2\\n-7\\n-4")
    14
    """
    y = []
    z = 0
    zs = []
    ins = input.split('\n')
    while True:
        for x in ins:
            #y.append(int(x))
            z += int(x)
            if z in zs:
                return z
            zs.append(z)
    return zs


if __name__ == '__main__':
    input = little_helper.get_input(1)
    print(answer(input))