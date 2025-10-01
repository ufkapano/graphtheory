# FLOW NETWORKS

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.flow.fordfulkerson import FordFulkerson
from graphtheory.flow.fordfulkerson import FordFulkersonSparse
from graphtheory.flow.fordfulkerson import FordFulkersonWithEdges
from graphtheory.flow.fordfulkerson import FordFulkersonRecursive
from graphtheory.flow.fordfulkerson import FordFulkersonRecursiveWithEdges
from graphtheory.flow.edmondskarp import EdmondsKarp
from graphtheory.flow.edmondskarp import EdmondsKarpSparse
from graphtheory.flow.dinic import Dinic
from graphtheory.flow.dinic import DinicSparse

N = 10   # the number of nodes
gf = GraphFactory(Graph)
G = gf.make_flow_network(n=N)
algorithm = FordFulkerson(G)
# algorithm = FordFulkersonSparse(G)
# algorithm = FordFulkersonWithEdges(G)
# algorithm = FordFulkersonRecursive(G)
# algorithm = FordFulkersonRecursiveWithEdges(G)
# algorithm = EdmondsKarp(G)
# algorithm = EdmondsKarpSparse(G)
# algorithm = Dinic(G)
# algorithm = DinicSparse(G)

# Finding the maximum flow from source to sink.
algorithm.run(source=0, sink=N-1)
print( algorithm.max_flow )   # the value of the maximum flow
print( algorithm.flow )       # a table with flows (dict of dict)
~~~

EOF
