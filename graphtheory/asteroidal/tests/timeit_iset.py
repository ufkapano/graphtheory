#!/usr/bin/env python3
#
# Testing max iset.

import timeit
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory

from graphtheory.permutations.permtools import make_bipartite_perm
from graphtheory.permutations.permtools import make_path_perm
from graphtheory.permutations.permtools import make_abstract_perm_graph

from graphtheory.chordality.intervaltools import make_path_interval
from graphtheory.chordality.intervaltools import make_tepee_interval
from graphtheory.chordality.intervaltools import make_2tree_interval
from graphtheory.chordality.intervaltools import make_star_interval
from graphtheory.chordality.intervaltools import make_ktree_interval
from graphtheory.chordality.intervaltools import make_abstract_interval_graph

from graphtheory.asteroidal.atfreeiset1 import ATFreeIndependentSet as ATFreeIndependentSet1
from graphtheory.asteroidal.atfreeiset2 import ATFreeIndependentSet as ATFreeIndependentSet2

n = 10

# Permutation graphs.
perm = make_bipartite_perm(p=n//2, q=n-(n//2))   # bipartite graph K_{p,q}
#perm = make_path_perm(n)   # path graph P_n
assert len(perm) == n
G = make_abstract_perm_graph(perm)

# Interval graphs.
#perm = make_path_interval(n)   # P_n graph
#perm = make_tepee_interval(n)   # tepee graph
#perm = make_2tree_interval(n)   # 2-tree
#perm = make_star_interval(n)   # K_{1,n-1} graph
#perm = make_ktree_interval(n, k=n // 2)   # interval k-tree
#assert len(perm) == 2*n
#G = make_abstract_interval_graph(perm)

V = G.v()
E = G.e()

print ( "Testing ATFreeIndependentSet1 ..." )
t1 = timeit.Timer(lambda: ATFreeIndependentSet1(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing ATFreeIndependentSet2 ..." )
t1 = timeit.Timer(lambda: ATFreeIndependentSet2(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

# EOF
