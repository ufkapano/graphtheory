#!/usr/bin/env python3

import timeit
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.independentsets.isetus import UnorderedSequentialIndependentSet1
from graphtheory.independentsets.isetus import UnorderedSequentialIndependentSet2
from graphtheory.independentsets.isetus import UnorderedSequentialIndependentSet3
from graphtheory.independentsets.isetrs import RandomSequentialIndependentSet1
from graphtheory.independentsets.isetrs import RandomSequentialIndependentSet2
from graphtheory.independentsets.isetrs import RandomSequentialIndependentSet3
from graphtheory.independentsets.isetsf import SmallestFirstIndependentSet1
from graphtheory.independentsets.isetsf import SmallestFirstIndependentSet2
from graphtheory.independentsets.isetsf import SmallestFirstIndependentSet3
from graphtheory.independentsets.isetsf import SmallestFirstIndependentSet4
from graphtheory.independentsets.isetsf import SmallestFirstIndependentSet5
from graphtheory.independentsets.isetsf import SmallestFirstIndependentSet6
from graphtheory.independentsets.isetsf import SmallestFirstIndependentSet7
from graphtheory.independentsets.isetll import LargestLastIndependentSet1
from graphtheory.independentsets.isetll import LargestLastIndependentSet2
from graphtheory.independentsets.isetll import LargestLastIndependentSet3
from graphtheory.independentsets.isetll import LargestLastIndependentSet4
from graphtheory.independentsets.isetll import LargestLastIndependentSet5
from graphtheory.independentsets.isetll import LargestLastIndependentSet6
from graphtheory.independentsets.isetll import LargestLastIndependentSet7

V = 10
graph_factory = GraphFactory(Graph)
G = graph_factory.make_random(V, False, edge_probability=0.5)
E = G.e()
#G.show()

print ( "Calculate parameters ..." )
print ( "Nodes: {} {}".format( G.v(), V ))
print ( "Edges: {} {}".format( G.e(), E ))
print ( "Directed: {}".format( G.is_directed() ))

print ( "Testing UnorderedSequentialIndependentSet1 ..." )
t1 = timeit.Timer(lambda: UnorderedSequentialIndependentSet1(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing UnorderedSequentialIndependentSet2 ..." )
t1 = timeit.Timer(lambda: UnorderedSequentialIndependentSet2(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing UnorderedSequentialIndependentSet3 ..." )
t1 = timeit.Timer(lambda: UnorderedSequentialIndependentSet3(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing RandomSequentialIndependentSet1 ..." )
t1 = timeit.Timer(lambda: RandomSequentialIndependentSet1(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing RandomSequentialIndependentSet2 ..." )
t1 = timeit.Timer(lambda: RandomSequentialIndependentSet2(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing RandomSequentialIndependentSet3 ..." )
t1 = timeit.Timer(lambda: RandomSequentialIndependentSet3(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing SmallestFirstIndependentSet1 ..." )
t1 = timeit.Timer(lambda: SmallestFirstIndependentSet1(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing SmallestFirstIndependentSet2 ..." )
t1 = timeit.Timer(lambda: SmallestFirstIndependentSet2(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing SmallestFirstIndependentSet3 ..." )
t1 = timeit.Timer(lambda: SmallestFirstIndependentSet3(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing SmallestFirstIndependentSet4 ..." )
t1 = timeit.Timer(lambda: SmallestFirstIndependentSet4(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing SmallestFirstIndependentSet5 ..." )
t1 = timeit.Timer(lambda: SmallestFirstIndependentSet5(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing SmallestFirstIndependentSet6 ..." )
t1 = timeit.Timer(lambda: SmallestFirstIndependentSet6(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing SmallestFirstIndependentSet7 ..." )
t1 = timeit.Timer(lambda: SmallestFirstIndependentSet7(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing LargestLastIndependentSet1 ..." )
t1 = timeit.Timer(lambda: LargestLastIndependentSet1(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing LargestLastIndependentSet2 ..." )
t1 = timeit.Timer(lambda: LargestLastIndependentSet2(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing LargestLastIndependentSet3 ..." )
t1 = timeit.Timer(lambda: LargestLastIndependentSet3(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing LargestLastIndependentSet4 ..." )
t1 = timeit.Timer(lambda: LargestLastIndependentSet4(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing LargestLastIndependentSet5 ..." )
t1 = timeit.Timer(lambda: LargestLastIndependentSet5(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing LargestLastIndependentSet6 ..." )
t1 = timeit.Timer(lambda: LargestLastIndependentSet6(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

print ( "Testing LargestLastIndependentSet7 ..." )
t1 = timeit.Timer(lambda: LargestLastIndependentSet7(G).run())
print ( "{} {} {}".format(V, E, t1.timeit(1)) )   # single run

# EOF
