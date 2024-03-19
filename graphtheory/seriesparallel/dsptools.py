#!/usr/bin/env python3
#
# Generator sp-grafow skierowanych.
# Najpierw przygotowuje krawedzie, a potem wlasciwy graf.

import random
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph

def swap(L, i, j):
    """Swap items on the list."""
    L[i], L[j] = L[j], L[i]

def make_random_dspgraph(n):
    """Make a directed series-parallel graph with n vertices."""
    if n < 2:
        raise ValueError("bad n")
    graph = Graph(n=n, directed=True)   # directed graph
    for node in range(n):
        graph.add_node(node)
    source = 0
    sink = n-1
    idx = 1
    edge_list = [Edge(source, sink, idx)]
    idx += 1
    node = n-2
    while node > 0:
        # Losowanie krawedzi na ktorej bedzie operacja.
        i = random.randrange(0, len(edge_list))
        swap(edge_list, i, -1)
        edge = edge_list[-1]
        # Losowanie operacji.
        action = random.choice(("series", "parallel"))
        #print ("action", action)
        if action == "series":
            edge_list.pop()
            edge_list.append(Edge(edge.source, node, idx))
            idx += 1
            edge_list.append(Edge(node, edge.target, idx))
            idx += 1
        elif action == "parallel":
            edge_list.append(Edge(edge.source, node, idx))
            idx += 1
            edge_list.append(Edge(node, edge.target, idx))
            idx += 1
        node -= 1
    for edge in edge_list:
        graph.add_edge(edge)
    return graph

if __name__ == "__main__":

    print("Testing random directed sp-graph ...")
    G = make_random_dspgraph(10)
    G.show()

# EOF
