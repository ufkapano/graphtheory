#!/usr/bin/env python3

import timeit
import random
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.chordality.chordaltools import make_random_ktree
from graphtheory.chordality.chordaltools import make_random_chordal
from graphtheory.chordality.peotools import find_peo_lex_bfs1
from graphtheory.chordality.peotools import find_peo_lex_bfs2

V = 10
G = make_random_chordal(V)
#G = make_random_ktree(V, V // 2)
E = G.e()
#G.show()

print ( "Testing find_peo_lex_bfs1 ..." )
t1 = timeit.Timer(lambda: find_peo_lex_bfs1(G))
print ("{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing find_peo_lex_bfs2 ..." )
t1 = timeit.Timer(lambda: find_peo_lex_bfs2(G))
print ("{} {} {}".format(V, E, t1.timeit(1)) )   # single run

# EOF
