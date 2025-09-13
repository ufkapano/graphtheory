#!/usr/bin/env python3

import timeit
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.bipartiteness.bipartite import BipartiteGraphBFS
from graphtheory.forests.treewdset import TreeWeightedDominatingSet1
from graphtheory.forests.treewdset import TreeWeightedDominatingSet2
from graphtheory.forests.treewidset import TreeWeightedIndependentDominatingSet1
from graphtheory.forests.treewidset import TreeWeightedIndependentDominatingSet2

V = 10
gf = GraphFactory(Graph)
G = gf.make_tree(n=V)   # random tree
E = G.e()
#G.show()

# Kolorowanie wierzcholkow drzewa.
algorithm = BipartiteGraphBFS(G)
algorithm.run()
# Przydzielam wagi 1 oraz 3.
weights = dict((node, 1 + 2 * algorithm.color[node]) for node in G.iternodes())
#print(weights)

print ( "Testing TreeWeightedDominatingSet1 ..." )
t1 = timeit.Timer(lambda: TreeWeightedDominatingSet1(G, weights).run())
print ("{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing TreeWeightedDominatingSet2 ..." )
t1 = timeit.Timer(lambda: TreeWeightedDominatingSet2(G, weights).run())
print ("{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing TreeWeightedIndependentDominatingSet1 ..." )
t1 = timeit.Timer(lambda: TreeWeightedIndependentDominatingSet1(G, weights).run())
print ("{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing TreeWeightedIndependentDominatingSet2 ..." )
t1 = timeit.Timer(lambda: TreeWeightedIndependentDominatingSet2(G, weights).run())
print ("{} {} {}".format(V, E, t1.timeit(1)) )   # single run

# EOF
