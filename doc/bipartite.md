# BIPARTITE GRAPHS

## RECOGNITION

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.bipartiteness.bipartite import BipartiteGraphBFS
from graphtheory.bipartiteness.bipartite import BipartiteGraphDFS
from graphtheory.bipartiteness.bipartite import is_bipartite
from graphtheory.structures.factory import GraphFactory

# Creating bipartite graphs.
N = 10
gf = GraphFactory(Graph)
G = gf.make_bipartite(n1=N, n2=N, directed=False, edge_probability=0.1)
#G = gf.make_tree(n=N)   # trees are bipartite
#G = gf.make_ladder(size=N)
assert is_bipartite(G)

algorithm = BipartiteGraphBFS(G)   # recognition and coloring
#algorithm = BipartiteGraphDFS(G)   # recognition and coloring
algorithm.run()
print( algorithm.color )
~~~

## MATCHINGS IN BIPARTITE GRAPHS

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.bipartiteness.matchingff import MatchingFordFulkersonSet
from graphtheory.bipartiteness.matchingff import MatchingFordFulkersonList
from graphtheory.bipartiteness.matchingff import MatchingFordFulkersonColor
from graphtheory.bipartiteness.matchingap import MatchingUsingAugmentingPath
from graphtheory.bipartiteness.hopcroftkarp import HopcroftKarpSet
from graphtheory.bipartiteness.hopcroftkarp import HopcroftKarpList

N = 10
graph_factory = GraphFactory(Graph)
G = graph_factory.make_bipartite(n1=N // 2, n2=N // 2, False, 0.5)   # random bipartite
#G = graph_factory.make_tree(n=N, False)   # trees are bipartite

algorithm = MatchingFordFulkersonSet(G)
# algorithm = MatchingFordFulkersonList(G)
# algorithm = MatchingFordFulkersonColor(G)
# algorithm = MatchingUsingAugmentingPath(G)   # O(nm) time
# algorithm = HopcroftKarpSet(G)   # O(m sqrt(n)) time
# algorithm = HopcroftKarpList(G)   # O(m sqrt(n)) time
algorithm.run()
print( algorithm.mate )   # a dict with pairs (source, target or None)
print( algorithm.cardinality )  # the size of max matching
~~~

## INDEPENDENT SETS IN BIPARTITE GRAPHS

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.bipartiteness.bipartiteiset import BipartiteIndependentSet

G = Graph()
# Add nodes and edges here and create a bipartite graph.
algorithm = BipartiteIndependentSet(G)
algorithm.run()   # O(m sqrt(n)) time
print( algorithm.independent_set )   # a maximum independent set
print( algorithm.cardinality )   # the size of a maximum independent set
~~~

EOF
