#! /usr/bin/python
#
# floydwarshall.py
#
# The Floyd-Warshall algorithm.

class FloydWarshall:
    """The Floyd-Warshall algorithm."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("graph is not directed")
        self.graph = graph
        self.dist = dict()
        for source in self.graph.iternodes():
            self.dist[source] = dict()
            for target in self.graph.iternodes():
                self.dist[source][target] = float("inf")
            self.dist[source][source] = 0
        for edge in self.graph.iteredges():
            self.dist[edge.source][edge.target] = edge.weight

    def run(self):
        """Executable pseudocode."""
        for node in self.graph.iternodes():
            for source in self.graph.iternodes():
                for target in self.graph.iternodes():
                    self.dist[source][target] = min(self.dist[source][target],
                        self.dist[source][node] + self.dist[node][target])
        if any(self.dist[node][node] < 0 for node in self.graph.iternodes()):
            raise ValueError("negative cycle")


class FloydWarshallPaths:
    """The Floyd-Warshall algorithm with path reconstruction."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("graph is not directed")
        self.graph = graph
        self.dist = dict()
        self.prev = dict()
        for source in self.graph.iternodes():
            self.dist[source] = dict()
            self.prev[source] = dict()
            for target in self.graph.iternodes():
                self.dist[source][target] = float("inf")
                self.prev[source][target] = None
            self.dist[source][source] = 0
        for edge in self.graph.iteredges():
            self.dist[edge.source][edge.target] = edge.weight
            self.prev[edge.source][edge.target] = edge.source

    def run(self):
        """Executable pseudocode."""
        for node in self.graph.iternodes():
            for source in self.graph.iternodes():
                for target in self.graph.iternodes():
                    alt = self.dist[source][node] + self.dist[node][target]
                    if alt < self.dist[source][target]:
                        self.dist[source][target] = alt
                        self.prev[source][target] = self.prev[node][target]
        if any(self.dist[node][node] < 0 for node in self.graph.iternodes()):
            raise ValueError("negative cycle")

    def path(self, source, target):
        """Path reconstruction."""
        if source == target:
            return [source]
        elif self.prev[source][target] is None:
            raise ValueError("no path to target")
        else:
            return self.path(source, self.prev[target]) + [target]

# EOF
