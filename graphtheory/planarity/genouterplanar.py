#!/usr/bin/env python3

import random
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph

class MaximalOuterplanarGenerator:
    """Generator of maximal outerplanar graphs."""

    def __init__(self, n):
        if not isinstance(n, int):
            raise ValueError("n is not int")
        if n < 0:
            raise ValueError("negative n")
        self.n = n
        self.graph = Graph()

    def run(self):
        # create hamiltonian cycle (cycle graph)
        weights = list(range(1, 1 + 2 * self.n - 3))   # different weights
        for i in range(self.n):
            self.graph.add_edge( Edge(i, (i + 1) % self.n, weights.pop()) )
        self._generate(weights)
        return self.graph

    def _generate(self, weights):
        G = self.graph.copy()
        node_list = list(G.iternodes())   # O(V) time
        random.shuffle(node_list)   # O(V) time
        while G.v() > 3:   # O(V) time
            # fill cycle with random edges
            node = node_list.pop()   # O(1) time
            source, target = list(G.iteradjacent(node))
            chord = Edge(source, target, weights.pop())
            self.graph.add_edge(chord)
            G.add_edge(chord)
            G.del_node(node)   # with edges
        assert weights == []

# EOF
