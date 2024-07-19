#!/usr/bin/env python3
#
# Testowanie funkcji i klasy do znajdowania PEO dla perm graph lub dopelnienia.
# Wnioski.
# Wersja z klasa jest okolo 5 procent wolniejsza, ale ogolnie czas O(n^4).

import timeit
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.permutations.permtools import make_bipartite_perm
from graphtheory.permutations.permtools import make_abstract_perm_graph
from graphtheory.permutations.permpeo import PermGraphPEO

N = 10
perm = make_bipartite_perm(p=N // 2, q=N-(N // 2))   # make perm for K_{p,q}
assert len(perm) == N
G = make_abstract_perm_graph(perm)
#G.show()

V = G.v()
E = G.e()

print ( "Testing PermGraphPEO ..." )
t1 = timeit.Timer(lambda: PermGraphPEO(perm).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

# EOF
