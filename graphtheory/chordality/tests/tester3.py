#!/usr/bin/env python3

from graphtheory.structures.graphs import Graph
from graphtheory.planarity.halintools import make_halin
from graphtheory.planarity.halintools import make_halin_cubic
from graphtheory.planarity.halintools import make_halin_outer
from graphtheory.planarity.halintools import make_halin_cubic_outer
from graphtheory.structures.factory import GraphFactory
from graphtheory.planarity.halinpeo import HalinGraphPEO
from graphtheory.planarity.halintd import HalinGraphTreeDecomposition

# Generowanie grafu Halina.
gf = GraphFactory(Graph)
#G = gf.make_wheel(n=10)       # wheel graph
#G = gf.make_necklace(n=10)   # necklace graph, n even
#G = make_halin(n=7)
#G = make_halin_cubic(n=10)   # n even

# Generowanie grafu Halina ze zbiorem wierzcholkow nalezacych do cyklu.
G, outer = make_halin_outer(n=10)
#G, outer = make_halin_cubic_outer(n=10)   # n even

# Wyznaczanie PEO dla chordal completion.
print("finding PEO ...")
algorithm = HalinGraphPEO(G, outer)
algorithm.run()
print(algorithm.parent)  # inner tree (dict)
print(algorithm.order)   # PEO (list)

# Wyznaczanie TD.
print("finding TD ...")
algorithm = HalinGraphTreeDecomposition(G, outer)
algorithm.run()
print(algorithm.parent)    # inner tree (dict)
print(algorithm.order)   # PEO (list)
print(algorithm.cliques)   # list of sets
print(algorithm.td)   # td as a graph (nodes are tuples)
algorithm.td.show()

assert algorithm.td.v() == algorithm.td.e() + 1   # tree
treewidth = max(len(bag) for bag in algorithm.td.iternodes()) - 1
print("treewidth", treewidth)

# EOF
