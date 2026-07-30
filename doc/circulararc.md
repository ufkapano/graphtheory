# CIRCULAR-ARC GRAPHS

## REPRESENTATION

~~~python
#   1       stop sign graph
#  / \
# 3---2---0
# pairs of events (integers)
# reprB = [(5,7), (0,3), (2,6), (1,4)]
#
# arcs      cliques (interval graph)
# +-------+ +-------+-------+
# |0 1 2 3| | Helly |0 1 2 3|
# +-------+ +-------+-------+
# |. 1 . .| |{1,2,3}|0 1 1 1|
# |. 1 . 3| |{0,2}  |1 0 1 0|
# |. 1 2 3| +-------+-------+
# |. . 2 3|
# |. . 2 .|
# |0 . 2 .|
# |0 . . .|
# |. . . .|
# +-------+
~~~

## RECOGNITION

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph

# TO DO
~~~

## GENERATORS

~~~python
from graphtheory.chordality.arctools import make_random_arc
from graphtheory.chordality.arctools import make_cycle_arc
from graphtheory.chordality.arctools import make_complete_arc

n = 10   # the number of arcs
reprB = make_random_arc(n)
reprB = make_cycle_arc(n)
reprB = make_complete_arc(n)
assert len(reprB) == n   # n 2-tuples
assert repr[0][0] == 0   # a canonical form from [1988 Masuda Nakajima]
assert repr[0][0] < repr[0][1]   # a forward arc first [1988 Masuda Nakajima]
~~~

## FUNCTIONS

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.chordality.arctools import make_abstract_arc_graph

G = make_abstract_arc_graph(reprB)
assert G.v() == len(reprB)   # the number of arcs
~~~

EOF
