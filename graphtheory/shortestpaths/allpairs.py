#!/usr/bin/python

class SlowAllPairs:
    """All-pairs shortest paths algorithm in O(V**4) time."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("the graph is not directed")
        self.graph = graph
        self.distance = dict()
        self.weights = dict()
        for source in self.graph.iternodes():   # O(V**2) time
            self.distance[source] = dict()
            for target in self.graph.iternodes():
                self.distance[source][target] = float("inf")
            self.distance[source][source] = 0
        for edge in self.graph.iteredges():   # O(E) time
            self.distance[edge.source][edge.target] = edge.weight
        for source in self.graph.iternodes():
            self.weights[source] = dict(self.distance[source])

    def run(self):
        """Executable pseudocode."""
        for m in xrange(2, self.graph.v()):   # |V|-2 times
            self.distance = self.extended_shortest_paths(self.distance)
        if any(self.distance[node][node] < 0 for node in self.graph.iternodes()):
            raise ValueError("negative cycle detected")

    def extended_shortest_paths(self, old_distance):
        """O(V**3) time."""
        new_distance = dict()
        for source in self.graph.iternodes():
            new_distance[source] = dict()
            for target in self.graph.iternodes():
                new_distance[source][target] = float("inf")
                for node in self.graph.iternodes():
                    new_distance[source][target] = min(new_distance[source][target],
                        old_distance[source][node] + self.weights[node][target])
        return new_distance


class SlowAllPairsEdges:
    """All-pairs shortest paths algorithm in O(V**2 (V+E)) time."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("the graph is not directed")
        self.graph = graph
        self.distance = dict()
        self.weights = dict()
        for source in self.graph.iternodes():   # O(V**2) time
            self.distance[source] = dict()
            for target in self.graph.iternodes():
                self.distance[source][target] = float("inf")
            self.distance[source][source] = 0
        for edge in self.graph.iteredges():   # O(E) time
            self.distance[edge.source][edge.target] = edge.weight
        for source in self.graph.iternodes():
            self.weights[source] = dict(self.distance[source])

    def run(self):
        """Executable pseudocode."""
        for m in xrange(2, self.graph.v()):   # |V|-2 times
            self.distance = self.extended_shortest_paths(self.distance)
        if any(self.distance[node][node] < 0 for node in self.graph.iternodes()):
            raise ValueError("negative cycle detected")

    def extended_shortest_paths(self, old_distance):
        """O(V*(V+E)) time."""
        new_distance = dict()
        for source in self.graph.iternodes():   # |V| times
            new_distance[source] = dict(old_distance[source]) # IMPORTANT, O(V)
            for edge in self.graph.iteredges():   # O(E) time
                new_distance[source][edge.target] = min(
                    new_distance[source][edge.target],
                    old_distance[source][edge.source] + edge.weight)
        return new_distance


class SlowAllPairsWithPaths:   # not for FasterAllPairsSP
    """All-pairs shortest paths algorithm in O(V**4) time."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("the graph is not directed")
        self.graph = graph
        self.distance = dict()
        self.weights = dict()
        self.parent = dict()
        for source in self.graph.iternodes():   # O(V**2) time
            self.distance[source] = dict()
            self.parent[source] = dict()
            for target in self.graph.iternodes():
                self.distance[source][target] = float("inf")
                self.parent[source][target] = None
            self.distance[source][source] = 0
        for edge in self.graph.iteredges():   # O(E) time
            self.distance[edge.source][edge.target] = edge.weight
            self.parent[edge.source][edge.target] = edge.source
        for source in self.graph.iternodes():
            self.weights[source] = dict(self.distance[source])

    def run(self):
        """Executable pseudocode."""
        for m in xrange(2, self.graph.v()):   # |V|-2 times
            self.distance = self.extended_shortest_paths(self.distance)
        if any(self.distance[node][node] < 0 for node in self.graph.iternodes()):
            raise ValueError("negative cycle detected")

    def extended_shortest_paths(self, old_distance):
        """O(V**3) time."""
        new_distance = dict()
        for source in self.graph.iternodes():
            new_distance[source] = dict(old_distance[source]) # IMPORTANT, copy
            for target in self.graph.iternodes():
                for node in self.graph.iternodes():
                    alt = old_distance[source][node] + self.weights[node][target]
                    if new_distance[source][target] > alt:
                        new_distance[source][target] = alt
                        self.parent[source][target] = node
        return new_distance


class FasterAllPairs:
    """All-pairs shortest paths algorithm in O(V**3 log V) time."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("the graph is not directed")
        self.graph = graph
        self.distance = dict()
        for source in self.graph.iternodes():   # O(V**2) time
            self.distance[source] = dict()
            for target in self.graph.iternodes():
                self.distance[source][target] = float("inf") # IMPORTANT
            self.distance[source][source] = 0
        for edge in self.graph.iteredges():   # O(E) time
            self.distance[edge.source][edge.target] = edge.weight

    def run(self):
        """Executable pseudocode."""
        m = 1
        while m < (self.graph.v() - 1):   # log(V) times
            self.distance = self.extended_shortest_paths(self.distance)
            m = 2 * m
        if any(self.distance[node][node] < 0 for node in self.graph.iternodes()):
            raise ValueError("negative cycle detected")

    def extended_shortest_paths(self, old_distance):
        """O(V**3) time."""
        new_distance = dict()
        for source in self.graph.iternodes():
            new_distance[source] = dict()
            for target in self.graph.iternodes():
                new_distance[source][target] = float("inf")
                for node in self.graph.iternodes():
                    new_distance[source][target] = min(new_distance[source][target],
                        old_distance[source][node] + old_distance[node][target])
        return new_distance

# EOF
