#!/usr/bin/env python3
#
# Obliczanie max iset algorytmem dokladnym dla ogolnych grafow.
# Sensowny czas tylko dla malych grafow.
# Bedzie mozna porownac wyniki dla AT-free graphs.

from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.independentsets.isetbt import BacktrackingIndependentSet

# 1---4---5---6
# |   | /
# 2---3
print("House with edge ...")
G = Graph(directed=False)
nodes = ["1", "2", "3", "4", "5", "6"]
edges = [Edge("1", "2"), Edge("1", "4"), Edge("2", "3"),
    Edge("3", "4"), Edge("4", "5"), Edge("3", "5"), Edge("5", "6")]
for node in nodes:
    G.add_node(node)
for edge in edges:
    G.add_edge(edge)
#G.show()

algorithm = BacktrackingIndependentSet(G)
algorithm.run()
print(algorithm.independent_set)
print(algorithm.cardinality)

print()

print("Graph with n=18 ...")
G = Graph(directed=False)
nodes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "11", "12", "13", "14", "15", "16", "17"]
edges = [Edge("0", "1"), Edge("1", "2"), Edge("2", "3"),
    Edge("3", "4"), Edge("4", "5"), Edge("5", "6"),
    Edge("6", "7"), Edge("7", "8"), Edge("8", "17"),
    Edge("17", "16"), Edge("16", "15"), Edge("15", "14"),
    Edge("14", "13"), Edge("13", "12"), Edge("12", "11"),
    Edge("11", "10"), Edge("10", "9"), Edge("9", "0"),
    Edge("1", "10"), Edge("2", "11"), Edge("3", "12"),
    Edge("5", "14"), Edge("6", "15"), Edge("7", "16"),
    Edge("3", "13"), Edge("13", "5"), Edge("14", "4"),
    Edge("4", "12")]
for node in nodes:
    G.add_node(node)
for edge in edges:
    G.add_edge(edge)
#G.show()

algorithm = BacktrackingIndependentSet(G)
algorithm.run()
print(algorithm.independent_set)
print(algorithm.cardinality)

# EOF
