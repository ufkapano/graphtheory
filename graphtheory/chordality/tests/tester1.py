#!/usr/bin/env python3

import networkx as nx
import matplotlib.pyplot as plt

# 0-------5
# |\     /|
# | 1---4 |
# |/     \|
# 2-------3
G = nx.Graph()
vlist = [(0,0,2), (1,1,1), (2,0,0), (3,3,0), (4,2,1), (5,3,2)]
elist = [(0,1), (0,2), (0,5), (1,2), (1,4), (2,3), (3,4), (3,5), (4,5)]

for (v,x,y) in vlist:
    G.add_node(v, pos=(x,y))

for (u,v) in elist:
    G.add_edge(u, v)

pos = nx.get_node_attributes(G, 'pos')

nx.draw(G, pos, with_labels=True, font_weight='bold')

plt.show()

# EOF
