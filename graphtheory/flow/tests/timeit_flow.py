#!/usr/bin/python

import timeit
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.flow.fordfulkerson import FordFulkerson
from graphtheory.flow.fordfulkerson import FordFulkersonSparse
from graphtheory.flow.fordfulkerson import FordFulkersonWithEdges
from graphtheory.flow.fordfulkerson import FordFulkersonRecursive
from graphtheory.flow.fordfulkerson import FordFulkersonRecursiveWithEdges
from graphtheory.flow.edmondskarp import EdmondsKarp
from graphtheory.flow.edmondskarp import EdmondsKarpSparse

V = 10
graph_factory = GraphFactory(Graph)
G = graph_factory.make_flow_network(V)
E = G.e()
#G.show()

print "Calculate parameters ..."
print "Nodes:", G.v(), V
print "Edges:", G.e(), E
print "Directed:", G.is_directed()

print "Testing FordFulkerson ..."
t1 = timeit.Timer(lambda: FordFulkerson(G).run(0, V-1))
print V, E, t1.timeit(1)            # single run

print "Testing FordFulkersonSparse ..."
t1 = timeit.Timer(lambda: FordFulkersonSparse(G).run(0, V-1))
print V, E, t1.timeit(1)            # single run

print "Testing FordFulkersonWithEdges ..."
t1 = timeit.Timer(lambda: FordFulkersonWithEdges(G).run(0, V-1))
print V, E, t1.timeit(1)            # single run

print "Testing FordFulkersonRecursive ..."
t1 = timeit.Timer(lambda: FordFulkersonRecursive(G).run(0, V-1))
print V, E, t1.timeit(1)            # single run

print "Testing FordFulkersonRecursiveWithEdges ..."
t1 = timeit.Timer(lambda: FordFulkersonRecursiveWithEdges(G).run(0, V-1))
print V, E, t1.timeit(1)            # single run

print "Testing EdmondsKarp ..."
t1 = timeit.Timer(lambda: EdmondsKarp(G).run(0, V-1))
print V, E, t1.timeit(1)            # single run

print "Testing EdmondsKarpSparse ..."
t1 = timeit.Timer(lambda: EdmondsKarpSparse(G).run(0, V-1))
print V, E, t1.timeit(1)            # single run

# EOF
