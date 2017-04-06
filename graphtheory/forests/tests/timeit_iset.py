#!/usr/bin/python

import timeit
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.forests.treeiset import BorieIndependentSet
from graphtheory.forests.treeiset import TreeIndependentSet

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

algorithm = TreeIndependentSet(G)
algorithm.run()
print algorithm.independent_set
print "tree iset", algorithm.cardinality

print "Testing BorieIndependentSet ..."
t1 = timeit.Timer(lambda: BorieIndependentSet(G).run())
print V, E, t1.timeit(1)            # single run

print "Testing TreeIndependentSet ..."
t1 = timeit.Timer(lambda: TreeIndependentSet(G).run())
print V, E, t1.timeit(1)            # single run

# EOF
