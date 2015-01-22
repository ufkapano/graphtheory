#!/usr/bin/python

class BellmanFord:
    """The Bellman-Ford algorithm for the shortest path problem."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("graph is not directed")
        self.graph = graph
        self.distance = dict(((node, float("inf")) for node in self.graph.iternodes()))
        # Shortest path tree as a dictionary.
        self.parent = dict(((node, None) for node in self.graph.iternodes()))

    def run(self, source):
        """Executable pseudocode."""
        self.source = source
        self.distance[source] = 0
        for step in xrange(self.graph.v()-1):   # |V|-1 times
            for edge in self.graph.iteredges():   # O(E) time
                self._relax(edge)
        # Check for negative cycles.
        for edge in self.graph.iteredges():   # O(E) time
            if self.distance[edge.target] > self.distance[edge.source] + edge.weight:
                raise ValueError("negative cycle")

    def _relax(self, edge):
        """Edge relaxation."""
        alt = self.distance[edge.source] + edge.weight
        if self.distance[edge.target] > alt:
            self.distance[edge.target] = alt
            self.parent[edge.target] = edge.source
            return True
        return False

    def path(self, target):
        """Construct a path from source to target."""
        if self.source == target:
            return [self.source]
        elif self.parent[target] is None:
            raise ValueError("no path to target")
        else:
            return self.path(self.parent[target]) + [target]

# EOF
