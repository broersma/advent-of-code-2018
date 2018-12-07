import little_helper
import networkx as nx
create_graph = __import__("7_1").create_graph


def answer(input):
    G = create_graph(input)

    done_nodes = set()

    worker_nodes = dict()
    for i in range(5):
        worker_nodes[i] = None

    time = 0
    while len(done_nodes) != len(G.nodes):
        for node in G.nodes:
            if node not in done_nodes and not any(node == value[0] for value in worker_nodes.values() if value):
                if all(ancestor in done_nodes for ancestor in nx.ancestors(G, node)):
                    for i in worker_nodes:
                        if not worker_nodes[i]:
                            worker_nodes[i] = (node, ord(node) - 4) #-64+60
                            break
        for i in worker_nodes:
            if worker_nodes[i]:
                node, time_left = worker_nodes[i]
                if time_left == 1:
                    done_nodes.add(node)
                    worker_nodes[i] = None
                else:
                    worker_nodes[i] = (node, time_left-1)
        time+=1
    return time


if __name__ == '__main__':
    print(answer(little_helper.get_input(7)))
