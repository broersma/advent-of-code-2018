import little_helper


def answer(input):
    split_input = input.split('\n\n')
    initial = split_input[0]
    initial = initial[15:]
    lines = split_input[1].split('\n')
    rules = dict(line.split(' => ') for line in lines)

    for i in range(20):
        initial = "...." + initial + "...."
        next = ""
        for i in range(len(initial)-4):
            x = initial[i:i+5]
            if x in rules:
                next += rules[x]
            else:
                next += '.'
        initial = next

    thesum = 0
    for i,c in enumerate(initial):
        if c == '#':
            thesum+=i-40

    return thesum


if __name__ == '__main__':
    print(answer(little_helper.get_input(12)))

