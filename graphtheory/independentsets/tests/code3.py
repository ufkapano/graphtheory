#!/usr/bin/python3
#
# Kody korekcyjne. Wezly sa polaczone, jezeli roznia sie
# na jednym lub 2 miejscach.
# Dla 3 bitow jest 2^3=8 wezlow.

import itertools
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.independentsets.isetbt import BacktrackingIndependentSet

G = Graph()
#nodes = ['000','001','010','011','100','101','110','111']
nodes = [''.join(t) for t in itertools.product('01', repeat=3)]
print(nodes)

edges1 = [Edge('000','100'), Edge('000','010'), Edge('000','001'),
    Edge('001','101'), Edge('001','011'), Edge('010','110'),
    Edge('010','011'), Edge('011','111'), Edge('100','110'),
    Edge('100','101'), Edge('101','111'), Edge('110','111'),]

edges2 = [Edge('000','110'), Edge('000','101'), Edge('000','011'),
    Edge('001','111'), Edge('001','100'), Edge('001','010'),
    Edge('010','100'), Edge('010','111'), Edge('011','101'),
    Edge('011','110'), Edge('100','111'), Edge('101','110'),]

for node in nodes:
    G.add_node(node)
for edge in edges1:
    G.add_edge(edge)
for edge in edges2:
    G.add_edge(edge)

algorithm = BacktrackingIndependentSet(G)
algorithm.run()   # znajduje najlepszy iset
print(algorithm.cardinality)
print(algorithm.independent_set)

#EOF
