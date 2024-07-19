#!/usr/bin/env python3

from graphtheory.chordality.peotools import is_peo1
from graphtheory.chordality.tdtools import find_td_chordal
from graphtheory.permutations.permtools import make_bipartite_perm
from graphtheory.permutations.permtools import make_star_perm
from graphtheory.permutations.permtools import make_path_perm
from graphtheory.permutations.permpeo import PermGraphPEO

#perm = (4,3,2,1,0)   # K_5, perm is chordal
# Non-chordal perm graphs with n=5.
#perm = (2,4,0,3,1)   # house, 1 cykl (2,0,4,1), dwie cieciwy, new_edges [(0,1)]
#perm = (2,4,0,1,3)   # kwadrat z lisciem, new_edges [(0,1)]
#perm = (3,4,0,2,1)   # 2 cykle, new_edges [(3,4)]
#perm = (3,4,0,1,2)   # 3 cykle, jedna krawedz wystarczy, new_edges [(3,4)]
#perm = (3,4,1,2,0)   # 1 cykl, new_edges [(1,2)]

#perm = (3,4,5,0,1,2)   # K_{3,3}, jest 9 cykli C_4, new_edges [(0,1),(1,2),(0,2)]
#perm = (4,5,2,3,0,1)   # sa 3 cykle C_4, planar, 4-regular
#perm = (2,4,0,5,1,3)   # figure-8, 2 cykle C_4
#perm = (2,4,0,6,1,7,3,5)   # ladder, 3 cykle C_4
#perm = (2,4,0,6,1,8,3,9,5,7)   # ladder, 4 cykle C_4
perm = make_bipartite_perm(p=5, q=5)   # make perm for K_{p,q} graph
#perm = make_star_perm(n=10)
#perm = make_path_perm(n=10)

algorithm = PermGraphPEO(perm)
algorithm.run()
assert is_peo1(algorithm.graph, algorithm.order)   # testing PEO
print("new_edges", algorithm.new_edges)
print("order", algorithm.order)

T = find_td_chordal(algorithm.graph, algorithm.order)   # finding TD
assert T.v() == T.e() + 1   # tree
treewidth = max(len(bag) for bag in T.iternodes()) - 1
print("treewidth", treewidth)

# EOF
