#!/usr/bin/env python3

try:
    range = xrange
except NameError:   # Python 3
    pass

import random
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph


def make_random_ktree(n, k):
    """Make a random k-tree with n vertices, PEO = range(n)."""
    if k >= n:
        raise ValueError("bad k")   # run time error possible
    graph = Graph(n)
    if n < 1:
        raise ValueError("bad n")
    elif n == 1:
        graph.add_node(0)
    else:
        for node in range(n):
            graph.add_node(node)
        # Make {n-k-1, ..., n-1} into (k+1)-clique in graph.
        for source in range(n-k-1, n):
            for target in range(n-k-1, n):
                if source < target:
                    graph.add_edge(Edge(source, target))
        node = n-k-2
        while node >= 0:
            source = random.choice(range(node+1, n-k))
            neighbors = set(target for target in graph.iteradjacent(source)
                            if source < target)
            neighbors.add(source)   # closed neighborhood
            target = random.choice(list(neighbors))
            neighbors.remove(target)
            for target in neighbors:
                graph.add_edge(Edge(node, target))
            node -= 1
    return graph


def make_random_chordal(n):
    """Make a connected chordal graph with n vertices, PEO = range(n)."""
    graph = Graph(n)
    if n < 1:
        raise ValueError("bad n")
    elif n == 1:
        graph.add_node(0)
    else:
        for node in range(n):
            graph.add_node(node)
        # Make the first 2-clique (one edge).
        graph.add_edge(Edge(n-2, n-1))
        node = n-3
        while node >= 0:
            # Select source from the range(node+1, n-1).
            # To jest jakby wybor duzej kliki,
            #source = random.choice(range(node+1, n)) # nie chce jednego
            source = random.choice(range(node+1, n-1))
            # Teraz zbieram wierzcholki tej kliki, ale one maja byc
            # wieksze od source, wieksze numery!
            neighbors = list(target for target in graph.iteradjacent(source)
                            if source < target)
            neighbors.append(source)   # closed neighborhood
            # Z duzej kliki wybieram mala k-klike, losuje k.
            k = random.randrange(1, len(neighbors)+1)
            neighbors = random.sample(neighbors, k)
            # Connect node to all nodes from neighbors.
            for target in neighbors:
                graph.add_edge(Edge(node, target))
            node -= 1
    return graph

# EOF
