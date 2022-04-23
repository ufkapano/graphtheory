#!/usr/bin/env python3

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

print ( "Calculate parameters ..." )
print ( "Nodes: {} {}".format( G.v(), V ))
print ( "Edges: {} {}".format( G.e(), E ))
print ( "Directed: {}".format( G.is_directed() ))
print ( "Bipartite: {}".format( is_bipartite(G) ))

algorithm = BorieMatching(G)
algorithm.run()
print ( "BorieMatching cardinality: {}".format( algorithm.cardinality ))

algorithm = HopcroftKarpSet(G)
algorithm.run()
print ( "HopcroftKarpSet cardinality: {}".format( algorithm.cardinality ))

algorithm = MatchingFordFulkersonSet(G)
algorithm.run()
print ( "MatchingFordFulkersonSet cardinality: {}".format( algorithm.cardinality ))

print ( "Testing BorieMatching ..." )
t1 = timeit.Timer(lambda: BorieMatching(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing HopcroftKarpSet ..." )
t1 = timeit.Timer(lambda: HopcroftKarpSet(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing HopcroftKarpList ..." )
t1 = timeit.Timer(lambda: HopcroftKarpList(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing MatchingFordFulkersonSet ..." )
t1 = timeit.Timer(lambda: MatchingFordFulkersonSet(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing MatchingFordFulkersonList ..." )
t1 = timeit.Timer(lambda: MatchingFordFulkersonList(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing MatchingFordFulkersonColor ..." )
t1 = timeit.Timer(lambda: MatchingFordFulkersonColor(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

# EOF
