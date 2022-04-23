#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.seriesparallel.sptools import make_random_spgraph
from graphtheory.seriesparallel.sptools import find_peo_spgraph1
from graphtheory.seriesparallel.sptools import find_peo_spgraph2


print ( "Testing random sp-graph ..." )
G = make_random_spgraph(15)
#G.show()
print ( "peo1 {}".format(find_peo_spgraph1(G)) )
print ( "peo2 {}".format(find_peo_spgraph2(G)) )

print ( "Testing complete graph ..." )
gf = GraphFactory(Graph)
G = gf.make_complete(4)
#G.show()
#print ( "peo1 {}".format(find_peo_spgraph1(G)) )   # ValueError
#print ( "peo2 {}".format(find_peo_spgraph2(G)) )   # ValueError

print ( "Testing cyclic graph ..." )
G = gf.make_cyclic(10)
#G.show()
print ( "peo1 {}".format(find_peo_spgraph1(G)) )
print ( "peo2 {}".format(find_peo_spgraph2(G)) )

# EOF
