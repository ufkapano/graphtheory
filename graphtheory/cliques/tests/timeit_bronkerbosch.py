#!/usr/bin/env python3

import timeit
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.bipartiteness.bipartite import is_bipartite
from graphtheory.cliques.bronkerbosch import BronKerboschClassic
from graphtheory.cliques.bronkerbosch2 import BronKerboschClassicIterator
from graphtheory.cliques.bronkerboschrp import BronKerboschRandomPivot
from graphtheory.cliques.bronkerboschdp import BronKerboschDegreePivot
from graphtheory.cliques.bronkerboschdeg import BronKerboschDegeneracy

# Wnioski.
# BronKerboschDegreePivot ma najmniejsza liczbe wywolan rekurencyjnych
# dla V=100 i jest wtedy najszybszy.
# W testach za podstawe mozna wziac czas wykonania klasycznego BK,
# potem wzgledem niego podac ile procent czasu lub wywolan rekorencyjnych
# daja pozostale wersje.

#V = 100   # random pivot BK trwa 2/3 czasu clasic BK
V = 100
graph_factory = GraphFactory(Graph)
G = graph_factory.make_random(V, False, 0.5)
#G = graph_factory.make_complete(V, False)
#G = graph_factory.make_cyclic(V, False)
#G = graph_factory.make_triangle(size=70)
V = G.v()
E = G.e()
#G.show()

print("Calculate parameters ...")
print("Nodes:", G.v(), V)
print("Edges:", G.e(), E)
print("Directed:", G.is_directed())
print("Bipartite:", is_bipartite(G))
Delta = max(G.degree(node) for node in G.iternodes())
print("Delta:", Delta)

print("Testing BronKerboschClassic ...")
t1 = timeit.Timer(lambda: BronKerboschClassic(G).run())
print(V, E, t1.timeit(1))            # pojedyncze wykonanie

print("Testing BronKerboschClassicIterator ...")
t1 = timeit.Timer(lambda: list(BronKerboschClassicIterator(G).run()))
print(V, E, t1.timeit(1))            # pojedyncze wykonanie

print("Testing BronKerboschRandomPivot ...")
t1 = timeit.Timer(lambda: BronKerboschRandomPivot(G).run())
print(V, E, t1.timeit(1))            # pojedyncze wykonanie

print("Testing BronKerboschDegreePivot ...")
t1 = timeit.Timer(lambda: BronKerboschDegreePivot(G).run())
print(V, E, t1.timeit(1))            # pojedyncze wykonanie

print("Testing BronKerboschDegeneracy ...")
t1 = timeit.Timer(lambda: BronKerboschDegeneracy(G).run())
print(V, E, t1.timeit(1))            # pojedyncze wykonanie

# EOF
