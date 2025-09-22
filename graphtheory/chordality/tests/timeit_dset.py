#!/usr/bin/env python3

import timeit
from graphtheory.chordality.intervaltools import make_abstract_interval_graph
from graphtheory.chordality.intervaltools import make_2tree_interval
from graphtheory.chordality.intervaltools import make_ktree_interval
from graphtheory.chordality.intervaldset import IntervalDominatingSet


N = 10
#perm = make_2tree_interval(N)
perm = make_ktree_interval(N, N // 2)
G = make_abstract_interval_graph(perm)
V = G.v()
E = G.e()
#G.show()

print ( "Testing IntervalDominatingSet ..." )
t1 = timeit.Timer(lambda: IntervalDominatingSet(perm).run())
print ("{} {} {}".format(V, E, t1.timeit(1)) )   # single run

# EOF
