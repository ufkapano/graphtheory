#!/usr/bin/python

import timeit
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.bipartiteness.bipartite import is_bipartite
from graphtheory.bipartiteness.hopcroftkarp import HopcroftKarpSet
from graphtheory.bipartiteness.hopcroftkarp import HopcroftKarpList
from graphtheory.bipartiteness.matching import MatchingFordFulkersonSet
from graphtheory.bipartiteness.matching import MatchingFordFulkersonList
from graphtheory.bipartiteness.matching import MatchingFordFulkersonColor
from graphtheory.forests.treemate import BorieMatching

V = 10
E = V-1   # drzewo
graph_factory = GraphFactory(Graph)
G = graph_factory.make_tree(V, False)
#G.show()

print "Calculate parameters ..."
print "Nodes:", G.v(), V
print "Edges:", G.e(), E
print "Directed:", G.is_directed()
print "Bipartite:", is_bipartite(G)

algorithm = BorieMatching(G)
algorithm.run()
print "BorieMatching cardinality:", algorithm.cardinality

algorithm = HopcroftKarpSet(G)
algorithm.run()
print "HopcroftKarpSet cardinality:", algorithm.cardinality

algorithm = MatchingFordFulkersonSet(G)
algorithm.run()
print "MatchingFordFulkersonSet cardinality:", algorithm.cardinality

print "Testing BorieMatching ..."
t1 = timeit.Timer(lambda: BorieMatching(G).run())
print V, E, t1.timeit(1)            # pojedyncze wykonanie

print "Testing HopcroftKarpSet ..."
t1 = timeit.Timer(lambda: HopcroftKarpSet(G).run())
print V, E, t1.timeit(1)            # pojedyncze wykonanie

print "Testing HopcroftKarpList ..."
t1 = timeit.Timer(lambda: HopcroftKarpList(G).run())
print V, E, t1.timeit(1)            # pojedyncze wykonanie

print "Testing MatchingFordFulkersonSet ..."
t1 = timeit.Timer(lambda: MatchingFordFulkersonSet(G).run())
print V, E, t1.timeit(1)            # pojedyncze wykonanie

print "Testing MatchingFordFulkersonList ..."
t1 = timeit.Timer(lambda: MatchingFordFulkersonList(G).run())
print V, E, t1.timeit(1)            # pojedyncze wykonanie

print "Testing MatchingFordFulkersonColor ..."
t1 = timeit.Timer(lambda: MatchingFordFulkersonColor(G).run())
print V, E, t1.timeit(1)            # pojedyncze wykonanie

# EOF
