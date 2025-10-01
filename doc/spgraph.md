# UNDIRECTED SERIES-PARALLEL GRAPHS (SP-GRAPHS)

## RECOGNITION

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.seriesparallel.sptrees import find_sptree
from graphtheory.seriesparallel.spnodes import btree_print
from graphtheory.seriesparallel.spnodes import btree_print2

graph_factory = GraphFactory(Graph)
G = graph_factory.make_cyclic(n=5)   # n > 2
# a cycle graph is an sp-graph

#T = find_sptree(G)
T = find_sptree(G, fixed_ends=(1, 3))   # using fixed ends
btree_print(T)
btree_print2(T)
~~~

## GENERATORS

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.seriesparallel.sptools import make_random_ktree
from graphtheory.seriesparallel.sptools import make_random_spgraph

G = make_random_spgraph(n=10)
#G = make_random_ktree(n=10, k=2)
~~~

## PERFECT ELIMINATION ORDERING (treewidth = 2)

~~~python
from graphtheory.seriesparallel.sptools import find_peo_spgraph

peo = find_peo_spgraph(G)     # list
print ( peo )
~~~

## MAXIMUM INDEPENDENT SET

~~~python
from graphtheory.seriesparallel.spiset import SPGraphIndependentSet
from graphtheory.seriesparallel.spiset import SPTreeIndependentSet

algorithm = SPGraphIndependentSet(G, T)
algorithm.run()
print ( algorithm.independent_set )

algorithm = SPTreeIndependentSet(T)
algorithm.run()
print ( algorithm.independent_set )
~~~

## MINIMUM DOMINATING SET

~~~python
from graphtheory.seriesparallel.spdset import SPGraphDominatingSet
from graphtheory.seriesparallel.spdset import SPTreeDominatingSet

algorithm = SPGraphDominatingSet(G, T)
algorithm.run()
print ( algorithm.dominating_set )

algorithm = SPTreeDominatingSet(T)
algorithm.run()
print ( algorithm.dominating_set )
~~~

## MINIMUM VERTEX COVER

~~~python
from graphtheory.seriesparallel.spcover import SPGraphNodeCover
from graphtheory.seriesparallel.spcover import SPTreeNodeCover

algorithm = SPGraphNodeCover(G, T)
algorithm.run()
print ( algorithm.node_cover )

algorithm = SPTreeNodeCover(T)
algorithm.run()
print ( algorithm.node_cover )
~~~

## MAXIMUM MATCHING

~~~python
from graphtheory.seriesparallel.spmate import SPGraphMatching
from graphtheory.seriesparallel.spmate import SPTreeMatching

algorithm = SPGraphMatching(G, T)
algorithm.run()
print ( algorithm.mate_set )   # a set of edges
print ( algorithm.mate )       # dict

algorithm = SPTreeMatching(T)
algorithm.run()
print ( algorithm.mate_set )   # a set of edges
print ( algorithm.mate )       # dict
~~~

## VERTEX COLORING

~~~python
from graphtheory.seriesparallel.spnodecolor import SPNodeColoring

algorithm = SPNodeColoring(G)
algorithm.run()
print ( algorithm.color )   # dict
~~~

EOF
