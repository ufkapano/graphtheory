# PLANAR GRAPHS

## RECOGNITION

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph

# TO DO
~~~

## TOPOLOGICAL PLANAR GRAPH GENERATORS 

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.planarity.planarfactory import PlanarGraphFactory

gf = PlanarGraphFactory(Graph)

G = gf.make_cyclic(n=10)   # cyclic topological graph
G = gf.make_wheel(n=10)   # wheel topological graph

G.show()
print( G.v() )   # the number of nodes
print( G.e() )   # the number of edges
print( G.f() )   # the number of faces
for face in G.iterfaces():
    print( face )
for edge in G.iterface(start_edge):
    print( edge )
~~~

EOF
