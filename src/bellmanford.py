#!/usr/bin/python
#
# bellmanford.py
#
# The Bellman-Ford algorithm.

class BellmanFord:
    """The Bellman-Ford algorithm for the shortest path problem."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.dist = dict(((node, float("inf")) for node in self.graph.iternodes()))
        # shortest path tree
        self.prev = dict(((node, None) for node in self.graph.iternodes()))

    def run(self, source):
        """Executable pseudocode."""
        self.source = source
        self.dist[source] = 0
        for step in xrange(self.graph.v()-1):   # |V|-1 times
            for edge in self.graph.iteredges():   # O(E) time
                self.relax(edge)
        # check for negative cycles
        for edge in self.graph.iteredges():   # O(E) time
            if self.dist[edge.target] > self.dist[edge.source] + edge.weight:
                raise ValueError("negative cycle")

    def relax(self, edge):
        """Edge relaxation."""
        alt = self.dist[edge.source] + edge.weight
        if self.dist[edge.target] > alt:
            self.dist[edge.target] = alt
            self.prev[edge.target] = edge.source
            return True
        return False

    def path_to(self, end):
        """Construct a path from source to target."""
        if self.source == end:
            return [self.source]
        elif self.prev[end] is None:
            raise Exception("no path to node")
        else:
            return self.path_to(self.prev[end]) + [end]

# EOF
