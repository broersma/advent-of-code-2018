import little_helper
import networkx as nx


def answer(input):
    G = create_graph(input)
    return ''.join(nx.lexicographical_topological_sort(G))


def create_graph(input):
    lines = input.split('\n')
    G=nx.DiGraph()
    for line in lines:
        a,b = line[5], line[36]
        G.add_edge(a,b)
    return G


if __name__ == '__main__':
    print(answer(little_helper.get_input(7)))
