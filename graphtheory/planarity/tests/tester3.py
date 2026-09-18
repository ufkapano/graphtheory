#!/usr/bin/env python3

from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.planarity.planarfactory import PlanarGraphFactory

V = 5
gf = PlanarGraphFactory(Graph)
#G = gf.make_cyclic(n=V)   # cyclic topological graph
G = gf.make_wheel(n=V)   # wheel topological graph
G.show()

print( "V", G.v() )   # the number of nodes
print( "E", G.e() )   # the number of edges
print( "F", G.f() )   # the number of faces

for face in G.iterfaces():
    print( face )
start_edge = next(G.iteredges())
for edge in G.iterface(start_edge):
    print( edge )

print("edge_next ...")
print( G.edge_next )
print("edge_prev ...")
print( G.edge_prev )
print("face2edge ...")
print( G.face2edge )
print("edge2face ...")
print( G.edge2face )


# EOF
