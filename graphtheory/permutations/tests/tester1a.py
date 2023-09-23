#!/usr/bin/env python3
#
# Generating all perm graphs.
# Counting connected perms.
# Counting connected nonchordal perms.

import itertools
from graphtheory.permutations.permtools import perm_is_connected
from graphtheory.permutations.permtools import make_abstract_perm_graph
from graphtheory.chordality.peotools import find_peo_lex_bfs
from graphtheory.chordality.peotools import is_peo1, is_peo2

n = 5
counter = 0
for perm in itertools.permutations(range(n)):
    if not perm_is_connected(perm):   # pomijamy grafy niespojne
        continue
    graph = make_abstract_perm_graph(perm)
    order = find_peo_lex_bfs(graph)
    if is_peo1(graph, order):   # pomijamy chordal graphs
        continue
    print(perm)
    #graph.show()
    counter += 1

print("counter {}".format(counter))

# EOF
