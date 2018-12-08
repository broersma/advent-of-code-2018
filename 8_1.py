import little_helper


def get_len(node):
    return 2+len(node[0]) + sum(get_len(n) for n in node[1])


def get_sum(node):
    return sum(node[0]) + sum(get_sum(n) for n in node[1])


def get_node(nums):
    num_children = nums[0]
    num_meta_data = nums[1]
    remaining_nums = nums[2:]

    children = []
    for i in range(num_children):
        node = get_node(remaining_nums)

        children.append(node)
        remaining_nums = remaining_nums[get_len(node):]

    meta_data = remaining_nums[:num_meta_data]
    return (meta_data, children)

def get_tree(input):
    lines = input.split('\n')
    nums = []
    for line in lines:
        for num in line.split():
            nums.append(int(num))

    return get_node(nums)


def answer(input):
    """
    >>> answer("0 3 10 11 12")
    33
    >>> answer("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2")
    138
    """
    tree = get_tree(input)
    return get_sum(tree)


if __name__ == '__main__':
    print(answer(little_helper.get_input(8)))
