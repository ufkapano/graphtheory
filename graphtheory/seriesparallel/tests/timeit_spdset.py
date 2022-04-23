#!/usr/bin/env python3
#
# Sprawdzam szybkosc wyznaczania dset.

import timeit
import random
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.seriesparallel.spnodes import Node
from graphtheory.seriesparallel.sptrees import make_random_sptree
from graphtheory.seriesparallel.spdset import SPTreeDominatingSet
from graphtheory.seriesparallel.spnodes import btree_inorder
from graphtheory.seriesparallel.spnodes import btree_print

V = 10
root = make_random_sptree(V)
E = 0
for tnode in btree_inorder(root):
    if tnode.type == "edge":
        E += 1
#btree_print(root)

algorithm = SPTreeDominatingSet(root)
algorithm.run()
print ( "dset {}".format( algorithm.dominating_set ))
print ( "cardinality {}".format( algorithm.cardinality ))

print ( "Testing SPTreeDominatingSet ..." )
t1 = timeit.Timer(lambda: SPTreeDominatingSet(root).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

# EOF
