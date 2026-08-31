#!/usr/bin/env python3

import timeit
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.bipartiteness.bipartite import is_bipartite
from graphtheory.connectivity.connected import is_connected
from graphtheory.bipartiteness.hopcroftkarp import HopcroftKarpSet
from graphtheory.bipartiteness.hopcroftkarp import HopcroftKarpList
from graphtheory.bipartiteness.matchingff import MatchingFordFulkersonSet
from graphtheory.bipartiteness.matchingff import MatchingFordFulkersonList
from graphtheory.bipartiteness.matchingff import MatchingFordFulkersonColor
from graphtheory.bipartiteness.matchingap import MatchingUsingAugmentingPath

V = 10
graph_factory = GraphFactory(Graph)
G = graph_factory.make_bipartite(n1=V // 2, n2=V // 2, directed=False,
    edge_probability=0.5)
#G = graph_factory.make_tree(n=V, False)
E = G.e()
#G.show()

print("Calculate parameters ...")
print("Nodes:", G.v(), V)
print("Edges:", G.e(), E)
print("Directed:", G.is_directed())
print("Bipartite:", is_bipartite(G))
print("Connected:", is_connected(G))

algorithm = MatchingUsingAugmentingPath(G)
algorithm.run()
print("MatchingUsingAugmentingPath cardinality:", algorithm.cardinality)

algorithm = HopcroftKarpSet(G)
algorithm.run()
print("HopcroftKarpSet cardinality:", algorithm.cardinality)

algorithm = MatchingFordFulkersonSet(G)
algorithm.run()
print("MatchingFordFulkersonSet cardinality:", algorithm.cardinality)

print()

print("Testing MatchingUsingAugmentingPath ...")
t1 = timeit.Timer(lambda: MatchingUsingAugmentingPath(G).run())
print(V, E, t1.timeit(1))   # pojedyncze wykonanie

print("Testing HopcroftKarpSet ...")
t1 = timeit.Timer(lambda: HopcroftKarpSet(G).run())
print(V, E, t1.timeit(1))   # pojedyncze wykonanie

print("Testing HopcroftKarpList ...")
t1 = timeit.Timer(lambda: HopcroftKarpList(G).run())
print(V, E, t1.timeit(1))   # pojedyncze wykonanie

print("Testing MatchingFordFulkersonSet ...")
t1 = timeit.Timer(lambda: MatchingFordFulkersonSet(G).run())
print(V, E, t1.timeit(1))   # pojedyncze wykonanie

print("Testing MatchingFordFulkersonList ...")
t1 = timeit.Timer(lambda: MatchingFordFulkersonList(G).run())
print(V, E, t1.timeit(1))   # pojedyncze wykonanie

print("Testing MatchingFordFulkersonColor ...")
t1 = timeit.Timer(lambda: MatchingFordFulkersonColor(G).run())
print(V, E, t1.timeit(1))   # pojedyncze wykonanie

# EOF
