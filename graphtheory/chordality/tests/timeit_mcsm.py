#!/usr/bin/env python3

import timeit
import random
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.chordality.mcsm import MCS_M

n = 10
gf = GraphFactory(Graph)
G = gf.make_cyclic(n)
#G = gf.make_bipartite(n // 2, n-(n // 2), edge_probability=1)
#G = gf.make_grid(size=3)   # V=size*size

V = G.v()
E = G.e()
#G.show()

print ( "Testing MCS_M ..." )
t1 = timeit.Timer(lambda: MCS_M(G).run())
print ("{} {} {}".format(V, E, t1.timeit(1)) )   # single run

# EOF
