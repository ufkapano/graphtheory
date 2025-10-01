# VERTEX COVERS

## HEURISTIC ALGORITHMS FOR A MINIMUM VERTEX COVER

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.vertexcovers.nodecoverapp import ApproximationNodeCover
from graphtheory.vertexcovers.nodecoverdeg import DegreeNodeCover
from graphtheory.vertexcovers.nodecoverlf import LargestFirstNodeCover

G = Graph()
# Add nodes and edges here.
#algorithm = ApproximationNodeCover(G)   # 2-approximation
#algorithm = DegreeNodeCover   # greedy
algorithm = LargestFirstNodeCover   # greedy
algorithm.run()
print( algorithm.node_cover )   # a set with nodes
print( algorithm.cardinality )
~~~

## VERTEX COVERS IN SPECIAL GRAPHS

* [Forests](forest.md)
* [Series-parallel graphs](spgraph.md)

EOF
