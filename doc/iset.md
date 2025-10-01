# INDEPENDENT SETS

## EXACT ALGORITHMS FOR A MAXIMUM INDEPENDENT SET

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.independentsets.isetbt import BacktrackingIndependentSet

G = Graph()
# Add nodes and edges here.
algorithm = BacktrackingIndependentSet(G)
algorithm.run()
print( algorithm.independent_set )
print( algorithm.cardinality )
~~~

## HEURISTIC ALGORITHMS FOR A MAXIMUM INDEPENDENT SET

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.independentsets.isetus import UnorderedSequentialIndependentSet
from graphtheory.independentsets.isetrs import RandomSequentialIndependentSet
from graphtheory.independentsets.isetsf import SmallestFirstIndependentSet
from graphtheory.independentsets.isetll import LargestLastIndependentSet

G = Graph()
# Add nodes and edges here.
# algorithm = UnorderedSequentialIndependentSet(G)
# algorithm = RandomSequentialIndependentSet(G)
# algorithm = SmallestFirstIndependentSet(G)
algorithm = LargestLastIndependentSet(G)
algorithm.run()
print( algorithm.independent_set )
print( algorithm.cardinality )
~~~

## INDEPENDENT SETS IN SPECIAL GRAPHS

* [Forests](forest.md)
* [Series-parallel graphs](spgraph.md)
* [Chordal graphs](chordal.md)

EOF
