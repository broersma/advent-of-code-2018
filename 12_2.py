import little_helper


def answer(input):
    split_input = input.split('\n\n')
    initial = split_input[0]
    initial = [c == '#' for c in initial[15:]]
    lines = split_input[1].split('\n')
    rulesss= (line.split(' => ') for line in lines if line.endswith('#'))
    rules = set(tuple(c == '#' for c in a) for a,_ in rulesss)

    offset = 0
    for i in range(500000):
        # 50000 = 4300349
        # 500000 = 43000349
        # 50000000000 =?= 4300000000349 (wat?)
        initial = [False]*4 + initial + [False]*4
        first = 0
        last = -1
        for i, x in enumerate(zip(initial, initial[1:], initial[2:], initial[3:], initial[4:])):
            if x in rules:
                if not first:
                    first = i
                initial[i] = True
                last = i
            else:
                initial[i] = False
        initial = initial[first:last+1]
        offset += 2 - first

    thesum = 0
    for i,c in enumerate(initial):
        if c:
            pot = i-offset
            thesum += pot

    return thesum


if __name__ == '__main__':
    print(answer(little_helper.get_input(12)))

