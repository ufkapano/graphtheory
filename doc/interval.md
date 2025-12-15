# INTERVAL GRAPHS

## RECOGNITION

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph

# TO DO
~~~

## GENERATORS

~~~python
from graphtheory.chordality.intervaltools import make_random_interval
from graphtheory.chordality.intervaltools import make_complete_interval
from graphtheory.chordality.intervaltools import make_path_interval
from graphtheory.chordality.intervaltools import make_tepee_interval
from graphtheory.chordality.intervaltools import make_2tree_interval
from graphtheory.chordality.intervaltools import make_star_interval
from graphtheory.chordality.intervaltools import make_ktree_interval
from graphtheory.chordality.intervaltools import make_abstract_interval_graph

# Generators return an interval graph as a double perm.
n = 10
perm = make_random_interval(n)   # random interval graph
perm = make_complete_interval(n)   # K_n graph
perm = make_path_interval(n)   # P_n graph
perm = make_tepee_interval(n)   # tepee graph
# 0---5---4   make_tepee_interval(6)
# | / | \ |
# 1---2---3
perm = make_2tree_interval(n)   # interval 2-tree graph
# 0---2---4   make_2tree_interval(6)
# | / | / |
# 1---3---5
perm = make_star_interval(n)   # K_{1,n-1} graph
perm = make_ktree_interval(n, k=n // 2)   # interval k-tree
assert isinstance(perm, list)
assert len(perm) == 2*n

# Create an abstract interval graph in O(n+m) time.
G = make_abstract_interval_graph(perm)
assert isinstance(G, Graph)
~~~

## CONNECTIVITY

~~~python
from graphtheory.chordality.intervaltools import interval_is_connected
from graphtheory.chordality.intervaltools import interval_has_edge
from graphtheory.chordality.intervaltools import find_edges_interval

# Testing connectivity in O(n) time.
assert interval_is_connected([0,1,0,1])   # P_2
assert interval_is_connected([0,1,2,0,1,2])   # K_3
assert not interval_is_connected([0,0,1,1])   # P_1 + P_1
assert interval_has_edge([1,2,3,1,4,2,3,4], 1, 3)   # diamond
assert not interval_has_edge([1,2,3,1,4,2,3,4], 1, 4)   # diamond

# Finding the number of edges from a double perm in O(n^2) time.
assert find_edges_interval([0,1,2,0,1,2]) == 3   # K_3
assert find_edges_interval([1,2,3,1,4,2,3,4]) == 5   # diamond
~~~

## CLIQUES AND PEO

~~~python
from graphtheory.chordality.intervaltools import find_peo_cliques
from graphtheory.chordality.intervaltools import find_max_clique_size
from graphtheory.chordality.intervaltools import iter_cliques_interval

#   1
#  / \
# 2---3---4
perm = [1,2,3,1,2,4,3,4]   # stop
peo, cliques = find_peo_cliques(perm)   # O(n+m) time
assert peo == [1, 2, 3, 4]
assert cliques == [{1, 2, 3}, {3, 4}]   # ordered cliques
assert find_max_clique_size(perm) == 3   # O(n) time
for clique in iter_cliques_interval(perm):   # clique iterator, O(n+m) time
    print(clique)

# Let weight_dict be a dict with node weights.
# Finding a maximum weight clique in O(n+m) time:
max_weight_clique = max(iter_cliques_interval(perm),
    key=lambda clique: sum(weight_dict[v] for v in clique))
~~~

## VERTEX COLORING

~~~python
from graphtheory.chordality.intervaltools import interval_node_color

# Vertex coloring in O(n) time.
n = 5
perm = list(range(n)) * 2   # K_n graph
color = interval_node_color(perm)
print(color)   # {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}, n colors

perm = make_path_interval(n)
color = interval_node_color(perm)
print(color)   # {0: 0, 1: 1, 2: 0, 3: 1, 4: 0}, 2 colors
~~~

## MAXIMUM INDEPENDENT SET

~~~python
from graphtheory.chordality.intervaltools import interval_maximum_iset

n = 10
perm = list(range(n)) * 2   # K_n graph
iset = interval_maximum_iset(perm)
assert len(iset) == 1

perm = make_path_interval(n)   # P_n graph
iset = interval_maximum_iset(perm)
assert len(iset) == (n+1) // 2

perm = make_tepee_interval(n)
iset = interval_maximum_iset(perm)
assert len(iset) == n // 2

perm = make_2tree_interval(n)
iset = interval_maximum_iset(perm)
assert len(iset) == (n+2) // 3

perm = make_star_interval(n)   # K_{1,n-1} star graph
iset = interval_maximum_iset(perm)
assert len(iset) == n-1
~~~

## MINIMUM DOMINATING SET

~~~python
from graphtheory.chordality.intervaldset import IntervalDominatingSet

# [2013 Chang] Primal-dual algorithm, O(n+m) time.
# perm is a double perm for an interval graph.
algorithm = IntervalDominatingSet(perm)
algorithm.run()
print(algorithm.dominating_set)
assert algorithm.cardinality == len(algorithm.dominating_set)
print(algorithm.two_stable_set)
~~~

## TRAVERSING (BFS)

~~~python
from graphtheory.chordality.intervalbfs import IntervalBFS

# 0---4---3   2-tree graph (tepee)
# | \ | /
# 2---1
#
# 2-----2
#   0-------0
#     1-------------1
#         4-----4
#             3---3

perm = [2,0,1,2,4,0,3,4,3,1]
preorder = []
postorder = []
algorithm = IntervalBFS(perm)
algorithm.run(0, pre_action=lambda node: preorder.append(node),
                post_action=lambda node: postorder.append(node))
print(preorder)   # [0, 1, 2, 4, 3]
print(postorder)   # [0, 1, 2, 4, 3]
print(algorithm.parent)   # {0: None, 1: 0, 2: 0, 3: 1, 4: 0}
print(algorithm.path(0, 3))    # [0, 1, 3]
print(algorithm.path(0, 1))   # [0, 1]
~~~

## TRAVERSING (DFS)

~~~python
from graphtheory.chordality.intervaldfs import IntervalDFS

# 0---4---3   2-tree graph (tepee)
# | \ | /
# 2---1
#
# 2-----2
#   0-------0
#     1-------------1
#         4-----4
#             3---3

perm = [2,0,1,2,4,0,3,4,3,1]   # interval graph as double perm
preorder = []
postorder = []
algorithm = IntervalDFS(perm)
algorithm.run(0, pre_action=lambda node: preorder.append(node),
                post_action=lambda node: postorder.append(node))
print(preorder)   # [0, 1, 2, 3, 4]
print(postorder)   # [2, 4, 3, 1, 0]
print(algorithm.parent)   # {0: None, 1: 0, 2: 1, 3: 1, 4: 3}
print(algorithm.path(0, 1))   # [0, 1]
print(algorithm.path(0, 3))   # [0, 1, 3]
~~~

## DRAWING INTERVAL GRAPHS

~~~python
from graphtheory.chordality.intervaltools import make_random_interval
from graphtheory.chordality.intervaltools import interval_drawing

n = 10   # the number of vertices
perm = make_random_interval(n)
print(perm)
interval_drawing(perm)
# [4, 3, 6, 1, 9, 9, 4, 0, 5, 8, 7, 8, 3, 7, 0, 6, 2, 1, 2, 5]
# 4-----------4 0-------------0   2---2   
#   3---------------------3               
#     6-------------------------6         
#       1---------------------------1     
#         9-9     5---------------------5 
#                   8---8                 
#                     7-----7
~~~

EOF
