#!/usr/bin/python

import timeit
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.forests.treeiset import BorieIndependentSet
from graphtheory.forests.treeiset import TreeIndependentSet1
from graphtheory.forests.treeiset import TreeIndependentSet2

V = 10
E = V-1   # tree
graph_factory = GraphFactory(Graph)
G = graph_factory.make_tree(V, False)
#G.show()

print "Calculate parameters ..."
print "Nodes:", G.v(), V
print "Edges:", G.e(), E
print "Directed:", G.is_directed()

algorithm = BorieIndependentSet(G)
algorithm.run()
print algorithm.independent_set
print "borie iset", algorithm.cardinality

algorithm = TreeIndependentSet1(G)
algorithm.run()
print algorithm.independent_set
print "tree iset1", algorithm.cardinality

algorithm = TreeIndependentSet2(G)
algorithm.run()
print algorithm.independent_set
print "tree iset2", algorithm.cardinality

print "Testing BorieIndependentSet ..."
t1 = timeit.Timer(lambda: BorieIndependentSet(G).run())
print V, E, t1.timeit(1)            # single run

print "Testing TreeIndependentSet1 ..."
t1 = timeit.Timer(lambda: TreeIndependentSet1(G).run())
print V, E, t1.timeit(1)            # single run

print "Testing TreeIndependentSet2 ..."
t1 = timeit.Timer(lambda: TreeIndependentSet2(G).run())
print V, E, t1.timeit(1)            # single run

# EOF
