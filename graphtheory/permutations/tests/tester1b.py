#!/usr/bin/env python3
#
# Generating all perm graphs.
# Finding cycles without chords in connected graphs.
# Plotting nonchordal perm graphs.

import itertools
import networkx as nx
import matplotlib.pyplot as plt
from graphtheory.permutations.permtools import perm_is_connected
from graphtheory.permutations.permtools import make_abstract_perm_graph
from graphtheory.chordality.peotools import find_peo_lex_bfs
from graphtheory.chordality.peotools import is_peo1, is_peo2

n = 5
counter = 0
for perm in itertools.permutations(range(n)):
#for perm in [(3,4,5,0,1,2)]:   # K_{3,3}, jest 9 cykli C_4
#for perm in [(4,5,2,3,0,1)]:   # sa 3 cykle C_4
    if not perm_is_connected(perm):   # O(n) time
        continue
    graph = make_abstract_perm_graph(perm)
    order = find_peo_lex_bfs(graph)
    if is_peo1(graph, order):   # pomijamy chordal graphs
        continue
    print(perm)
    #graph.show()
    # Szukam 4 liczb tworzacych indukowany graf C_4.
    for (i,j,k,r) in itertools.combinations(range(n),4):
        if perm[k] < perm[r] < perm[i] < perm[j]:
            print("idx",i,j,k,r,"perm",perm[i],perm[j],perm[k],perm[r])
    counter += 1

    filename = "".join(map(str,perm)) + ".png"
    print(filename)
    G = nx.Graph()   # an empty undirected graph
    for node in graph.iternodes():
        G.add_node(node)
    for edge in graph.iteredges():
        G.add_edge(edge.source, edge.target)
    # Rysowanie grafu.
    nx.draw(G, with_labels=True, font_weight='bold')
    #plt.savefig(filename)
    plt.close(plt.gcf())   # reset rysunku

print("counter {}".format(counter))

# EOF
