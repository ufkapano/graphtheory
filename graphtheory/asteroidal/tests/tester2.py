#!/usr/bin/env python3
#
# Przykladowy graf AT-free do ilustracji [1999 Broersma ...].

from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.asteroidal.atfree import ATFreeGraph

import networkx as nx
import matplotlib.pyplot as plt

# 0---1---2---3---4---5---6---7---8
# |   |   |   | X   X |   |   |   |
# 9--10--11--12--13--14--15--16--17
vlist = [(0,0,1), (1,1,1), (2,2,1), (3,3,1), (4,4,1), (5,5,1),
   (6,6,1), (7,7,1), (8,8,1), (9,0,0), (10,1,0), (11,2,0),
   (12,3,0), (13,4,0), (14,5,0), (15,6,0), (16,7,0), (17,8,0),
]
elist = [(0,1), (1,2), (2,3), (3,4), (4,5), (5,6), (6,7), (7,8),
    (0,9), (1,10), (2,11), (3,12), (3,13), (4,12), (4,14), (5,13),
    (5,14), (6,15), (7,16), (8,17), (9,10), (10,11), (11,12), (12,13),
    (13,14), (14,15), (15,16), (16,17),
]
G = nx.Graph()
H = Graph()

for (v,x,y) in vlist:
    G.add_node(v, pos=(x,y))
    H.add_node(v)

for (u,v) in elist:
    G.add_edge(u, v)
    H.add_edge(Edge(u, v))

print("Testing AT ...")
print("V {} E {}".format(H.v(), H.e()))
algorithm = ATFreeGraph(H)
algorithm.run()
print("AT {}".format(algorithm.asteroidal_triple))
assert algorithm.is_at_free()

# Rysowanie.
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, with_labels=True, font_weight='bold')
plt.show()

# EOF
