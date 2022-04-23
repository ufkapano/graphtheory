#!/usr/bin/env python3

import timeit
import random
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.planarity.halin import HalinGraph
from graphtheory.planarity.halintools import make_halin_outer
from graphtheory.planarity.halintools import make_halin_cubic_outer

V = 10
graph_factory = GraphFactory(Graph)
G = graph_factory.make_necklace(n=V)   # V even
outer = set(range(0,V,2)) | set([V-1])   # necklace

#G, outer = make_halin_outer(V)
#G, outer = make_halin_cubic_outer(V)   # always finishing with 7-wheel
E = G.e()
#G.show()

print ( "Testing HalinGraph ..." )
t1 = timeit.Timer(lambda: HalinGraph(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

# EOF
