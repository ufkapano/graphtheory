#!/usr/bin/env python3
"""
https://en.wikipedia.org/wiki/Tree_decomposition

https://en.wikipedia.org/wiki/Treewidth

"""

try:
    range = xrange
except NameError:   # Python 3
    pass

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


def find_treewidth_min_deg(graph):
    """Finding a treewidth (upper bound) using the minimum degree heuristic."""
    if graph.is_directed():
        raise ValueError("the graph is directed")
    treewidth = 0   # upper bound
    used = set()
    order = [] # kolejnosc usuwania wierzcholkow, PEO dla chordal completion
    # Nie chce modyfikowac oryginalnego grafu, wiec mam kopie.
    graph_copy = graph.copy()   # O(V+E) time and memory
    # W kazdym kroku bede usuwal jeden wierzcholek.
    for _ in range(graph.v()):
        # Wybieram node o najmniejszym stopniu, nie zaliczony do order.
        # Wierzcholki nalezace do order nie wystepuja w kopii grafu.
        #source = min(graph_copy.iternodes(), key=graph_copy.degree)
        source = min((node for node in graph_copy.iternodes()
            if node not in used), key=graph_copy.degree)
        used.add(source)
        order.append(source)
        # Szacowanie treewidth.
        treewidth = max(treewidth, graph_copy.degree(source))
        # Robie klike z {source} + N(source). Chyba czas O(V^2).
        for (node, target) in itertools.combinations(
            graph_copy.iteradjacent(source), 2):
            edge = Edge(node, target)
            if not graph_copy.has_edge(edge):
                graph_copy.add_edge(edge)
        # Usuwanie source z krawedziami.
        # Dzieki used to dziala nawet kiedy usuwane sa tylko krawedzie,
        # a wierzcholek source pozostaje (macierz sasiedztwa).
        graph_copy.del_node(source)
    return treewidth, order


def find_treewidth_mmd(graph):
    """Finding a treewidth (lower bound) using the maximum minimum degree heuristic."""
    if graph.is_directed():
        raise ValueError("the graph is directed")
    treewidth = 0   # lower bound
    used = set()
    order = [] # kolejnosc usuwania wierzcholkow, moze sie przyda
    degree_dict = dict((node, graph.degree(node))
        for node in graph.iternodes())
    bucket = list(set() for deg in range(graph.v()))   # O(V) time
    for node in graph.iternodes():   # wstawiam do kubelkow, O(V) time
        bucket[graph.degree(node)].add(node)
    for _ in range(graph.v()):   # O(V) time
        # Szukam wierzcholka o najmniejszym stopniu.
        for deg in range(graph.v()):
            if bucket[deg]:
                source = bucket[deg].pop()
                break
        used.add(source)
        order.append(source)
        # Szacowanie treewidth.
        treewidth = max(treewidth, degree_dict[source])
        # Usuwanie source.
        for target in graph.iteradjacent(source):
            # Trzeba przerzucic target do innego kubelka.
            if target in used:   # not present in bucket
                continue
            deg = degree_dict[target]   # old degree
            bucket[deg].remove(target)
            bucket[deg-1].add(target)
            degree_dict[target] = deg-1   # new degree
    return treewidth, order

# EOF
