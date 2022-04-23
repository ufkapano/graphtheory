#!/usr/bin/env python3

import timeit
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.traversing.dfs import DFSWithStack
from graphtheory.traversing.dfs import DFSWithRecursion
from graphtheory.traversing.dfs import SimpleDFS

V = 10
#V = 1000000   # OK for DFSWithStack
#V = 20000   # Naruszenie ochrony pamieci
graph_factory = GraphFactory(Graph)
G = graph_factory.make_cyclic(V, False)
E = G.e()
#G.show()

print ("Testing DFSWithStack ..." )
t1 = timeit.Timer(lambda: DFSWithStack(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ("Testing DFSWithRecursion ..." )
t1 = timeit.Timer(lambda: DFSWithRecursion(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ("Testing SimpleDFS ..." )
t1 = timeit.Timer(lambda: SimpleDFS(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

# EOF
