# OUTERPLANAR GRAPHS

## RECOGNITION

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph

# TO DO
~~~

## GENERATORS

~~~python
from graphtheory.planarity.genouterplanar import MaximalOuterplanarGenerator

algorithm = MaximalOuterplanarGenerator(n)   # n is the number of vertices
algorithm.run()
algorithm.graph.show()   # random maximal outerplanar graph
~~~

## VERTEX COLORING

~~~python
from graphtheory.planarity.nodecolorouterplanar import OuterplanarNodeColoring

algorithm = OuterplanarNodeColoring(G)   # O(n) time
algorithm.run()
print( algorithm.color )   # dict
~~~

EOF
