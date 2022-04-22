#!/usr/bin/env python3

import timeit
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.connectivity.connected import is_connected

V = 10
# V = 1000000   # OK for is_connected with BFS
graph_factory = GraphFactory(Graph)
G = graph_factory.make_cyclic(V, False)
E = G.e()
#G.show()

print ("Testing is_connected ..." )
t1 = timeit.Timer(lambda: is_connected(G))
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

# EOF
