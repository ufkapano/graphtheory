#!/usr/bin/env python3

from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.planarity.planarfactory import PlanarGraphFactory

# 0-------1-------2   figure 8 graph, 3 faces
# | inner | inner | outer
# |face(1)|face(2)| face(0)
# 5-------4-------3
V = 6
G = Graph(n=V)
for node in range(V):
    G.add_node(node)
e01 = Edge(0,1) ; e10 = ~e01
e12 = Edge(1,2) ; e21 = ~e12
e23 = Edge(2,3) ; e32 = ~e23
e34 = Edge(3,4) ; e43 = ~e34
e45 = Edge(4,5) ; e54 = ~e45
e05 = Edge(0,5) ; e50 = ~e05
e14 = Edge(1,4) ; e41 = ~e14
for edge in (e01, e12, e23, e34, e45, e05, e14):
    G.add_edge(edge)
G.show()

# Creating a topological graph.
G.edge_next = dict()
G.edge_prev = dict()
G.face2edge = dict()
G.edge2face = dict()
G.edge_next[e01] = e05 ; G.edge_prev[e01] = e05
G.edge_next[e05] = e01 ; G.edge_prev[e05] = e01
G.edge_next[e12] = e10 ; G.edge_prev[e12] = e14
G.edge_next[e10] = e14 ; G.edge_prev[e14] = e10
G.edge_next[e14] = e12 ; G.edge_prev[e10] = e12
G.edge_next[e23] = e21 ; G.edge_prev[e23] = e21
G.edge_next[e21] = e23 ; G.edge_prev[e21] = e23
G.edge_next[e34] = e32 ; G.edge_prev[e34] = e32
G.edge_next[e32] = e34 ; G.edge_prev[e32] = e34
G.edge_next[e45] = e43 ; G.edge_prev[e45] = e41
G.edge_next[e43] = e41 ; G.edge_prev[e41] = e43
G.edge_next[e41] = e45 ; G.edge_prev[e43] = e45
G.edge_next[e50] = e54 ; G.edge_prev[e50] = e54
G.edge_next[e54] = e50 ; G.edge_prev[e54] = e50

G.face2edge[0] = e05   # outer face
G.face2edge[1] = e01
G.face2edge[2] = e12

G.edge2face[e01] = 1
G.edge2face[e14] = 1
G.edge2face[e45] = 1
G.edge2face[e50] = 1
G.edge2face[e12] = 2
G.edge2face[e23] = 2
G.edge2face[e34] = 2
G.edge2face[e41] = 2
G.edge2face[e05] = 0
G.edge2face[e54] = 0
G.edge2face[e43] = 0
G.edge2face[e32] = 0
G.edge2face[e21] = 0
G.edge2face[e10] = 0

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
