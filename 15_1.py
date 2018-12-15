import little_helper

# defaultdict(list), defaultdict(int), deque.rotate/append
from collections import defaultdict, deque
# functools.reduce(function, iterable[, initializer])
from functools import reduce
# islice(seq, [start,] stop [, step])
from itertools import islice
import re
import networkx as nx
#import matplotlib.pyplot as plt
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
                units.append([x,y,c,id,3,200])
                id += 1
            elif c == 'g':
                units.append([x,y,'G',id,3,100])
                id += 1

        line = line.replace("G", ".").replace("E", ".").replace("g", ".")
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
                    c = unit[2]
            text += c
        for unit in sorted((unit for unit in units if unit[1] == y), key=lambda u: u[0]):
            text += " {0}({1}){2}".format(unit[2],unit[5],unit[3])                
        text += "\n"
        y += 1
    return text

def update_weights(G, units):
    for u,v,data in G.edges(data=True):
        weight = 99999 if any(tuple(unit[:2]) in [u, v] for unit in units if unit[5] > 0) else 1
        data['weight'] = weight
        
def create_graph(grid):    
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
    
def pr(unit):
    return "{0}({1}){2}".format(unit[2],unit[5],unit[3])
    
def answer(input):
    grid, units = parse_input(input)
    
    G = create_graph(grid)
    update_weights(G,units)
    round = 0
    while True:
    #for _ in range(3):
        for unit in sorted(units, key=lambda u: (u[1], u[0])):
            if unit[5] > 0:
                #print(pr(unit), end='')
                potential_targets = [u for u in units if unit[2] != u[2] and u[5] > 0]
                #print("->",', '.join([pr(u) for u in potential_targets]))
                if len(potential_targets) == 0:
                    hps = [u[5] for u in units if u[5] > 0]
                    #print(show_grid(grid, units))
                    print("Outcome: {0} * {1} = {2}".format(round, sum(hps), sum(hps) * round))
                    print("Outcome 2: {0} * {1} = {2}".format(round, sum(hps)-3, (sum(hps)-3) * round))
                    return sum(hps) * round
                
                
                # move
                paths = []
                for potential_target in potential_targets:
                    for dx,dy in [(-1,0), (1,0),(0,1),(0,-1)]:
                        adjacent_square = (potential_target[0] + dx, potential_target[1] + dy)
                        if adjacent_square in G.nodes and adjacent_square not in ((u[0],u[1]) for u in units if unit[3] != u[3]):
                            paths += [path for path in nx.all_shortest_paths(G, tuple(unit[:2]), adjacent_square, weight='weight')]
                paths = [path for path in paths if len(path) == 1 or (len(path)>1 and not any(tuple(u[:2]) in path[1:-1] for u in units if u[5] > 0))]
                
                if len(paths) > 0:
                    shortest_path_len = min(set(len(path) for path in paths))
                    if shortest_path_len > 1:
                        paths_sorted_by_len = (path for path in paths if len(path) == shortest_path_len)
                        paths_sorted_by_first_step = sorted(paths_sorted_by_len, key=lambda path: (path[1][1], path[1][0]))
                        path = next(paths_sorted_by_first_step)
                        unit[0] = path[1][0]
                        unit[1] = path[1][1]
                        update_weights(G,units)
                        
                #attack
                adjacent_squares = [(unit[0] + dx, unit[1] + dy) for dx,dy in [(-1,0), (1,0),(0,1),(0,-1)]]
                potential_targets = sorted((u for u in units if unit[2] != u[2] and tuple(u[:2]) in adjacent_squares), key=lambda unit: (unit[5],unit[1], unit[0]))
                for potential_target in potential_targets:
                    #if round == 46:
                    #    print(unit, "->", potential_target)
                    potential_target[5] -= unit[4]
                    update_weights(G,units)
                    break


        # remove dead units
        units = [u for u in units if u[5] > 0]

        round += 1
        #print("After", round, "rounds")
        #print(show_grid(grid, units))
        
    hps = [u[5] for u in units]
    #print(hps)
    print("Combat ends after {0} full rounds\nElves win with {1} total hit points left\nOutcome: {0} * {1} = {2}".format(round, sum(hps), sum(hps) * round))
    return sum(hps) * round


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
