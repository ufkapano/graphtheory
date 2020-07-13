#!/usr/bin/python

import timeit
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.vertexcovers.nodecoverlf import LargestFirstNodeCover

V = 10
graph_factory = GraphFactory(Graph)
G = graph_factory.make_random(V, False, edge_probability=0.2)
E = G.e()
#G.show()

print ( "Testing LargestFirstNodeCover ..." )
t1 = timeit.Timer(lambda: LargestFirstNodeCover(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

# EOF
