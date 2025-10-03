# MATCHINGS

## MATCHINGS FOR GENERAL GRAPHS (HEURISTICS)

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

## MATCHINGS FOR BIPARTITE GRAPHS

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.bipartiteness.matching import MatchingFordFulkersonSet
from graphtheory.bipartiteness.matching import MatchingFordFulkersonList
from graphtheory.bipartiteness.matching import MatchingFordFulkersonColor
from graphtheory.bipartiteness.hopcroftkarp import HopcroftKarpSet
from graphtheory.bipartiteness.hopcroftkarp import HopcroftKarpList

V = 10
graph_factory = GraphFactory(Graph)
G = graph_factory.make_bipartite(V // 2, V // 2, False, 0.5)   # random bipartite
#G = graph_factory.make_tree(V, False)   # trees are bipartite

algorithm = MatchingFordFulkersonSet(G)
# algorithm = MatchingFordFulkersonList(G)
# algorithm = MatchingFordFulkersonColor(G)
# algorithm = HopcroftKarpSet(G)
# algorithm = HopcroftKarpList(G)
algorithm.run()
print( algorithm.mate )   # a dict with pairs (source, target or None)
print( algorithm.cardinality )  # the size of max matching
~~~

EOF
