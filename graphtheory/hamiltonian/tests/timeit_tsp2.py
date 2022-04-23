#!/usr/bin/env python3

import math
import random
import timeit
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.hamiltonian.tspbf import BruteForceTSPWithGraph
from graphtheory.hamiltonian.tspnn import NearestNeighborTSPWithGraph
from graphtheory.hamiltonian.tsprnn import RepeatedNearestNeighborTSPWithGraph
from graphtheory.hamiltonian.tspse import SortedEdgeTSPWithGraph

V = 8
graph_factory = GraphFactory(Graph)
G = graph_factory.make_complete(V, False)
E = G.e()
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

# EOF
