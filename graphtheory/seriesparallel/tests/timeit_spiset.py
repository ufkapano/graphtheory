#!/usr/bin/env python3
#
# Sprawdzam szybkosc wyznaczania iset.

import timeit
import random
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.seriesparallel.spnodes import Node
from graphtheory.seriesparallel.sptrees import make_random_sptree
from graphtheory.seriesparallel.spiset import SPTreeIndependentSet
from graphtheory.seriesparallel.spnodes import btree_inorder
from graphtheory.seriesparallel.spnodes import btree_print

V = 10
root = make_random_sptree(V)
E = 0
for tnode in btree_inorder(root):
    if tnode.type == "edge":
        E += 1
#btree_print(root)

algorithm = SPTreeIndependentSet(root)
algorithm.run()
print ( "iset {}".format( algorithm.independent_set ))
print ( "cardinality {}".format( algorithm.cardinality ))

print ( "Testing SPTreeIndependentSet ..." )
t1 = timeit.Timer(lambda: SPTreeIndependentSet(root).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

# EOF
