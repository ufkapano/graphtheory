# ASTEROIDAL TRIPLE-FREE GRAPHS (AT-FREE GRAPHS)

## RECOGNITION IN O(n^4) TIME

~~~python
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.asteroidal.atfree import ATFreeGraph

gf = GraphFactory(Graph)

# Exemplary AT-free graphs.
G = gf.make_cyclic(n=4)   # undirected cyclic graph C_4
#G = gf.make_cyclic(n=5)   # undirected cyclic graph C_5
#G = gf.make_prism(size=3)

algorithm = ATFreeGraph(G)
algorithm.run()
assert algorithm.is_at_free()

# Exemplary graphs with AT.
G = gf.make_cyclic(n=6)   # undirected cyclic graph C_6

algorithm = ATFreeGraph(G)
algorithm.run()
assert not algorithm.is_at_free()
~~~

## MAXIMUM INDEPENDENT SETS IN O(n^4) TIME

### Finding the independence number.

~~~python
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.asteroidal.atfreeiset1 import ATFreeIndependentSet

gf = GraphFactory(Graph)
G = gf.make_cyclic(n=4)   # undirected cyclic graph C_4
algorithm = ATFreeIndependentSet(G)
algorithm.run()
assert algorithm.cardinality == 2
~~~

### Finding a maximum independent set.

~~~python
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.asteroidal.atfreeiset2 import ATFreeIndependentSet

gf = GraphFactory(Graph)
G = gf.make_cyclic(n=4)   # undirected cyclic graph C_4
algorithm = ATFreeIndependentSet(G)
algorithm.run()
assert algorithm.independent_set in [{0, 2}, {1, 3}]
assert algorithm.cardinality == 2
~~~

## MINIMUM DOMINATING SETS

~~~python
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.asteroidal.atfreedset import ATFreeDominatingSet

gf = GraphFactory(Graph)
G = gf.make_path(n=6)   # undirected path graph P_6   0--1--2--3--4--5
algorithm = ATFreeDominatingSet(G)
algorithm.run()
assert algorithm.dominating_set == {1, 4}
assert algorithm.cardinality == 2
~~~

EOF
