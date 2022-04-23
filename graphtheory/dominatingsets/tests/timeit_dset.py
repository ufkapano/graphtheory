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

print ( "Testing BacktrackingDominatingSet ..." )
t1 = timeit.Timer(lambda: BacktrackingDominatingSet(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing HybridDominatingSet ..." )
t1 = timeit.Timer(lambda: HybridDominatingSet(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing UnorderedSequentialDominatingSet ..." )
t1 = timeit.Timer(lambda: UnorderedSequentialDominatingSet(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing RandomSequentialDominatingSet ..." )
t1 = timeit.Timer(lambda: RandomSequentialDominatingSet(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing LargestFirstDominatingSet ..." )
t1 = timeit.Timer(lambda: LargestFirstDominatingSet(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

# EOF
