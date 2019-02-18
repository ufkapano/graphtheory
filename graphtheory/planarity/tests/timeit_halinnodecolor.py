#!/usr/bin/python

import timeit
import random
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.planarity.halinnodecolor import HalinNodeColoring
from graphtheory.planarity.halintools import make_halin_outer
from graphtheory.planarity.halintools import make_halin_cubic_outer

V = 1000
#G, outer = make_halin_outer(V)
G, outer = make_halin_cubic_outer(V)
E = G.e()
#G.show()

print "Testing HalinNodeColoring ..."
t1 = timeit.Timer(lambda: HalinNodeColoring(G, outer).run())
print V, E, t1.timeit(1)            # pojedyncze wykonanie

# EOF
