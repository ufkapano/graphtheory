#!/usr/bin/env python3

from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.seriesparallel.sptrees import find_sptree
from graphtheory.seriesparallel.spnodes import btree_print
from graphtheory.seriesparallel.spnodes import btree_print2

#   0
#  /|\
# 5 | \
#  \|  \
#   4   3
#    \ /
#     2
#     |
#     1

N = 6           # number of nodes
G = Graph(N)
nodes = range(N)
edges = [Edge(1, 2), Edge(2, 3), Edge(3, 0), Edge(2, 4), Edge(4, 0),
 Edge(4, 5), Edge(5, 0)]
for node in nodes:
    G.add_node(node)
for edge in edges:
    G.add_edge(edge)

T = find_sptree(G)
btree_print2(T)

# EOF
