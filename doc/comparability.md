# COMPARABILITY GRAPHS

## RECOGNITION

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph

# TO DO
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
