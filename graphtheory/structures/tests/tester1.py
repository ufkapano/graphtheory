#!/usr/bin/env python3

from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.traversing.bfs import SimpleBFS

# A---D---E
# | / |
# B---C
G = Graph()   # an undirected graph
for node in "ABCDE":
    G.add_node(node)
edge_list = [Edge("A","B"), Edge("A","D"), Edge("B","C"), 
    Edge("B","D"), Edge("C","D"), Edge("D","E")]
#edge_list = [("A","B"), ("A","D"), ("B","C"), ("B","D"), ("C","D"), ("D","E")]
for edge in edge_list:
    G.add_edge(edge)
G.show()

assert not G.is_directed()
assert G.v() == 5   # the number of vertices
assert G.e() == 6   # the number of edges
assert sorted(G.degree(node) for node in G.iternodes()) == [1, 2, 2, 3, 4]

# Using node and edge attributes.
color_dict = dict()
for node in G.iternodes():
    color_dict[node] = 'black'

length_dict = dict()
for edge in G.iteredges():
    length_dict[edge] = 1

order = []
algorithm = SimpleBFS(G)
algorithm.run("A", pre_action=lambda node: order.append(node))
print(order)   # visited nodes ['A', 'B', 'D', 'C', 'E']
print(algorithm.parent)   # BFS tree as a dict
# {'A': None, 'B': 'A', 'D': 'A', 'C': 'B', 'E': 'D'}

algorithm.path("A","E")   # ['A', 'D', 'E']

assert algorithm.dag.is_directed()
algorithm.dag.show()    # BFS tree as a directed graph

# EOF
