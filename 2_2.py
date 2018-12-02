import little_helper

def answer(input):
    ids = sorted(input.split("\n"))
    
    for id1, id2 in zip(ids[:-1], ids[1:]):
        for i in range(len(id1)):
            if id1[:i] + id1[i+1:] == id2[:i] + id2[i+1:]:
                return(id1[:i] + id1[i+1:])


if __name__ == '__main__':
    input = little_helper.get_input(2)
    print(answer(input))