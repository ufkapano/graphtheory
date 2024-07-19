#!/usr/bin/env python3
#
# Finding a maximum idependent set for permutation graphs.

from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.permutations.permtools import make_random_perm
from graphtheory.permutations.permtools import make_star_perm
from graphtheory.permutations.permtools import make_bipartite_perm
from graphtheory.permutations.permtools import make_path_perm
from graphtheory.permutations.permtools import make_abstract_perm_graph
from lis1 import find_maximum_iset
from graphtheory.asteroidal.atfreeiset1 import ATFreeIndependentSet

# Tworzenie permutacji liczb od 0 do n-1.
n = 10
#perm = make_random_perm(n)   # random perm graph
#perm = make_star_perm(n)   # bipartite graph K_{1,n-1}
#perm = make_bipartite_perm(p=3, q=4)   # bipartite graph K_{p,q}
perm = make_path_perm(n)   # path graph P_n
assert len(perm) == n

print(perm)

iset = find_maximum_iset(perm)
print("max iset {}".format(iset))
print("cardinality {}".format(len(iset)))

G = make_abstract_perm_graph(perm)
algorithm = ATFreeIndependentSet(G)
algorithm.run()
assert algorithm.cardinality == len(iset)

# EOF
