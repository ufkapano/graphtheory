#!/usr/bin/python

import unittest
import timeit
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.forests.treecenter import TreeCenter
from graphtheory.structures.factory import GraphFactory

V = 1000   # liczba wierzcholkow
E = V-1      # liczba krawedzi
graph_factory = GraphFactory(Graph)
G = graph_factory.make_tree(V)
#G.show()

print "Calculate parameters ..."
print "Nodes:", G.v(), V
print "Edges:", G.e(), E
assert G.v() == V
assert G.e() == E
print "Directed:", G.is_directed()
print "Max degree:", max(G.degree(node) for node in G.iternodes())

print "Testing TreeCenter ..."
t1 = timeit.Timer(lambda: TreeCenter(G).run())
print V, E, t1.timeit(1)            # pojedyncze wykonanie

# EOF
