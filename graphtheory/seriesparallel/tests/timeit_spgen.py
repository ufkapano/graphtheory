#!/usr/bin/env python3
#
# Sprawdzam szybkosc generatora sp-grafu.

import timeit
import random
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.seriesparallel.sptools import make_random_ktree
from graphtheory.seriesparallel.sptools import make_random_spgraph

V = 10

print ( "Testing make_random_spgraph ..." )
L = []
t1 = timeit.Timer(lambda: L.append(make_random_spgraph(V)))
result = t1.timeit(1)            # single run
E = L[0].e()
print ( "{} {} {}".format(V, E, result) )   # single run

print ( "Testing make_random_ktree ..." )
L = []
t1 = timeit.Timer(lambda: L.append(make_random_ktree(V, 2)))
result = t1.timeit(1)            # single run
E = L[0].e()
print ( "{} {} {}".format(V, E, result) )   # single run

# EOF
