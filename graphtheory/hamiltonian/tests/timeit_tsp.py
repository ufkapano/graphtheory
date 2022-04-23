#!/usr/bin/env python3

import math
import random
import timeit
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.hamiltonian.tspbf import BruteForceTSPWithGraph
from graphtheory.hamiltonian.tspnn import NearestNeighborTSPWithGraph
from graphtheory.hamiltonian.tsprnn import RepeatedNearestNeighborTSPWithGraph
from graphtheory.hamiltonian.tspse import SortedEdgeTSPWithGraph
from graphtheory.hamiltonian.tspmst import PrimTSPWithGraph

# Euclidean TSP.
# Nodes are points in a unit square.
# Weights are distances.
V = 8               # number of nodes
E = V*(V-1) // 2       # number of edges
G = Graph(n=V, directed=False)
for i in range(V):
    G.add_node((random.random(), random.random()))
for source in G.iternodes():
    for target in G.iternodes():
        if source < target:
            x0, y0 = source
            x1, y1 = target
            weight = math.hypot(x1-x0, y1-y0)
            G.add_edge(Edge(source, target, weight))
#G.show()

print ( "Calculate parameters ..." )
print ( "Nodes: {} {}".format( G.v(), V ))
print ( "Edges: {} {}".format( G.e(), E ))
print ( "Directed: {}".format( G.is_directed() ))
print ( "Delta: {}".format( max(G.degree(node) for node in G.iternodes()) ))

print ( "Testing BruteForceTSPWithGraph ..." )
t1 = timeit.Timer(lambda: BruteForceTSPWithGraph(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing NearestNeighborTSPWithGraph ..." )
t1 = timeit.Timer(lambda: NearestNeighborTSPWithGraph(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing RepeatedNearestNeighborTSPWithGraph ..." )
t1 = timeit.Timer(lambda: RepeatedNearestNeighborTSPWithGraph(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing SortedEdgeTSPWithGraph ..." )
t1 = timeit.Timer(lambda: SortedEdgeTSPWithGraph(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing PrimTSPWithGraph ..." )
t1 = timeit.Timer(lambda: PrimTSPWithGraph(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

# EOF
