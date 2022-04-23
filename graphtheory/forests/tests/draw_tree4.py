#!/usr/bin/env python3

import math
import matplotlib.pyplot as plt
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.structures.points import Point
from graphtheory.forests.treeplot import TreePlot
from graphtheory.forests.treeplot import TreePlotRadiusAngle

# Complete binary tree
N = 50
V = 2 * N + 1   # the number of nodes
E = 2 * N       # the number of edges
G = Graph(V, False)
for i in range(V):
    G.add_node(i)
for i in range(N):
    G.add_edge(Edge(i, 2*i+1))
    G.add_edge(Edge(i, 2*i+2))
#G.show()

algorithm = TreePlot(G)   # only for V < 1e4
algorithm.run()
D = algorithm.point_dict   # node ---> point on the plane
#print ( D )

for edge in G.iteredges():
    x = [D[edge.source].x, D[edge.target].x]
    y = [D[edge.source].y, D[edge.target].y]
    plt.plot(x, y, 'k-')   # black line

x = [D[node].x for node in G.iternodes()]
y = [D[node].y for node in G.iternodes()]
plt.plot(x, y, 'bo')   # blue circle

plt.title("Random tree")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# EOF
