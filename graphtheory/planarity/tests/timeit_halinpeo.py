#!/usr/bin/python
#
# Sprawdzam szybkosc wyznaczania PEO.
# Wnioski:

import timeit
import random
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.planarity.halin import HalinGraph
from graphtheory.planarity.halinpeo import HalinGraphPEO
from graphtheory.planarity.halintools import make_halin
from graphtheory.planarity.halintools import make_halin_cubic

V = 100000
G = make_halin(V)
#G = make_halin_cubic(V)
E = G.e()
#G.show()

# Rozpoznawanie outer.
algorithm = HalinGraph(G)
algorithm.run()
#print "outer", algorithm.outer
outer = algorithm.outer

print "Testing HalinGraphPEO ..."
t1 = timeit.Timer(lambda: HalinGraphPEO(G, outer).run())
print V, E, t1.timeit(1)            # pojedyncze wykonanie

# EOF
