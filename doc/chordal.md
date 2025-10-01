# CHORDAL GRAPHS

## RECOGNITION

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.chordality.peotools import find_peo_lex_bfs
from graphtheory.chordality.peotools import find_peo_mcs
from graphtheory.chordality.peotools import find_maximum_clique_peo
from graphtheory.chordality.peotools import find_all_maximal_cliques
from graphtheory.chordality.peotools import is_peo1, is_peo2

#order = find_peo_lex_bfs(G)   # if G is not chordal, then 'order' is not a PEO
order = find_peo_mcs(G)   # if G is not chordal, then 'order' is not a PEO
assert is_peo1(G, order)   # testing PEO, O(n+m) time
assert is_peo2(G, order)   # testing PEO, O(n+m) time

max_clique = find_maximum_clique_peo(G, peo)   # G have to be chordal
print ( max_clique )   # a set of nodes
treewidth = len(max_clique) - 1

cliques = find_all_maximal_cliques(G, peo)   # G have to be chordal
print ( cliques )   # a list with sets
~~~

## GENERATORS

~~~python
from graphtheory.chordality.chordaltools import make_random_ktree
from graphtheory.chordality.chordaltools import make_random_chordal

G = make_random_ktree(n=10, k=5)   # PEO = range(n)
G = make_random_chordal(n=10)   # PEO = range(n)
~~~

## MAXIMUM INDEPENDENT SETS OF CHORDAL GRAPHS

~~~python
from graphtheory.chordality.peotools import find_maximum_independent_set

iset = find_maximum_independent_set(G, peo)   # G have to be chordal
print ( iset )   # a set of nodes
~~~

## MINIMUM DEGREE ORDERING (MDO) OF CHORDAL GRAPHS

~~~python
from graphtheory.chordality.mdotools import find_mdo
from graphtheory.chordality.mdotools import find_maximum_clique_mdo

order = find_mdo(G)   # O(n+m) time
print ( order )   # list of nodes (MDO)
max_clique = find_maximum_clique_mdo(G)   # O(n+m) time
print ( max_clique )   # a set of nodes
~~~

## TREE DECOMPOSITION (TD) OF CHORDAL GRAPHS

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.chordality.peotools import find_peo_mcs
from graphtheory.chordality.tdtools import find_td_chordal

G = make_random_chordal(n)   # G is a chordal graph
peo = find_peo_mcs(G)   # finding PEO
T = find_td_chordal(G, peo)   # finding a tree decomposition
assert isinstance(T, Graph)
bags = list(T.iternodes())   # a list of tuples
treewidth = max(len(bag) for bag in bags) - 1
~~~

## TREE DECOMPOSITION (TD) OF GENERAL GRAPHS

~~~python
from graphtheory.chordality.tdtools import find_td_order
from graphtheory.chordality.tdtools import find_treewidth_min_deg # upper bound
from graphtheory.chordality.tdtools import find_treewidth_mmd # lower bound

# G is a general connected undirected graph.
# 'order' is a selected sequence of nodes.

T = find_td_order(G, order)   # finding a tree decomposition (heuristic)
treewidth = max(len(bag) for bag in T.iternodes()) - 1 # upper bound

treewidth, order = find_treewidth_min_deg(G) # upper bound for treewidth

treewidth, order = find_treewidth_mmd(G) # lower bound for treewidth
~~~

## MCS-M ALGORITHM FOR MINIMAL TRIANGULATIONS

~~~python
from graphtheory.chordality.mcsm import MCS_M

# G is a general connected undirected graph.

algorithm = MCS_M(G)
algorithm.run()
algorithm.graph.show()   # chordal completion of G
print(algorithm.order)   # PEO of chordal completion
print(algorithm.new_edges)   # new edges added to G
~~~

## MINIMUM NODE COVER FOR CHORDAL GRAPHS

~~~python
from graphtheory.chordality.chordalcover import ChordalNodeCover

# G is a chordal graph, T is a tree decomposition of G
algorithm = ChordalNodeCover(G, T)
algorithm.run()
print(algorithm.cardinality)
print(algorithm.node_cover)
~~~

## MINIMUM DOMINATING SET FOF CHORDAL GRAPHS

~~~python
from graphtheory.chordality.chordaldset import ChordalDominatingSet

# G is a chordal graph, T is a tree decomposition of G
algorithm = ChordalDominatingSet(G, T)
algorithm.run()
print(algorithm.cardinality)
print(algorithm.dominating_set)
~~~

EOF
