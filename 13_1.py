import little_helper


def show_grid(grid, carts):
    text = ""
    y = 0
    for line in grid:
        for x, c in enumerate(line):
            for cart in carts:
                if cart[0] == x and cart[1] == y:
                    c = cart[2]
            text += c
        text += "\n"
        y += 1
    return text


def parse_input(input):
    input = input.split('\n')
    y = 0
    carts = []
    grid = []
    for line in input:
        for x, c in enumerate(line):
            if c in ["<",">","v","^"]:
                carts.append([x,y,c,0])
        line = line.replace("<", "-").replace(">", "-").replace("v", "|").replace("^", "|")
        grid.append(line)
        y += 1
    return grid, carts


def tick (grid, carts):
    carts = sorted(carts, key=lambda c: (c[1], c[0]))
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
            if cart[2] != cart2[2] and cart[:2] == cart2[:2]:
                cart[2] = 'X'
                cart2[2] = 'X'
                return carts, cart[:2]
    return carts, None


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
    '-X\n'
    >>> test_tick("v\n^")
    '|\nX\n'
    >>> test_tick("+<")
    'v-\n'
    >>> test_tick(">+")
    '-^\n'
    >>> test_tick("+<\n+\n+", 3)
    '+-\n+\n<\n'
    """
    grid, carts = parse_input(input)
    for i in range(iters):
        carts, _ = tick(grid, carts)
    return show_grid(grid, carts)


def answer(input):
    grid, carts = parse_input(input)

    while True:
        carts, crash = tick(grid, carts)
        if crash:
            return ','.join(str(c) for c in crash)

    return show_grid(grid, carts)


if __name__ == '__main__':
    print(answer(little_helper.get_input(13)))
