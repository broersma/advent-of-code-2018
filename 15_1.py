import little_helper

# defaultdict(list), defaultdict(int), deque.rotate/append
from collections import defaultdict, deque
# functools.reduce(function, iterable[, initializer])
from functools import reduce
# islice(seq, [start,] stop [, step])
from itertools import islice
import re
import networkx as nx
import matplotlib.pyplot as plt
#from numba import jit
from sys import exit

day = 15
if __file__.endswith("_2"):
    m = __import__(day + "_1")
    
def parse_input(input):
    input = input.split('\n')
    y = 0
    units = []
    grid = []
    id = 0
    for line in input:
        for x, c in enumerate(line):
            if c in ['E','G']:
                units.append([x,y,c,id])
                id += 1

        line = line.replace("G", ".").replace("E", ".")
        grid.append(line)
        y += 1
    return grid, units
    
def show_grid(grid, units):
    text = ""
    y = 0
    for line in grid:
        for x, c in enumerate(line):
            for unit in units:
                if unit[0] == x and unit[1] == y:
                    c = str(unit[3])
            text += c
        text += "\n"
        y += 1
    return text
    
def update_weights(G, units):
    for u,v,data in G.edges(data=True):
        data['weight'] = 99999 if any(tuple(unit[:2]) in [u,v] for unit in units) else 1 

def create_graph(grid):    
    G = nx.Graph()
    for y,line in enumerate(grid):
        for x,c in enumerate(line):
            if grid[y][x] == '.':
                G.add_node((x,y))
                for dx,dy in [(-1,0), (1,0),(0,1),(0,-1)]:
                    if grid[y+dy][x+dx] == '.':
                        G.add_edge((x,y),(x+dx,y+dy))
    return G
def answer(input):
    grid, units = parse_input(input)
    
    G = create_graph(grid)
    update_weights(G,units)
    
    #nx.draw(G, with_labels=True)
    #plt.show()
    #plt.savefig("path.png")
    print(nx.shortest_path(G, tuple(units[0][:2]), tuple(units[1][:2]), weight='weight'))
    #print(nx.shortest_path(G, (10,1), (10,5), weight='weight'))
    print(show_grid(grid, units))
    #while True:
    for i in range(3):
        # move
        for unit in sorted(units, key=lambda unit: tuple(unit[:2][::-1])):
            paths = []
            for potential_target in (u for u in units if unit[3] != u[3] and unit[2] != u[2]):
                for dx,dy in [(-1,0), (1,0),(0,1),(0,-1)]:
                    adjacent_square = (potential_target[0] + dx, potential_target[1] + dy)
                    # TODO detect if we're next to the potential target and attack
                    if adjacent_square in G.nodes and adjacent_square not in ((u[0],u[1]) for u in units if unit[3] != u[3]):
                        paths += [path for path in nx.all_shortest_paths(G, tuple(unit[:2]), adjacent_square, weight='weight')]
            if len(paths) > 0:
                shortest_path_len = min(set(len(path) for path in paths))
                if shortest_path_len > 1:
                    paths_sorted_by_len = (path for path in paths if len(path) == shortest_path_len)
                    paths_sorted_by_first_step = sorted(paths_sorted_by_len, key=lambda path: (path[1][1], path[1][0]))
                    path = paths_sorted_by_first_step[0]
                    #print(unit[3],unit[:2], end=' -> ')
                    unit[0] = path[1][0]
                    unit[1] = path[1][1]
                    #print(unit[:2])
                    update_weights(G,units)
        
        print(show_grid(grid, units))
        
        # attack
        for unit in sorted(units, key=lambda unit: tuple(unit[:2][::-1])):
            print(unit)
            potential_targets = []
            adjacent_squares = ((unit[0] + dx, unit[1] + dy) for dx,dy in [(-1,0), (1,0),(0,1),(0,-1)])
            for potential_target in (u for u in units if unit[2] != u[2]):
                if tuple(potential_target[:2]) in adjacent_squares:
                    print(unit,"attack", potential_target)
    return #show_grid(grid, units)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('level', type=int, default=-1, nargs='?')
    args = parser.parse_args()
    level = args.level

    input = little_helper.get_input(day)
    the_answer = answer(input)

    if level == -1:
        print(the_answer)
    else:
        print("Submitting", the_answer, "for day", day,"star", level)
        print(little_helper.submit(the_answer, level, day))
