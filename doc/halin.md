# HALIN GRAPHS

## RECOGNITION

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.planarity.halin import HalinGraph

graph_factory = GraphFactory(Graph)
G = graph_factory.make_prism(size=3)   # n=6
# 3-prism is a Halin graph

algorithm = HalinGraph(G)
algorithm.run()
print ( algorithm.outer )   # a set of nodes from the outer face
outer = algorithm.outer
~~~

## GENERATORS

~~~python
from graphtheory.planarity.halintools import make_halin
from graphtheory.planarity.halintools import make_halin_cubic
from graphtheory.planarity.halintools import make_halin_outer
from graphtheory.planarity.halintools import make_halin_cubic_outer
from graphtheory.structures.factory import GraphFactory

gf = GraphFactory(Graph)

G = gf.make_wheel(n=10)       # wheel graph
G = gf.make_necklace(n=10)   # necklace graph, n even
G = make_halin(n=7)
G = make_halin_cubic(n=10)   # n even
G, outer = make_halin_outer(n=7)
G, outer = make_halin_cubic_outer(n=10)   # n even
~~~

## PERFECT ELIMINATION ORDERING FOR CHORDAL COMPLETION (treewidth = 3)

~~~python
from graphtheory.planarity.halinpeo import HalinGraphPEO

algorithm = HalinGraphPEO(G, outer)
algorithm.run()
print ( algorithm.parent )  # inner tree (dict)
print ( algorithm.order )   # PEO (list)
~~~

## VERTEX COLORING

~~~python
from graphtheory.planarity.halinnodecolor import HalinNodeColoring

algorithm = HalinNodeColoring(G, outer)
algorithm.run()
print ( algorithm.parent )    # inner tree (dict)
print ( algorithm.color )     # dict with node colors
~~~

## TREE DECOMPOSITION

~~~python
from graphtheory.planarity.halintd import HalinGraphTreeDecomposition

algorithm = HalinGraphTreeDecomposition(G, outer)
algorithm.run()
print ( algorithm.parent )    # inner tree (dict)
print ( algorithm.order )   # PEO (list)
print ( algorithm.cliques )   # list of sets
print ( algorithm.td )   # td as a graph (nodes are tuples)
~~~

EOF
