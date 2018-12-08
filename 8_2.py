import little_helper

get_tree = __import__('8_1').get_tree


def get_sum(node):
    if len(node[1]) == 0:
        return sum(node[0])
    sum_node = 0
    for i in node[0]:
        if i <= len(node[1]):
            sum_node += get_sum(node[1][i-1])
    return sum_node


def answer(input):
    """
    >>> answer("0 3 10 11 12")
    33
    >>> answer("2 2 0 3 10 11 12 0 1 5 0 1")
    38
    >>> answer("2 2 0 3 10 11 12 0 1 5 1 1")
    66
    >>> answer("0 1 99")
    99
    >>> answer("1 1 0 1 99 2")
    0
    >>> answer("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2")
    66
    """
    tree = get_tree(input)
    return get_sum(tree)


if __name__ == '__main__':
    print(answer(little_helper.get_input(8)))
