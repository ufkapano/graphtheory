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

G = Graph()   # an undirected graph
# Add nodes and edges here.

algorithm = BronKerboschClassic(G)
#algorithm = BronKerboschRandomPivot(G)
#algorithm = BronKerboschDegreePivot(G)
#algorithm = BronKerboschDegeneracy(G)
algoritm.run()
print( algoritm.cliques )   # a list of maximal cliques
~~~

EOF


