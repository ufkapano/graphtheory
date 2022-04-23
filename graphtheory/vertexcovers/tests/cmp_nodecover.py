#!/usr/bin/env python3

import timeit
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.vertexcovers.nodecoverapp import ApproximationNodeCover
from graphtheory.vertexcovers.nodecoverdeg import DegreeNodeCover
from graphtheory.vertexcovers.nodecoverlf import LargestFirstNodeCover

V = 10
graph_factory = GraphFactory(Graph)
G = graph_factory.make_random(V, False, edge_probability=0.5)
E = G.e()
#G.show()

print ( "Calculate parameters ..." )
print ( "Nodes: {} {}".format( G.v(), V ))
print ( "Edges: {} {}".format( G.e(), E ))
print ( "Directed: {}".format( G.is_directed() ))

algorithm = ApproximationNodeCover(G)
algorithm.run()
print ( "AppNC {}".format(algorithm.cardinality) )

algorithm = DegreeNodeCover(G)
algorithm.run()
print ( "DegNC {}".format(algorithm.cardinality) )

algorithm = LargestFirstNodeCover(G)
algorithm.run()
print ( "LFNC {}".format(algorithm.cardinality) )

# EOF
