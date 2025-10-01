# CONNECTIVITY

## UNDIRECTED GRAPHS

~~~python
from graphtheory.connectivity.connected import ConnectedComponentsBFS
from graphtheory.connectivity.connected import ConnectedComponentsDFS
from graphtheory.connectivity.connected import is_connected
from graphtheory.connectivity.cutedges import TrivialCutEdge
from graphtheory.connectivity.cutedges import TarjanCutEdge
from graphtheory.connectivity.cutnodes import TrivialCutNode
from graphtheory.connectivity.cutnodes import TarjanCutNode
from graphtheory.connectivity.cutnodes import is_biconnected

# G is an undirected graph.
algorithm = ConnectedComponentsBFS(G)
#algorithm = ConnectedComponentsDFS(G)
algorithm.run()
print ( algorithm.n_cc )   # the number of connected components
print ( algorithm.cc )   # a dict with pairs (node, component_number)

assert is_connected(G)   # simple testing
assert is_biconnected(G)   # simple testing

# Finding cut edges.
#algorithm = TrivialCutEdge(G)
algorithm = TarjanCutEdge(G)
algorithm.run()
print ( algorithm.cut_edges )   # a list of cut edges

# Finding cut nodes.
#algorithm = TrivialCutNode(G)
algorithm = TarjanCutNode(G)
algorithm.run()
print ( algorithm.cut_nodes )   # a list of cut nodes
~~~

## DIRECTED GRAPHS

~~~python
from graphtheory.connectivity.connected import StronglyConnectedComponents

# G is a directed graph.
algorithm = StronglyConnectedComponents(G)
algorithm.run()
print ( algorithm.n_cc )   # the number of strongly connected components
print ( algorithm.cc )   # a dict with pairs (node, component_number)
~~~

EOF
