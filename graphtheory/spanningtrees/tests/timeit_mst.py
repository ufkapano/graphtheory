#!/usr/bin/env python3

import timeit
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.connectivity.connected import is_connected
from graphtheory.algorithms.acyclic import is_acyclic
from graphtheory.bipartiteness.bipartite import is_bipartite
from graphtheory.connectivity.cutnodes import is_biconnected
from graphtheory.spanningtrees.boruvka import BoruvkaMST
from graphtheory.spanningtrees.prim import PrimMST
from graphtheory.spanningtrees.prim import PrimMSTWithEdges
from graphtheory.spanningtrees.prim import PrimMatrixMST
from graphtheory.spanningtrees.prim import PrimMatrixMSTWithEdges
from graphtheory.spanningtrees.prim import PrimConnectedMST
from graphtheory.spanningtrees.prim import PrimTrivialMST
from graphtheory.spanningtrees.kruskal import KruskalMST
from graphtheory.spanningtrees.kruskal import KruskalMSTSorted

V = 50
graph_factory = GraphFactory(Graph)
G = graph_factory.make_random(V, False, 0.5)
#G = graph_factory.make_complete(V, False)
#G = graph_factory.make_cyclic(V, False)
E = G.e()
#G.show()

print ( "Calculate parameters ..." )
print ( "Nodes: {} {}".format(G.v(), V) )
print ( "Edges: {} {}".format(G.e(), E) )
print ( "Directed: {}".format(G.is_directed()) )
print ( "Connected: {}".format(is_connected(G)) )
print ( "Biconnected: {}".format(is_biconnected(G)) )
print ( "Acyclic: {}".format(is_acyclic(G)) )
print ( "Bipartite: {}".format(is_bipartite(G)) )
Delta = max(G.degree(node) for node in G.iternodes())
print ( "Delta: {}".format(Delta) )

print ("Testing BoruvkaMST ..." )
t1 = timeit.Timer(lambda: BoruvkaMST(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ("Testing PrimMST ..." )
t1 = timeit.Timer(lambda: PrimMST(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ("Testing PrimMSTWithEdges ..." )
t1 = timeit.Timer(lambda: PrimMSTWithEdges(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ("Testing PrimMatrixMST ..." )
t1 = timeit.Timer(lambda: PrimMatrixMST(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ("Testing PrimMatrixMSTWithEdges ..." )
t1 = timeit.Timer(lambda: PrimMatrixMSTWithEdges(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ("Testing PrimConnectedMST ..." )
t1 = timeit.Timer(lambda: PrimConnectedMST(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ("Testing PrimTrivialMST ..." )
t1 = timeit.Timer(lambda: PrimTrivialMST(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ("Testing KruskalMST ..." )
t1 = timeit.Timer(lambda: KruskalMST(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ("Testing KruskalMSTSorted ..." )
t1 = timeit.Timer(lambda: KruskalMSTSorted(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

# EOF
