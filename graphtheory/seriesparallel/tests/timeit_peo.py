#!/usr/bin/env python3
#
# Sprawdzam szybkosc generatora sp-grafu.
# Wnioski:
# Wersja 2 jest o kilka procent szybsza dla 2-tree, ale dla
# sp-grafow przypadkowych jest prawie tak samo szybka.

import timeit
import random
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.seriesparallel.sptools import make_random_ktree
from graphtheory.seriesparallel.sptools import make_random_spgraph
from graphtheory.seriesparallel.sptools import find_peo_spgraph1
from graphtheory.seriesparallel.sptools import find_peo_spgraph2

V = 100
G = make_random_spgraph(V)
#G = make_random_ktree(V, 2)
E = G.e()
#G.show()

print ( "Testing find_peo_spgraph1 ..." )
t1 = timeit.Timer(lambda: find_peo_spgraph1(G))
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing find_peo_spgraph2 ..." )
t1 = timeit.Timer(lambda: find_peo_spgraph2(G))
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

# EOF
