#!/usr/bin/env python3

import timeit
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.forests.treepeo import find_peo_tree

N = 10
gf = GraphFactory(Graph)
G = gf.make_tree(N)
assert G.v() == G.e() + 1
#G.show()

print ( "Testing find_peo_tree ..." )
t1 = timeit.Timer(lambda: find_peo_tree(G))
print ( "{} {} {}".format(N, G.e(), t1.timeit(1)) )   # single run

# EOF
