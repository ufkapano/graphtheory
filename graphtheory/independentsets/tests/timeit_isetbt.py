#!/usr/bin/env python3

import timeit
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.independentsets.isetbt import BacktrackingIndependentSet

V = 10
graph_factory = GraphFactory(Graph)
G = graph_factory.make_random(V, False, edge_probability=0.5)
#G = graph_factory.make_cyclic(V, False)
E = G.e()
#G.show()

print ( "Calculate parameters ..." )
print ( "Nodes: {} {}".format( G.v(), V ))
print ( "Edges: {} {}".format( G.e(), E ))
print ( "Directed: {}".format( G.is_directed() ))

print ( "Testing BacktrackingIndependentSet ..." )
t1 = timeit.Timer(lambda: BacktrackingIndependentSet(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

# EOF
