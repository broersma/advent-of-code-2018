import little_helper
show_grid = __import__("13_1").show_grid


def parse_input(input):
    input = input.split('\n')
    y = 0
    carts = []
    grid = []
    id = 0
    for line in input:
        for x, c in enumerate(line):
            if c in ["<",">","v","^"]:
                carts.append([x,y,c,0,id])
                id += 1

        line = line.replace("<", "-").replace(">", "-").replace("v", "|").replace("^", "|")
        grid.append(line)
        y += 1
    return grid, carts


def tick (grid, carts):
    carts = sorted(carts, key=lambda c: (c[1], c[0]))
    destroyed = set()
    for cart in carts:
        if cart[2] == "<":
            cart[0] -= 1
        elif cart[2] == ">":
            cart[0] += 1
        elif cart[2] == "v":
            cart[1] += 1
        elif cart[2] == "^":
            cart[1] -= 1
        cell = grid[cart[1]][cart[0]]
        if cell == '/':
            if cart[2] == "<":
                cart[2] = "v"
            elif cart[2] == ">":
                cart[2] = "^"
            elif cart[2] == "v":
                cart[2] = "<"
            elif cart[2] == "^":
                cart[2] = ">"
        elif cell == '\\':
            if cart[2] == "<":
                cart[2] = "^"
            elif cart[2] == ">":
                cart[2] = "v"
            elif cart[2] == "v":
                cart[2] = ">"
            elif cart[2] == "^":
                cart[2] = "<"
        elif cell == '+':
            if cart[2] == "<":
                if cart[3] % 3 == 0:
                    cart[2] = "v"
                elif cart[3] % 3 == 2:
                    cart[2] = "^"
            elif cart[2] == ">":
                if cart[3] % 3 == 0:
                    cart[2] = "^"
                elif cart[3] % 3 == 2:
                    cart[2] = "v"
            elif cart[2] == "v":
                if cart[3] % 3 == 0:
                    cart[2] = ">"
                elif cart[3] % 3 == 2:
                    cart[2] = "<"
            elif cart[2] == "^":
                if cart[3] % 3 == 0:
                    cart[2] = "<"
                elif cart[3] % 3 == 2:
                    cart[2] = ">"
            cart[3] += 1
        for cart2 in carts:
            if cart[4] != cart2[4] and cart[:2] == cart2[:2]:
                destroyed.add(cart[4])
                destroyed.add(cart2[4])
    carts = [cart for cart in carts if cart[4] not in destroyed]
    return carts


def test_tick(input, iters=1):
    r"""
    >>> test_tick("---<---")
    '--<----\n'
    >>> test_tick("--->---")
    '---->--\n'
    >>> test_tick("|\nv\n|")
    '|\n|\nv\n'
    >>> test_tick("|\n^\n|")
    '^\n|\n|\n'
    >>> test_tick("/<")
    'v-\n'
    >>> test_tick("\<")
    '^-\n'
    >>> test_tick("><")
    '--\n'
    >>> test_tick("v\n^")
    '|\n|\n'
    >>> test_tick("+<")
    'v-\n'
    >>> test_tick(">+")
    '-^\n'
    >>> test_tick("+<\n+\n+", 3)
    '+-\n+\n<\n'
    >>> test_tick("/<")
    'v-\n'
    >>> test_tick("/<")
    'v-\n'
    """
    grid, carts = parse_input(input)
    for i in range(iters):
        carts = tick(grid, carts)
    return show_grid(grid, carts)


def answer(input):
    grid, carts = parse_input(input)

    while len(carts) > 1:
        carts = tick(grid, carts)

    return ','.join(str(c) for c in carts[0][:2])


if __name__ == '__main__':
    print(answer(little_helper.get_input(13)))
