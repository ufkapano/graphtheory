#!/usr/bin/env python3

from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.seriesparallel.sptrees import find_sptree
from graphtheory.seriesparallel.spnodes import btree_print
from graphtheory.seriesparallel.spnodes import btree_print2
from graphtheory.seriesparallel.dsptrees import find_dsptree

#   0    directed sp-graph
#  / \
# 1   3
#  \ /
#   2
#   |
#   4

N = 5   # the number of nodes
nodes = range(N)
edges = [Edge(0, 1), Edge(0, 3), Edge(1, 2), Edge(3, 2), Edge(2, 4)]
G = Graph(n=N, directed=True)
for node in nodes:
    G.add_node(node)
for edge in edges:
    G.add_edge(edge)

T = find_dsptree(G)
btree_print2(T)

# EOF
