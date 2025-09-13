#!/usr/bin/env python3

import timeit
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.forests.treedset import BorieDominatingSet
from graphtheory.forests.treedset import TreeDominatingSet1
from graphtheory.forests.treedset import TreeDominatingSet2
from graphtheory.forests.treedset import TreeDominatingSet3
from graphtheory.forests.treedset import TreeDominatingSet4
from graphtheory.forests.treeidset import TreeIndependentDominatingSet

V = 10
E = V-1   # tree
graph_factory = GraphFactory(Graph)
G = graph_factory.make_tree(V, False)
#G.show()

print ( "Calculate parameters ..." )
print ( "Nodes: {} {}".format( G.v(), V ))
print ( "Edges: {} {}".format( G.e(), E ))
print ( "Directed: {}".format( G.is_directed() ))

algorithm = BorieDominatingSet(G)
algorithm.run()
print ( algorithm.dominating_set )
print ( "borie dset []".format( algorithm.cardinality ))

algorithm = TreeDominatingSet1(G)
algorithm.run()
print ( algorithm.dominating_set )
print ( "tree dset1 {}".format( algorithm.cardinality ))

algorithm = TreeIndependentDominatingSet(G)
algorithm.run()
print ( algorithm.dominating_set )
print ( "tree idset {}".format( algorithm.cardinality ))

print ( "Testing BorieDominatingSet ..." )
t1 = timeit.Timer(lambda: BorieDominatingSet(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing TreeDominatingSet1 ..." )
t1 = timeit.Timer(lambda: TreeDominatingSet1(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing TreeDominatingSet2 ..." )
t1 = timeit.Timer(lambda: TreeDominatingSet2(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing TreeDominatingSet3 ..." )
t1 = timeit.Timer(lambda: TreeDominatingSet3(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing TreeDominatingSet4 ..." )
t1 = timeit.Timer(lambda: TreeDominatingSet4(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing TreeIndependentDominatingSet ..." )
t1 = timeit.Timer(lambda: TreeIndependentDominatingSet(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

# EOF
