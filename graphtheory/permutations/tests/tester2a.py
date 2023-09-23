#!/usr/bin/env python3
#
# Generating all circle graphs.
# Counting connected circle graphs.
# Counting connected circle graphs and not perm graphs.
# Sprawdzanie postaci circle graphs, ktore nie sa perm graphs.

import itertools
from graphtheory.permutations.circletools import circle_is_connected
from graphtheory.permutations.circletools import make_abstract_circle_graph
from graphtheory.permutations.circletools import is_perm_graph
from graphtheory.chordality.peotools import find_peo_lex_bfs
from graphtheory.chordality.peotools import is_peo1, is_peo2

n = 5
letters = "abcdefghijklmnopqrstuvwxyz"
word = [letters[i // 2] for i in range(2*n)]   # double perm
# Chce wykorzystac symetrie wzgledem cyklicznej rotacji 
# i ustawiam ostatni znak zawsze na koncu.
# Beda powtorzenia zwiazane ze zmiana kierunku obchodzenia okregu.
last = word.pop()
perm_set = set()   # for unique double perms
counter = 0

for perm in itertools.permutations(word):   # (2n-1)-(double perms)
    perm = perm + (last,)   # 2n-(double perm)
    if perm in perm_set:   # discard repetitions
        continue
    else:
        perm_set.add(perm)
    if not circle_is_connected(perm):   # pomijamy grafy niespojne
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

print("counter {}".format(counter))

# EOF
