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
G = gf.make_bipartite(N, N, directed=False, edge_probability=0.1)
#G = gf.make_tree(n=N)   # trees are bipartite
#G = gf.make_ladder(size=N)
assert is_bipartite(G)

algorithm = BipartiteGraphBFS(G)   # recognition and coloring
#algorithm = BipartiteGraphDFS(G)   # recognition and coloring
algorithm.run()
print( algorithm.color )
~~~

## MATCHINGS IN BIPARTITE GRAPHS

* [Matchings](matching.md)

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
