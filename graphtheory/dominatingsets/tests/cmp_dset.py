#!/usr/bin/env python3

import timeit
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.dominatingsets.dsetbt import BacktrackingDominatingSet
from graphtheory.dominatingsets.dsethb import HybridDominatingSet
from graphtheory.dominatingsets.dsetus import UnorderedSequentialDominatingSet
from graphtheory.dominatingsets.dsetrs import RandomSequentialDominatingSet
from graphtheory.dominatingsets.dsetlf import LargestFirstDominatingSet

V = 10
graph_factory = GraphFactory(Graph)
G = graph_factory.make_random(V, False, edge_probability=0.5)
E = G.e()
#G.show()

print ( "Calculate parameters ..." )
print ( "Nodes: {} {}".format( G.v(), V ))
print ( "Edges: {} {}".format( G.e(), E ))
print ( "Directed: {}".format( G.is_directed() ))

algorithm = BacktrackingDominatingSet(G)
algorithm.run()
print ( "BT {}".format(algorithm.cardinality) )

algorithm = HybridDominatingSet(G)
algorithm.run()
print ( "HB {}".format(algorithm.cardinality) )

algorithm = UnorderedSequentialDominatingSet(G)
algorithm.run()
print ( "US {}".format(algorithm.cardinality) )

algorithm = RandomSequentialDominatingSet(G)
algorithm.run()
print ( "RS {}".format(algorithm.cardinality) )

algorithm = LargestFirstDominatingSet(G)
algorithm.run()
print ( "LF {}".format(algorithm.cardinality) )

# EOF
