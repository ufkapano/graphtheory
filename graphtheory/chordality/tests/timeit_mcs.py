#!/usr/bin/env python3

import timeit
import random
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.chordality.chordaltools import make_random_ktree
from graphtheory.chordality.chordaltools import make_random_chordal
from graphtheory.chordality.peotools import find_peo_mcs1
from graphtheory.chordality.peotools import find_peo_mcs2
from graphtheory.chordality.peotools import find_peo_mcs3

V = 10
G = make_random_chordal(V)
#G = make_random_ktree(V, V // 2)
E = G.e()
#G.show()

print ( "Testing find_peo_mcs1 ..." )
t1 = timeit.Timer(lambda: find_peo_mcs1(G))
print ("{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing find_peo_mcs2 ..." )
t1 = timeit.Timer(lambda: find_peo_mcs2(G))
print ("{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing find_peo_mcs3 ..." )
t1 = timeit.Timer(lambda: find_peo_mcs3(G))
print ("{} {} {}".format(V, E, t1.timeit(1)) )   # single run

# EOF
