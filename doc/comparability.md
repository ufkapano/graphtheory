# COMPARABILITY GRAPHS

## RECOGNITION

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph

# TO DO
~~~

## CYCLE DETECTION FOR DIRECTED AND UNDIRECTED GRAPHS

~~~python
from graphtheory.algorithms.acyclic import AcyclicGraphDFS
from graphtheory.algorithms.acyclic import is_acyclic

# G is given.
assert is_acyclic(G)   # simple testing
algorithm = AcyclicGraphDFS(G)
algorithm.run()
print ( algorithm.parent )   # a DFS tree or a forest as a dict
~~~

## DAG (DIRECTED ACYCLIC GRAPH) DETECTION

~~~python
# G is given.
assert G.is_directed()
assert is_acyclic(G)
~~~

## TOPOLOGICAL SORTING FOR DAGS

~~~python
from graphtheory.algorithms.topsort import TopologicalSortQueue
from graphtheory.algorithms.topsort import TopologicalSortSet
from graphtheory.algorithms.topsort import TopologicalSortList
from graphtheory.algorithms.topsort import TopologicalSortDFS

# G is a DAG.
#algorithm = TopologicalSortQueue(G)
#algorithm = TopologicalSortSet(G)
#algorithm = TopologicalSortList(G)
algorithm = TopologicalSortDFS(G)
algorithm.run()
print ( algorithm.sorted_nodes )   # a sorted list of nodes
~~~

## TRANSITIVE CLOSURE

~~~python
from graphtheory.algorithms.closure import TransitiveClosureSimple
from graphtheory.algorithms.closure import TransitiveClosure
from graphtheory.algorithms.closure import TransitiveClosureBFS
from graphtheory.algorithms.closure import TransitiveClosureDFS

# A directed graph G is given.
#algorithm = TransitiveClosureSimple(G)
#algorithm = TransitiveClosureBFS(G)
#algorithm = TransitiveClosureDFS(G)
algorithm = TransitiveClosure(G)
algorithm.run()
print ( algorithm.T )   # solution matrix (bool)
~~~

EOF
