#!/usr/bin/env python3

from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.seriesparallel.sptrees import find_sptree
from graphtheory.seriesparallel.spnodes import btree_print
from graphtheory.seriesparallel.spnodes import btree_print2

N = 10           # number of nodes
G = Graph(n=N)
nodes = range(N)
edges = [Edge(0, 1, 1), Edge(1, 2, 2), Edge(2, 3, 3),
Edge(0, 4, 4), Edge(4, 5, 5), Edge(5, 3, 6),
Edge(0, 6, 9), Edge(6, 7, 8), Edge(7, 3, 7),
Edge(3, 8, 10), Edge(8, 9, 11), 
]
for node in nodes:
    G.add_node(node)
for edge in edges:
    G.add_edge(edge)

#T = find_sptree(G)
T = find_sptree(G, fixed_ends=(0,3))
btree_print2(T)

# EOF
