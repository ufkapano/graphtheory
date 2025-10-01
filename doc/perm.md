# PERMUTATION GRAPHS

## RECOGNITION

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph

# TO DO
~~~

## GENERATORS

~~~python
from graphtheory.permutations.permtools import make_random_perm
from graphtheory.permutations.permtools import make_star_perm
from graphtheory.permutations.permtools import make_bipartite_perm
from graphtheory.permutations.permtools import make_path_perm
from graphtheory.permutations.permtools import make_ladder_perm
from graphtheory.permutations.permtools import perm_has_edge
from graphtheory.permutations.permtools import make_complement_perm
from graphtheory.permutations.permtools import make_abstract_perm_graph

# perm has numbers from 0 to n-1.
n = 10
perm = make_random_perm(n)   # random perm graph
perm = make_star_perm(n)   # bipartite graph K_{1,n-1}
perm = make_bipartite_perm(p=3, q=4)   # bipartite graph K_{p,q}
perm = make_path_perm(n)   # path graph P_n
perm = make_ladder_perm(n)   # ladder graph (bipartite)
assert isinstance(perm, list)
assert len(perm) == n
assert sorted(perm) == list(range(n))
assert perm_has_edge(perm, 1, 2)   # O(n) time
perm2 = make_complement_perm(perm)   # O(n) time
assert not perm_has_edge(perm2, 1, 2)

# Create an abstract perm graph.
G = make_abstract_perm_graph(perm)
assert isinstance(G, Graph)
~~~

## CONNECTIVITY

~~~python
from graphtheory.permutations.permtools import perm_is_connected
from graphtheory.permutations.permtools import perm_connected_components
from graphtheory.permutations.permtools import make_abstract_perm_graph

assert perm_is_connected([3, 2, 1, 0])   # K_4 is connected
assert not perm_is_connected([1, 0, 3, 2])   # P_2+P_2 is not connected

n_cc, cc = perm_connected_components([1, 0, 3, 2])
assert n_cc == 2
assert cc == {1: 0, 0: 0, 3: 1, 2: 1}

perm = [4, 3, 2, 1, 0]   # K_5
graph = make_abstract_perm_graph(perm)
assert isinstance(graph, Graph)
assert graph.v() == 5   # K_5
assert graph.e() == 10   # K_5
~~~

## TRAVERSING

~~~python
from graphtheory.permutations.permbfs import PermBFS
from graphtheory.permutations.permdfs import PermDFS

# Using BFS/DFS in O(n^2) time.
perm = [...]   # perm graph as a list
source = ...   # starting node
pre_order = []
post_order = []
algorithm = PermBFS(perm)
#algorithm = PermDFS(perm)
algorithm.run(source,
    pre_action=lambda node: pre_order.append(node),
    post_action=lambda node: post_order.append(node))

# Results.
print( pre_order )   # node list
print( post_order )   # node list
print( algorithm.parent )   # BFS/DFS tree as a dict
print( algorithm.path(source, target) )   # node list
~~~

## FINDING A CHORDAL COMPLETION FOR PERMUTATION GRAPHS IN O(n^4) TIME

~~~python
from graphtheory.permutations.permpeo import PermGraphPEO
from graphtheory.chordality.peotools import is_peo1

n = 10
perm = make_bipartite_perm(n // 2, n-(n // 2))   # exemplary perm graph
assert len(perm) == n
algorithm = PermGraphPEO(perm)
algorithm.run()

# Results.
algorithm.graph.show()   # chordal completion
assert isinstance(algorithm.graph, Graph)
print( algorithm.order )   # PEO for chordal completion
assert isinstance(algorithm.order, list)
assert len(algorithm.order) == n
print( algorithm.new_edges )   # new edges added to the perm graph
assert is_peo1(algorithm.graph, algorithm.order)
~~~

EOF
