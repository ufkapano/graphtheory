#!/usr/bin/env python3
#
# Sprawdzam szybkosc rozpoznawania sp-grafu.

import timeit
import random
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.seriesparallel.sptools import make_random_ktree
from graphtheory.seriesparallel.sptools import make_random_spgraph
from graphtheory.seriesparallel.sptrees import find_sptree
from graphtheory.seriesparallel.spnodes import btree_print

V = 10
#G = make_random_spgraph(V)
G = make_random_ktree(V, 2)
E = G.e()
#G.show()

T = find_sptree(G)
btree_print(T)

print ( "Testing find_sptree ..." )
t1 = timeit.Timer(lambda: find_sptree(G))
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

# EOF
