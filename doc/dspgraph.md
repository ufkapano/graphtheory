# DIRECTED SERIES-PARALLEL GRAPHS (DSP-GRAPHS)

## RECOGNITION

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.seriesparallel.dsptrees import find_dsptree
from graphtheory.seriesparallel.spnodes import btree_print
from graphtheory.seriesparallel.spnodes import btree_print2

#   0    directed sp-graph
#  / \
# 1   3
#  \ /
#   2
#   |
#   4

N = 5   # the number of nodes
nodes = range(N)
# directed edges!
edges = [Edge(0, 1), Edge(0, 3), Edge(1, 2), Edge(3, 2), Edge(2, 4)]
G = Graph(n=N, directed=True)   # directed graph!
for node in nodes:
    G.add_node(node)
for edge in edges:
    G.add_edge(edge)

T = find_dsptree(G)
btree_print(T)
btree_print2(T)
~~~

## GENERATORS

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.seriesparallel.dsptools import make_random_dspgraph

G = make_random_dspgraph(n=10)   # returns a directed graph
~~~

EOF
