# MATCHINGS

## MATCHINGS IN GENERAL GRAPHS (HEURISTICS)

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.algorithms.matching import MaximalMatching
from graphtheory.algorithms.matching import MaximalMatchingWithEdges
from graphtheory.algorithms.matching import MinimumWeightMatchingWithEdges

G = Graph()
# Add nodes and edges here.
algorithm = MaximalMatching(G)   # O(n+m) time
# algorithm = MaximalMatchingWithEdges(G)   # O(n+m) time
# algorithm = MinimumWeightMatchingWithEdges(G)   # O(m log n) time
algorithm.run()
print( algorithm.mate )   # a dict with pairs (source, target or None)
#print( algorithm.mate )   # a dict with pairs (source, edge or None) '...WithEdges'
print( algorithm.cardinality )  # the size of max matching
~~~

## MATCHINGS IN SPECIAL GRAPHS

* [Forests](forest.md)
* [Bipartite graphs](bipartite.md)

EOF
