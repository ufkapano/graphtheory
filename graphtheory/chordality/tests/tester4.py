#!/usr/bin/env python3

import networkx as nx
import matplotlib.pyplot as plt

#   ----J----
#  /         \
# F---G       H---I   graph from [2004 Berry]
# |     \   /     |
# A---B---C---D---E
G = nx.Graph()
vlist = [("A",0,0), ("B",1,0), ("C",2,0.5), ("D",3,0), ("E",4,0),
        ("F",0,1), ("G",1,1), ("H",3,1), ("I",4,1), ("J",1.5,2)]
elist = [("A","B"),("B","C"),("C","G"),("G","F"),
        ("A","F"),("C","D"),("D","E"),("E","I"),
        ("I","H"),("C","H"),("F","J"),("H","J")]

for (v,x,y) in vlist:
    G.add_node(v, pos=(x,y))

for (u,v) in elist:
    G.add_edge(u, v)

pos = nx.get_node_attributes(G, 'pos')

nx.draw(G, pos, with_labels=True, font_weight='bold')

plt.show()

# EOF
