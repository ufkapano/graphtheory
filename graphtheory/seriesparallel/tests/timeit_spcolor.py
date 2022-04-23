#!/usr/bin/env python3
#
# Sprawdzam szybkosc kolorowania wierzcholkow sp-grafu.
# Wydaje sie, ze grafy dwudzielne trafiaja sie bardzo rzadko.

import timeit
import random
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.seriesparallel.spnodes import Node
from graphtheory.seriesparallel.spnodecolor import SPNodeColoring
from graphtheory.seriesparallel.sptools import make_random_spgraph
from graphtheory.seriesparallel.sptools import make_random_ktree

V = 10
G = make_random_spgraph(V)
#G = make_random_ktree(V, 2)
E = G.e()
#G.show()

algorithm = SPNodeColoring(G)
algorithm.run()
all_colors = set(algorithm.color[node] for node in G.iternodes())
assert len(all_colors) == 3

print ( "Testing SPNodeColoring ..." )
t1 = timeit.Timer(lambda: SPNodeColoring(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

# EOF
