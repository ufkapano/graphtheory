#!/usr/bin/python

import math
import random
import timeit
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.hamiltonian.tspbf import *
from graphtheory.hamiltonian.tspnn import *
from graphtheory.hamiltonian.tsprnn import *
from graphtheory.hamiltonian.tspse import *
from graphtheory.hamiltonian.tspmst import *

# Euclidean TSP.
# Nodes are points in a unit square.
# Weights are distances.
V = 8               # number of nodes
E = V*(V-1)/2       # number of edges
G = Graph(n=V, directed=False)
for i in xrange(V):
    G.add_node((random.random(), random.random()))
for source in G.iternodes():
    for target in G.iternodes():
        if source < target:
            x0, y0 = source
            x1, y1 = target
            weight = math.hypot(x1-x0, y1-y0)
            G.add_edge(Edge(source, target, weight))
G.show()

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

print "Testing PrimTSPWithGraph ..."
t1 = timeit.Timer(lambda: PrimTSPWithGraph(G).run())
print V, E, t1.timeit(1)            # pojedyncze wykonanie

# EOF
