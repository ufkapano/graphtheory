#!/usr/bin/env python3

import timeit
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.connectivity.cutedges import TrivialCutEdge
from graphtheory.connectivity.cutedges import TarjanCutEdge
from graphtheory.connectivity.cutedges import TarjanCutEdgeWithEdges

V = 10
graph_factory = GraphFactory(Graph)
#G = graph_factory.make_cyclic(n=V, directed=False)
G = graph_factory.make_tree(n=V, directed=False)
E = G.e()
#G.show()

algorithm = TarjanCutEdgeWithEdges(G)
algorithm.run()
print(algorithm.cut_edges)

print ("Testing TrivialCutEdge ..." )
t1 = timeit.Timer(lambda: TrivialCutEdge(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ("Testing TarjanCutEdge ..." )
t1 = timeit.Timer(lambda: TarjanCutEdge(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ("Testing TarjanCutEdgeWithEdges ..." )
t1 = timeit.Timer(lambda: TarjanCutEdgeWithEdges(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

# EOF
