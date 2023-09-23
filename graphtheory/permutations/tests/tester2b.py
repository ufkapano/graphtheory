#!/usr/bin/env python3

import itertools
import networkx as nx
import matplotlib.pyplot as plt
from graphtheory.permutations.circletools import circle_is_connected
from graphtheory.permutations.circletools import make_abstract_circle_graph
from graphtheory.permutations.circletools import is_perm_graph
from graphtheory.chordality.peotools import find_peo_lex_bfs
from graphtheory.chordality.peotools import is_peo1, is_peo2

n = 5
letters = "abcdefghijklmnopqrstuvwxyz"
word = [letters[i // 2] for i in range(2*n)]
# Chce wykorzystac symetrie wzgledem cyklicznej rotacji 
# i ustawiam ostatni znak zawsze na koncu.
# Beda powtorzenia zwiazane ze zmiana kierunku obchodzenia okregu.
last = word.pop()
perm_set = set()   # double perms
counter = 0

for perm in itertools.permutations(word):
    perm = perm + (last,)
    if perm in perm_set:
        continue
    else:
        perm_set.add(perm)
    if not circle_is_connected(perm):
        continue
    if is_perm_graph(perm):
        continue
    graph = make_abstract_circle_graph(perm)
    order = find_peo_lex_bfs(graph)
    if is_peo1(graph, order):   # pomijamy chordal graphs
        continue
    print(perm)
    print("V E {} {}".format(graph.v(), graph.e()))
    #graph.show()
    counter += 1

    filename = "".join(perm) + ".png"
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
