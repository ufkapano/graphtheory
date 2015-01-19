#!/usr/bin/python

class FloydWarshall:
    """The Floyd-Warshall algorithm."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("graph is not directed")
        self.graph = graph
        self.distance = dict()
        for source in self.graph.iternodes():
            self.distance[source] = dict()
            for target in self.graph.iternodes():
                self.distance[source][target] = float("inf")
            self.distance[source][source] = 0
        for edge in self.graph.iteredges():
            self.distance[edge.source][edge.target] = edge.weight

    def run(self):
        """Executable pseudocode."""
        for node in self.graph.iternodes():
            for source in self.graph.iternodes():
                for target in self.graph.iternodes():
                    self.distance[source][target] = min(
                        self.distance[source][target],
                        self.distance[source][node] 
                        + self.distance[node][target])
        if any(self.distance[node][node] < 0 
            for node in self.graph.iternodes()):
                raise ValueError("negative cycle detected")


class FloydWarshallPaths:
    """The Floyd-Warshall algorithm with path reconstruction."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("graph is not directed")
        self.graph = graph
        self.distance = dict()
        self.parent = dict()
        for source in self.graph.iternodes():
            self.distance[source] = dict()
            self.parent[source] = dict()
            for target in self.graph.iternodes():
                self.distance[source][target] = float("inf")
                self.parent[source][target] = None
            self.distance[source][source] = 0
        for edge in self.graph.iteredges():
            self.distance[edge.source][edge.target] = edge.weight
            self.parent[edge.source][edge.target] = edge.source

    def run(self):
        """Executable pseudocode."""
        for node in self.graph.iternodes():
            for source in self.graph.iternodes():
                for target in self.graph.iternodes():
                    alt = self.distance[source][node] + self.distance[node][target]
                    if self.distance[source][target] > alt:
                        self.distance[source][target] = alt
                        self.parent[source][target] = self.parent[node][target]
        if any(self.distance[node][node] < 0
            for node in self.graph.iternodes()):
                raise ValueError("negative cycle")

    def path(self, source, target):
        """Path reconstruction."""
        if source == target:
            return [source]
        elif self.parent[source][target] is None:
            raise ValueError("no path to target")
        else:
            return self.path(source, self.parent[target]) + [target]


class FloydWarshallAllGraphs:
    """The Floyd-Warshall algorithm, nonnegatibe edge weights."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            if any(edge.weight < 0 for edge in graph.iteredges()):
                raise ValueError("negative edge weight")
        self.graph = graph
        self.distance = dict()
        for source in self.graph.iternodes():
            self.distance[source] = dict()
            for target in self.graph.iternodes():
                self.distance[source][target] = float("inf")
            self.distance[source][source] = 0
        if self.graph.is_directed():
            for edge in self.graph.iteredges():
                self.distance[edge.source][edge.target] = edge.weight
        else:
            for edge in self.graph.iteredges():
                self.distance[edge.source][edge.target] = edge.weight
                self.distance[edge.target][edge.source] = edge.weight

    def run(self):
        """Executable pseudocode."""
        for node in self.graph.iternodes():
            for source in self.graph.iternodes():
                for target in self.graph.iternodes():
                    self.distance[source][target] = min(
                        self.distance[source][target],
                        self.distance[source][node] 
                        + self.distance[node][target])
        if any(self.distance[node][node] < 0 
            for node in self.graph.iternodes()):
                raise ValueError("negative cycle detected")

# EOF
