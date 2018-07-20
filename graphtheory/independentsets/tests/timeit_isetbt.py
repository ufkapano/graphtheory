#!/usr/bin/python

import timeit
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.independentsets.isetbt import BacktrackingIndependentSet

V = 10
graph_factory = GraphFactory(Graph)
probability = 0.5
G = graph_factory.make_random(V, False, probability)
#G = graph_factory.make_cyclic(V, False)
E = G.e()
#G.show()

print "Calculate parameters ..."
print "Nodes:", G.v(), V
print "Edges:", G.e(), E
print "Directed:", G.is_directed()

print "Testing BacktrackingIndependentSet ..."
t1 = timeit.Timer(lambda: BacktrackingIndependentSet(G).run())
print V, E, t1.timeit(1)            # pojedyncze wykonanie

# EOF
