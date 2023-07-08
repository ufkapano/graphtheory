#!/usr/bin/env python3

try:
    integer_types = (int, long)
    range = xrange
except NameError:   # Python 3
    integer_types = (int,)

from graphtheory.traversing.bfs import BFSWithDepthTracker


class TreeLongestPath:
    """Finding the longest path of a single tree in O(n) time.
    
    R.W. Bulterman, F.W. van der Sommen, G. Zwaan, T. Verhoeff,
    A.J.M. van Gasteren, "On computing a longest path in a tree",
    Information Processing Letters 81(2), 93-96 (2002).
"""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        if self.graph.is_directed():
            raise ValueError("the graph is directed")
        self.longest_path = None

    def run(self):
        """Executable pseudocode."""
        # Etap 1. Z dowolnego wierzchołka robimy BFS, aby znalezc najdalszy X.
        source = next(self.graph.iternodes())
        order = []
        algorithm = BFSWithDepthTracker(self.graph)
        algorithm.run(source, pre_action=lambda pair: order.append(pair))
        source, _ = max(order, key=lambda pair: pair[1])

        # Etap 2. Z wierzcholka X robimy BFS, aby znalezc najdalszy Y.
        # Longest path is from X to Y.
        algorithm = BFSWithDepthTracker(self.graph)
        algorithm.run(source, pre_action=lambda pair: order.append(pair))
        target, _ = max(order, key=lambda pair: pair[1])
        self.longest_path = algorithm.path(source, target)

# EOF
