#!/usr/bin/python

import timeit
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.forests.treedset import BorieDominatingSet
from graphtheory.forests.treedset import TreeDominatingSet

V = 10
E = V-1   # tree
graph_factory = GraphFactory(Graph)
G = graph_factory.make_tree(V, False)
#G.show()

print "Calculate parameters ..."
print "Nodes:", G.v(), V
print "Edges:", G.e(), E
print "Directed:", G.is_directed()

algorithm = BorieDominatingSet(G)
algorithm.run()
print algorithm.dominating_set
print "borie dset", algorithm.cardinality

algorithm = TreeDominatingSet(G)
algorithm.run()
print algorithm.dominating_set
print "tree dset", algorithm.cardinality

print "Testing BorieDominatingSet ..."
t1 = timeit.Timer(lambda: BorieDominatingSet(G).run())
print V, E, t1.timeit(1)            # single run

print "Testing TreeDominatingSet ..."
t1 = timeit.Timer(lambda: TreeDominatingSet(G).run())
print V, E, t1.timeit(1)            # single run

# EOF
