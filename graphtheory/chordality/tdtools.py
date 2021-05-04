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

# EOF
