#!/usr/bin/env python3

import timeit
from graphtheory.permutations.circletools import make_cycle_circle
from graphtheory.permutations.circletools import is_perm_graph

N = 1000
# Biore graf C_n, bo to nie jest graf permutacji dla n > 4
# i algorytm dziala do konca.
perm = make_cycle_circle(N) # not a perm graph

print ( "Testing is perm_graph ..." )
t1 = timeit.Timer(lambda: is_perm_graph(perm))
print ( "{} {}".format(N, t1.timeit(1)) )   # single run

# EOF
