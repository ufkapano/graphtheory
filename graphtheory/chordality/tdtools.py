#!/usr/bin/python
"""
https://en.wikipedia.org/wiki/Tree_decomposition

https://en.wikipedia.org/wiki/Treewidth

"""

try:
    integer_types = (int, long)
except NameError:   # Python 3
    integer_types = (int,)
    xrange = range

import itertools
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.chordality.peotools import find_all_maximal_cliques
from graphtheory.spanningtrees.prim import PrimMST


def find_td_chordal(graph, order):
    """Finding a tree decomposition for chordal graphs."""
    cliques = find_all_maximal_cliques(graph, order)
    H = Graph()   # graf przeciec klik maksymalnych
    bag_dict = dict()
    # Budowanie workow.
    for c in cliques:
        bag = tuple(sorted(c))
        bag_dict[bag] = c
        H.add_node(bag)
    # Budowanie krawedzi grafu przeciec klik.
    for (bag1, bag2) in itertools.combinations(bag_dict, 2):
        inter = bag_dict[bag1].intersection(bag_dict[bag2])
        if inter:
            H.add_edge(Edge(bag1, bag2, -len(inter)))
    algorithm = PrimMST(H)
    algorithm.run()
    algorithm.to_tree()
    return algorithm.mst


def find_td_order(graph, order):
    """Finding a tree decomposition using a given node order."""
    if graph.is_directed():
        raise ValueError("the graph is directed")
    # Nie chce modyfikowac oryginalnego grafu.
    graph_copy = graph.copy()
    edge_list = []
    for source in order:
        # Robie klike z {source} + N(source).
        # Dla grafow cieciwowych jest to niepotrzebne.
        for (node, target) in itertools.combinations(
            graph_copy.iteradjacent(source), 2):
            edge = Edge(node, target)
            if not graph_copy.has_edge(edge):
                graph_copy.add_edge(edge)
                edge_list.append(edge)
        # Usuwanie source z krawedziami.
        graph_copy.del_node(source)
    # Robie graf cieciwowy z oryginalu.
    for edge in edge_list:
        graph.add_edge(edge)
    # Graf stal sie cieciwowy.
    T = find_td_chordal(graph, order)
    # Przywracanie oryginalu.
    for edge in edge_list:
        graph.del_edge(edge)
    return T

# EOF
