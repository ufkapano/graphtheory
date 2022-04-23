#!/usr/bin/env python3

import timeit
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.traversing.bfs import BFSWithQueue
from graphtheory.traversing.bfs import SimpleBFS

V = 10
#V = 1000000   # OK
graph_factory = GraphFactory(Graph)
G = graph_factory.make_cyclic(V, False)
E = G.e()
#G.show()

print ("Testing BFSWithQueue ..." )
t1 = timeit.Timer(lambda: BFSWithQueue(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ("Testing SimpleBFS ..." )
t1 = timeit.Timer(lambda: SimpleBFS(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

# EOF
