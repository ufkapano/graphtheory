#!/usr/bin/env python3

import timeit
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.chordality.intervaltools import make_ktree_interval
from graphtheory.chordality.intervaltools import make_abstract_interval_graph
from graphtheory.asteroidal.atfree import ATFreeGraph

n = 10
# Graf C_n bedzie mial AT dla n > 5.
#graph_factory = GraphFactory(Graph)
#G = graph_factory.make_cyclic(n, False)

# k-tree jest tutaj interval (ale nie ogolnie!), czyli AT-free.
#perm = make_ktree_interval(n, 5)   # return double perm
perm = make_ktree_interval(n, n // 2)   # return double perm
assert len(perm) == 2*n
G = make_abstract_interval_graph(perm)

V = G.v()
E = G.e()

print ( "Testing ATFreeGraph ..." )
t1 = timeit.Timer(lambda: ATFreeGraph(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

# EOF
