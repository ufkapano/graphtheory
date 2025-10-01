# DOMINATING SETS

## EXACT ALGORITHMS FOR A MINIMUM DOMINATING SET

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.dominatingsets.dsetbt import BacktrackingDominatingSet
from graphtheory.dominatingsets.dsethb import HybridDominatingSet

G = Graph()
# Add nodes and edges here.
#algorithm = BacktrackingDominatingSet(G)
algorithm = HybridDominatingSet(G)
algorithm.run()
print ( algorithm.dominating_set )
print ( algorithm.cardinality )
~~~

## HEURISTIC ALGORITHMS FOR A MINIMUM DOMINATING SET

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.dominatingsets.isetus import UnorderedSequentialDominatingSet
from graphtheory.dominatingsets.isetrs import RandomSequentialDominatingSet
from graphtheory.dominatingsets.isetll import LargestFirstDominatingSet

G = Graph()
# Add nodes and edges here.
# algorithm = UnorderedSequentialDominatingSet(G)
# algorithm = RandomSequentialDominatingSet(G)
algorithm = LargestFistDominatingSet(G)
algorithm.run()
print ( algorithm.dominating_set )
print ( algorithm.cardinality )
~~~

## DOMINATING SETS IN SPECIAL GRAPHS

* [Forests](forest.md)
* [Series-parallel graphs](spgraph.md)
* [Interval graphs](interval.md)

EOF
