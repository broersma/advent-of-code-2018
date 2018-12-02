import little_helper

def answer(input):
    n2 = 0
    n3 = 0
    for id in input.split("\n"):
        num_twos = 0
        num_threes = 0
        for c in id:
            if id.count(c) == 2:
                num_twos += 1
            if id.count(c) == 3:
                num_threes += 1
        if num_twos >= 1:
            n2 += 1
        if num_threes >= 1:
            n3 += 1

    return n2 * n3

if __name__ == '__main__':
    input = little_helper.get_input(2)
    print(answer(input))