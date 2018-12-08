import little_helper
import networkx as nx


def answer(input):
    G = create_graph(input)
    topological_sort = nx.lexicographical_topological_sort(G)
    return ''.join(topological_sort)


def create_graph(input):
    lines = input.split('\n')
    return nx.DiGraph((line[5], line[36]) for line in lines)


if __name__ == '__main__':
    print(answer(little_helper.get_input(7)))
