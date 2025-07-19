#!/usr/bin/env python3
#
# Finding a miximume weight clique in a weighted bipartite graph.

import random
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory

N = 10
gf = GraphFactory(Graph)
#G = gf.make_tree(N)
# make_bipartite(self, n1=1, n2=1, directed=False, edge_probability=0.5):
G = gf.make_bipartite(N // 2, N - N // 2)
G.show()

w = list(range(1, N+1))
random.shuffle(w)
D = dict(zip(G.iternodes(), w))   # random weights
print(D)

max_clique = max(G.iteredges(), key=lambda edge: D[edge.source] + D[edge.target])
max_weight = D[max_clique.source] + D[max_clique.target]
print(max_clique, max_weight)

# EOF
