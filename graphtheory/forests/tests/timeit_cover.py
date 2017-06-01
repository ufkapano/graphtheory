#!/usr/bin/python

import timeit
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.forests.treecover import BorieNodeCover
from graphtheory.forests.treecover import TreeNodeCover1
from graphtheory.forests.treecover import TreeNodeCover2

V = 10
E = V-1   # tree
graph_factory = GraphFactory(Graph)
G = graph_factory.make_tree(V, False)
#G.show()

print "Calculate parameters ..."
print "Nodes:", G.v(), V
print "Edges:", G.e(), E
print "Directed:", G.is_directed()

algorithm = BorieNodeCover(G)
algorithm.run()
print algorithm.node_cover
print "borie cover", algorithm.cardinality

algorithm = TreeNodeCover1(G)
algorithm.run()
print algorithm.node_cover
print "tree cover1", algorithm.cardinality

algorithm = TreeNodeCover2(G)
algorithm.run()
print algorithm.node_cover
print "tree cover2", algorithm.cardinality

print "Testing BorieNodeCover ..."
t1 = timeit.Timer(lambda: BorieNodeCover(G).run())
print V, E, t1.timeit(1)            # single run

print "Testing TreeNodeCover1 ..."
t1 = timeit.Timer(lambda: TreeNodeCover1(G).run())
print V, E, t1.timeit(1)            # single run

print "Testing TreeNodeCover2 ..."
t1 = timeit.Timer(lambda: TreeNodeCover2(G).run())
print V, E, t1.timeit(1)            # single run

# EOF
