#!/usr/bin/python

import math
import random
import timeit
from graphtheory.structures.factory import GraphFactory
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.hamiltonian.tspbf import *
from graphtheory.hamiltonian.tspnn import *
from graphtheory.hamiltonian.tsprnn import *
from graphtheory.hamiltonian.tspse import *

V = 8
graph_factory = GraphFactory(Graph)
G = graph_factory.make_complete(V, False)
E = G.e()
#G.show()

print "Calculate parameters ..."
print "Nodes:", G.v(), V
print "Edges:", G.e(), E
print "Directed:", G.is_directed()
print "Delta:", max(G.degree(node) for node in G.iternodes())

print "Testing BruteForceTSPWithGraph ..."
t1 = timeit.Timer(lambda: BruteForceTSPWithGraph(G).run())
print V, E, t1.timeit(1)            # pojedyncze wykonanie

print "Testing NearestNeighborTSPWithGraph ..."
t1 = timeit.Timer(lambda: NearestNeighborTSPWithGraph(G).run())
print V, E, t1.timeit(1)            # pojedyncze wykonanie

print "Testing RepeatedNearestNeighborTSPWithGraph ..."
t1 = timeit.Timer(lambda: RepeatedNearestNeighborTSPWithGraph(G).run())
print V, E, t1.timeit(1)            # pojedyncze wykonanie

print "Testing SortedEdgeTSPWithGraph ..."
t1 = timeit.Timer(lambda: SortedEdgeTSPWithGraph(G).run())
print V, E, t1.timeit(1)            # pojedyncze wykonanie

# EOF
