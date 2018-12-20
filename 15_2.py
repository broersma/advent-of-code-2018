import little_helper
import networkx as nx


m = __import__("15_1")
parse_input = m.parse_input
create_graph = m.create_graph
update_weights = m.update_weights
get_adjacent_target = m.get_adjacent_target
get_paths = m.get_paths


def answer(input):
    grid, units = parse_input(input)

    ap = 13

    num_elves = len([u for u in units if u.is_alive() and u.faction == 'E'])
    for unit in units:
        if unit.faction == 'E':
            unit.ap = ap

    G = create_graph(grid)
    for unit in units:
        update_weights(G,units,unit.position)
    round = 0
    while True:
        for unit in sorted(units, key=lambda u: u.position[::-1]):
            if unit.is_alive():
                potential_targets = [u for u in units if u.is_alive() and unit.faction != u.faction]
                if not potential_targets:
                    print("Start elves: ",num_elves)
                    print("Current elves: ",len([u for u in units if u.is_alive() and u.faction == 'E']))
                    return ap

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
