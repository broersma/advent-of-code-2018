import little_helper
import networkx as nx


class Unit:
    def __init__(self, position, faction, ap=3, hp=200):
        self.position = position
        self.faction = faction
        self.ap = ap
        self.hp = hp

    def is_alive(self):
        return self.hp > 0

    def __repr__(self):
        return "Unit({})".format(', '.join([repr(x) for x in [self.position, self.faction, self.ap, self.hp]]))

    def __str__(self):
        return "{0}({1})".format(self.faction, self.hp)


def parse_input(input):
    r"""
    >>> x = '''
    ... ######
    ... #E..G#
    ... ######
    ... '''.strip()
    >>> grid, units = parse_input(x)
    >>> print('\n'.join(grid))
    ######
    #....#
    ######
    >>> units
    [Unit((1, 1), 'E', 3, 200), Unit((4, 1), 'G', 3, 200)]
    """
    input = input.split('\n')
    y = 0
    units = []
    grid = []
    for line in input:
        end = line.find(" ")
        if end > 0:
            line = line[:end]
        for x, c in enumerate(line):
            if c in ['E','G']:
                units.append(Unit((x,y),c,3,200))
            elif c == 'g':
                units.append(Unit((x,y),'G',3,200))

        line = line.replace("G", ".").replace("E", ".").replace("g", ".")
        grid.append(line)
        y += 1
        if line == '':
            break
    return grid, units


def show_grid(grid, units):
    text = ""
    y = 0
    for line in grid:
        for x, c in enumerate(line):
            for unit in units:
                if unit.position == (x,y):
                    c = unit.faction
            text += c
        for unit in sorted((unit for unit in units if unit.position[1] == y), key=lambda u: u.position[0]):
            text += " " + str(unit)
        text += "\n"
        y += 1
    return text


def create_graph(grid):
    """
    >>> G = create_graph(['######', '#....#', '######'])
    >>> G.nodes
    NodeView(((1, 1), (2, 1), (3, 1), (4, 1)))
    >>> G.edges
    EdgeView([((1, 1), (2, 1)), ((2, 1), (3, 1)), ((3, 1), (4, 1))])
    >>> G = create_graph(['##.#', '#..#', '#..#'])
    >>> G.nodes
    NodeView(((2, 0), (1, 1), (2, 1), (1, 2), (2, 2)))
    >>> G.edges
    EdgeView([((2, 0), (2, 1)), ((1, 1), (2, 1)), ((1, 1), (1, 2)), ((2, 1), (2, 2)), ((1, 2), (2, 2))])
    >>> G.add_edge((2,0),(2,2))
    >>> G.edges
    EdgeView([((2, 0), (2, 1)), ((2, 0), (2, 2)), ((1, 1), (2, 1)), ((1, 1), (1, 2)), ((2, 1), (2, 2)), ((1, 2), (2, 2))])
    >>> G.add_edge((2,2),(2,0))
    >>> G.edges
    EdgeView([((2, 0), (2, 1)), ((2, 0), (2, 2)), ((1, 1), (2, 1)), ((1, 1), (1, 2)), ((2, 1), (2, 2)), ((1, 2), (2, 2))])
    >>> G.add_edge((2,2),(1,2))
    >>> G.edges
    EdgeView([((2, 0), (2, 1)), ((2, 0), (2, 2)), ((1, 1), (2, 1)), ((1, 1), (1, 2)), ((2, 1), (2, 2)), ((1, 2), (2, 2))])
    >>> G.add_edge((2,1),(1,0))
    >>> G.edges
    EdgeView([((2, 0), (2, 1)), ((2, 0), (2, 2)), ((1, 1), (2, 1)), ((1, 1), (1, 2)), ((2, 1), (2, 2)), ((2, 1), (1, 0)), ((1, 2), (2, 2))])
    >>> G.add_edge((1,0),(2,1))
    >>> G.edges
    EdgeView([((2, 0), (2, 1)), ((2, 0), (2, 2)), ((1, 1), (2, 1)), ((1, 1), (1, 2)), ((2, 1), (2, 2)), ((2, 1), (1, 0)), ((1, 2), (2, 2))])
    """
    G = nx.Graph()
    for y,line in enumerate(grid):
        for x,c in enumerate(line):
            if c in ['.', 'G', 'E']:
                G.add_node((x,y))
    for node in G.nodes():
        for dx,dy in [(-1,0), (1,0),(0,1),(0,-1)]:
            adj_node = (node[0]+dx, node[1]+dy)
            if G.has_node(adj_node):
                G.add_edge(node,adj_node)
    return G


def add(a, b):
    return (a[0]+b[0], a[1]+b[1])


def get_adjacent_squares(position, G):
    r"""
    >>> x = '''
    ... ######
    ... #E..G#
    ... #....#
    ... #....#
    ... ######
    ... '''.strip()
    >>> grid, units = parse_input(x)
    >>> G = create_graph(grid)
    >>> list(get_adjacent_squares((1,1), G))
    [(2, 1), (1, 2)]
    """
    for direction in [(-1,0), (1,0),(0,1),(0,-1)]:
        adjacent_square = add(position, direction)
        if adjacent_square in G.nodes:
            yield adjacent_square


def get_relevant_edges(position, G):
    for adjacent_square in get_adjacent_squares(position, G):
        yield (position, adjacent_square)


def update_weights(G, units, position):
    for u,v in get_relevant_edges(position, G):
        if any(unit.position in [u, v] for unit in units if unit.is_alive()):
            if G.has_edge(u,v):
                #print("  Removing edge", u, v)
                G.remove_edge(u,v)
        else:
            if not G.has_edge(u,v):
                #print("  Adding edge", u, v)
                G.add_edge(u,v)


def get_adjacent_target(unit, G, units):
    adjacent_squares = list(get_adjacent_squares(unit.position, G))
    adjacent_enemy_units = (u for u in units if u.is_alive() and u.faction != unit.faction and u.position in adjacent_squares)
    return min(adjacent_enemy_units, key=lambda unit: (unit.hp, unit.position[1], unit.position[0]), default=None)


def dist(a, b):
   """
   >>> dist((1,1), (2,2))
   2
   >>> dist((1,1), (2,1))
   1
   >>> dist((1,1), (1,1))
   0
   >>> dist((3,5), (-1,-10))
   19
   """
   return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_paths(G, units, unit, potential_targets):
    for potential_target in potential_targets:
        for adjacent_square_target in get_adjacent_squares(potential_target.position, G):
            if adjacent_square_target not in (u.position for u in units if u.is_alive()):
                for adjacent_square_unit in get_adjacent_squares(unit.position, G):
                    if adjacent_square_unit not in (u.position for u in units if u.is_alive()):
                        try:
                            path = nx.shortest_path(G, adjacent_square_unit, adjacent_square_target)
                            if not any(u.position in path for u in units if u.is_alive()):
                                yield path
                        except nx.NetworkXNoPath:
                            pass


def answer(input):
    grid, units = parse_input(input)

    G = create_graph(grid)
    for unit in units:
        update_weights(G,units,unit.position)
    round = 0
    while True:
        for unit in sorted(units, key=lambda u: u.position[::-1]):
            if unit.is_alive():
                potential_targets = [u for u in units if u.is_alive() and unit.faction != u.faction]
                if not potential_targets:
                    hps = [u.hp for u in units if u.is_alive()]
                    print("Outcome: {0} * {1} = {2}".format(round, sum(hps), sum(hps) * round))
                    return sum(hps) * round

                target = get_adjacent_target(unit, G, units)
                if not target:
                    # move
                    paths = get_paths(G, units, unit, potential_targets)

                    path = min(paths, key=lambda path: (len(path), path[0][1], path[0][0]), default=None)
                    if path:
                        oldpos = unit.position
                        unit.position = path[0]
                        update_weights(G,units, unit.position)
                        update_weights(G,units, oldpos)

                    target = get_adjacent_target(unit, G, units)

                if target:
                    # attack
                    target.hp -= unit.ap
                    update_weights(G, units, target.position)

        round += 1


if __name__ == '__main__':
    print(answer(little_helper.get_input(15)))
