#!/usr/bin/python

from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.planarity.halin import HalinGraph
from graphtheory.planarity.halinpeo import HalinGraphPEO
from graphtheory.planarity.halinnodecolor import HalinNodeColoring
from graphtheory.planarity.halintools import make_halin
from graphtheory.planarity.halintools import make_halin_cubic
from graphtheory.planarity.wheels import is_wheel

graph_factory = GraphFactory(Graph)
#G = graph_factory.make_prism(3)   # V=2*size=6
#G = graph_factory.make_complete(4)   # V=4
#G = graph_factory.make_wheel(5)   # V > 3
#G = make_halin(7)    # V > 3
G = make_halin_cubic(8)   # V even
G.show()

print "Recognition ..."
print "is_wheel", is_wheel(G)
algorithm = HalinGraph(G)
algorithm.run()
print "outer", algorithm.outer
outer = algorithm.outer

print "Vertex coloring ..."
algorithm = HalinNodeColoring(G, outer)
algorithm.run()
print "parent", algorithm.parent
print "color", algorithm.color

print "Finding PEO for chordal completion ..."
algorithm = HalinGraphPEO(G, outer)
algorithm.run()
print "parent", algorithm.parent
print "order", algorithm.order

# EOF
