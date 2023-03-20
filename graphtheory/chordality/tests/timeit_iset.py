#!/usr/bin/env python3

import timeit
import random
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.chordality.chordaltools import make_random_ktree
from graphtheory.chordality.chordaltools import make_random_chordal
from graphtheory.chordality.peotools import find_maximum_independent_set

V = 10
G = make_random_chordal(V)
#G = make_random_ktree(V, V // 2)
E = G.e()
#G.show()

print ( "Calculate parameters ..." )
print ( "Nodes: {} {}".format(G.v(), V) )
print ( "Edges: {} {}".format(G.e(), E) )
print ( "Directed: {}".format(G.is_directed()) )

print ( "iset {}".format( find_maximum_independent_set(G, range(V)) ))

print ( "Testing find_maximum_independent_set ..." )
t1 = timeit.Timer(lambda: find_maximum_independent_set(G, range(V)))
print ("{} {} {}".format(V, E, t1.timeit(1)) )   # single run

# EOF
