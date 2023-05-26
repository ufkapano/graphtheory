#!/usr/bin/python3
#
# Kody korekcyjne. Wezly sa polaczone, jezeli roznia sie
# na jednym lub 2 miejscach.
# Dla 3 bitow jest 2^3=8 wezlow.
# Dla 4 bitow jest 2^4=16 wezlow.
# Dla 5 bitow jest 2^5=32 wezlow.
# Dla 6 bitow jest 2^6=64 wezlow.

import itertools
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.independentsets.isetbt import BacktrackingIndependentSet

bits = 5
G = Graph()
nodes = [''.join(t) for t in itertools.product("01", repeat=bits)]
print(nodes)

edges1 = []   # distance 1 bit
for node in nodes:
    for i in range(bits):
        #node2 = node[0:i] + ('0' if node[i] == '1' else '1') + node[i+1:]
        list1 = list(node)   # lista znakow
        list1[i] = '0' if node[i] == '1' else '1'
        node2 = ''.join(list1)
        edges1.append(Edge(node, node2))
#print(edges1)

edges2 = []   # distance 2 bits
for node in nodes:
    for (i,j) in itertools.combinations(range(bits), 2):
        list1 = list(node)
        list1[i] = '0' if node[i] == '1' else '1'
        list1[j] = '0' if node[j] == '1' else '1'
        node2 = ''.join(list1)
        edges2.append(Edge(node, node2))
#print(edges2)

for node in nodes:
    G.add_node(node)
for edge in edges1:
    if not G.has_edge(edge):
        G.add_edge(edge)
for edge in edges2:
    if not G.has_edge(edge):
        G.add_edge(edge)
print("V {} E {}".format(G.v(), G.e()))

algorithm = BacktrackingIndependentSet(G)
algorithm.run()   # best iset
print(algorithm.cardinality)
print(algorithm.independent_set)

#EOF
