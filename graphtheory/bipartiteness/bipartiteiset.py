#!/usr/bin/env python3

import collections
from graphtheory.bipartiteness.hopcroftkarp import HopcroftKarpSet


class BipartiteIndependentSet:
    """Finding a maximum independent set in a bipartite graph in O(m sqrt(n)) time.
    
    Notes
    -----
    Based on:

    https://en.wikipedia.org/wiki/K%C5%91nig%27s_theorem_(graph_theory)

    http://en.wikipedia.org/wiki/Hopcroft-Karp_algorithm
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.independent_set = None
        self.cardinality = 0

    def run(self):
        """Executable pseudocode."""
        algorithm = HopcroftKarpSet(self.graph)   # O(m sqrt(n)) time
        algorithm.run()

        left_part = algorithm.v1   # nie bedziemy zmieniac
        reachable_left = set(node for node in left_part
            if algorithm.mate[node] is None)   # free nodes from left_part
        reachable_right = set()

        # Kolejka na wierzcholki z left_part.
        # Beda tworzone sciezki naprzemianne o obu koncach w left_part.
        # To jest jakby BFS z wieloma zrodlami.
        queue = collections.deque(reachable_left)

        while queue:
            left = queue.popleft()

            for right in self.graph.iteradjacent(left):
                if algorithm.mate[left] == right:
                    continue   # nie chcemy sie cofac po krawedzi z matching
                if right in reachable_right:
                    continue   # tu juz bylismy na innej sciezce

                reachable_right.add(right)
                matched_left = algorithm.mate[right]

                if (matched_left is not None
                    and matched_left not in reachable_left):
                    reachable_left.add(matched_left)
                    queue.append(matched_left)

        minimum_vertex_cover = (left_part - reachable_left) | reachable_right
        self.independent_set = set(self.graph.iternodes()) - minimum_vertex_cover
        self.cardinality = len(self.independent_set)

# EOF
