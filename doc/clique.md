# CLIQUES

## CLIQUE TOOLS

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph

~~~

## THE BRON-KERBOSCH ALGORITHM

~~~python
from graphtheory.cliques.bronkerbosch import BronKerboschClassic
from graphtheory.cliques.bronkerboschrp import BronKerboschRandomPivot
from graphtheory.cliques.bronkerboschdp import BronKerboschDegreePivot
from graphtheory.cliques.bronkerboschdeg import BronKerboschDegeneracy

from graphtheory.cliques.bronkerbosch2 import BronKerboschClassicIterator
from graphtheory.cliques.bronkerboschrp2 import BronKerboschRandomPivotIterator
from graphtheory.cliques.bronkerboschdp2 import BronKerboschDegreePivotIterator
from graphtheory.cliques.bronkerboschdeg2 import BronKerboschDegeneracyIterator

G = Graph()   # an undirected graph
# Add nodes and edges here.

algorithm = BronKerboschClassic(G)
#algorithm = BronKerboschRandomPivot(G)
#algorithm = BronKerboschDegreePivot(G)
#algorithm = BronKerboschDegeneracy(G)   # finding MDO in O(n^2) time
# MDO = Minimum Degree Ordering
algorithm.run()
print( algorithm.cliques )   # a list of maximal cliques

algorithm = BronKerboschClassicIterator(G)
#algorithm = BronKerboschRandomPivotIterator(G)
#algorithm = BronKerboschDegreePivotIterator(G)
#algorithm = BronKerboschDegeneracyIterator(G)   # using find_mdo(G) in O(n+m) time
clique_iterator = algorithm.run()
print( list(clique_iterator) )   # a list of maximal cliques
~~~

## BIPARTITE GRAPHS

~~~python
# G is a bipartite graph.
# All maximum cliqes are edges.
# Let weight_dict be a dict with node weights.

max_weight_edge = max(G.iteredges(), key=lambda edge:
    weight_dict[edge.source] + weight_dict[edge.target])

max_weight_clique = {max_weight_edge.source, max_weight_edge.target}
~~~

EOF


