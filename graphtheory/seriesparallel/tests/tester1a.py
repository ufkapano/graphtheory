#!/usr/bin/env python3

from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.seriesparallel.sptrees import find_sptree
from graphtheory.seriesparallel.spnodes import btree_print
from graphtheory.seriesparallel.spnodes import btree_print2

graph_factory = GraphFactory(Graph)
G = graph_factory.make_cyclic(n=5)   # n > 2
G.show()

T = find_sptree(G)
#T = find_sptree(G, fixed_ends=(0, 2))
#T = find_sptree(G, fixed_ends=(1, 3))
#T = find_sptree(G, fixed_ends=(0, 1))
btree_print2(T)

# EOF
