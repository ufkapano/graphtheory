# MINIMUM SPANNING TREES

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph

from graphtheory.spanningtrees.boruvka import BoruvkaMST
from graphtheory.spanningtrees.prim import PrimMST
from graphtheory.spanningtrees.prim import PrimMSTWithEdges
from graphtheory.spanningtrees.prim import PrimMatrixMST
from graphtheory.spanningtrees.prim import PrimMatrixMSTWithEdges
from graphtheory.spanningtrees.prim import PrimConnectedMST
from graphtheory.spanningtrees.prim import PrimTrivialMST
from graphtheory.spanningtrees.kruskal import KruskalMST
from graphtheory.spanningtrees.kruskal import KruskalMSTSorted

G = Graph()
# Add nodes and edges here.
algorithm = BoruvkaMST(G)
# algorithm = PrimMST(G)
# algorithm = PrimMSTWithEdges(G)
# algorithm = PrimMatrixMST(G)
# algorithm = PrimMatrixMSTWithEdges(G)
# algorithm = PrimConnectedMST(G)
# algorithm = PrimTrivialMST(G)
# algorithm = KruskalMST(G)
# algorithm = KruskalMSTSorted(G)
algorithm.run()
# algorithm.run(source)   # starting node can be provided
algorithm.mst.show()         # MST as a graph
print( algorithm.parent )   # MST as a dict
print( algorithm.distance )
T = algorithm.to_tree()   # MST as a graph (it works for all algorithms)
T.show()
~~~

EOF
