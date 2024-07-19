#!/usr/bin/env python3
#
# Finding a maximum idependent set for interval graphs.

from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.chordality.intervaltools import make_random_interval
from graphtheory.chordality.intervaltools import make_path_interval
from graphtheory.chordality.intervaltools import make_tepee_interval
from graphtheory.chordality.intervaltools import make_2tree_interval
from graphtheory.chordality.intervaltools import make_star_interval
from graphtheory.chordality.intervaltools import make_ktree_interval
from graphtheory.chordality.intervaltools import make_abstract_interval_graph
from graphtheory.chordality.intervaltools import interval_maximum_iset
from graphtheory.asteroidal.atfreeiset1 import ATFreeIndependentSet

# Tworzenie reprezentacji permutacyjnej.
n = 10
#perm = make_random_interval(n)   # random interval graph
perm = make_path_interval(n)   # P_n graph
#perm = make_tepee_interval(n)   # tepee graph
#perm = make_2tree_interval(n)   # 2-tree
#perm = make_star_interval(n)   # K_{1,n-1} graph
#perm = make_ktree_interval(n, k=n // 2)   # interval k-tree
assert len(perm) == 2*n

print(perm)

iset = interval_maximum_iset(perm)
print("max iset {}".format(iset))
print("cardinality {}".format(len(iset)))

G = make_abstract_interval_graph(perm)
algorithm = ATFreeIndependentSet(G)
algorithm.run()
assert algorithm.cardinality == len(iset)

# EOF
