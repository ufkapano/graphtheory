#!/usr/bin/env python3

from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.seriesparallel.sptrees import find_sptree
from graphtheory.seriesparallel.spnodes import btree_print
from graphtheory.seriesparallel.spnodes import btree_print2

N = 2           # number of nodes
G = Graph(n=N)
nodes = range(N)
edges = [Edge(0, 1)]
for node in nodes:
    G.add_node(node)
for edge in edges:
    G.add_edge(edge)

T = find_sptree(G)
#T = find_sptree(G, fixed_ends=(0,1))
btree_print2(T)

# EOF
