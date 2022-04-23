#!/usr/bin/env python3
#
# Sprawdzam szybkosc wyznaczania matching.

import timeit
import random
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.seriesparallel.spnodes import Node
from graphtheory.seriesparallel.sptrees import make_random_sptree
from graphtheory.seriesparallel.spmate import SPTreeMatching
from graphtheory.seriesparallel.spnodes import btree_inorder
from graphtheory.seriesparallel.spnodes import btree_print

V = 10
root = make_random_sptree(V)
E = 0
for tnode in btree_inorder(root):
    if tnode.type == "edge":
        E += 1
#btree_print(root)

algorithm = SPTreeMatching(root)
algorithm.run()
print ( "mate_set {}".format( algorithm.mate_set ))
print ( "mate {}".format( algorithm.mate ))
print ( "cardinality {}".format( algorithm.cardinality ))

print ( "Testing SPTreeMatching ..." )
t1 = timeit.Timer(lambda: SPTreeMatching(root).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

# EOF
