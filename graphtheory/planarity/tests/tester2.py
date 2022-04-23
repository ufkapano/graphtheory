#!/usr/bin/env python3

from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.planarity.halin import HalinGraph
from graphtheory.planarity.wheels import is_wheel

V = 10
graph_factory = GraphFactory(Graph)
#G = graph_factory.make_prism(size=3)   # V=2*size=6
#G = graph_factory.make_complete(n=4)   # V=4
#G = graph_factory.make_wheel(n=V)   # V > 3
G = graph_factory.make_necklace(n=V)   # V even
G.show()

print ( "Recognition ..." )
print ( "is_wheel {}".format( is_wheel(G) ))
algorithm = HalinGraph(G)
algorithm.run()
print ( "outer {}".format( algorithm.outer ))
outer = algorithm.outer
#assert outer == set(range(1,V))   # wheel
assert outer == set(range(0,V,2)) | set([V-1])   # necklace

# EOF
