#! /usr/bin/python
#
# allpairs.py
#
# All-pairs shorted paths algorithms.

class SlowAllPairs:
    """O(V**4) time."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("graph is not directed")
        self.graph = graph
        self.dist = dict()
        self.weights = dict()
        for source in self.graph.iternodes():   # O(V**2) time
            self.dist[source] = dict()
            for target in self.graph.iternodes():
                self.dist[source][target] = float("inf")
            self.dist[source][source] = 0
        for edge in self.graph.iteredges():   # O(E) time
            self.dist[edge.source][edge.target] = edge.weight
        for source in self.graph.iternodes():
            self.weights[source] = dict(self.dist[source])

    def run(self):
        """Executable pseudocode."""
        for m in xrange(2, self.graph.v()):   # |V|-2 times
            self.dist = self.extended_shortest_paths(self.dist)
        if any(self.dist[node][node] < 0 for node in self.graph.iternodes()):
            raise ValueError("negative cycle")

    def extended_shortest_paths(self, old_dist):
        """O(V**3) time."""
        new_dist = dict()
        for source in self.graph.iternodes():
            new_dist[source] = dict()
            for target in self.graph.iternodes():
                new_dist[source][target] = float("inf")
                for node in self.graph.iternodes():
                    new_dist[source][target] = min(new_dist[source][target],
                        old_dist[source][node] + self.weights[node][target])
        return new_dist


class SlowAllPairsEdges:
    """O(V**2 (V+E)) time."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("graph is not directed")
        self.graph = graph
        self.dist = dict()
        self.weights = dict()
        for source in self.graph.iternodes():   # O(V**2) time
            self.dist[source] = dict()
            for target in self.graph.iternodes():
                self.dist[source][target] = float("inf")
            self.dist[source][source] = 0
        for edge in self.graph.iteredges():   # O(E) time
            self.dist[edge.source][edge.target] = edge.weight
        for source in self.graph.iternodes():
            self.weights[source] = dict(self.dist[source])

    def run(self):
        """Executable pseudocode."""
        for m in xrange(2, self.graph.v()):   # |V|-2 times
            self.dist = self.extended_shortest_paths(self.dist)
        if any(self.dist[node][node] < 0 for node in self.graph.iternodes()):
            raise ValueError("negative cycle")

    def extended_shortest_paths(self, old_dist):
        """O(V*(V+E)) time."""
        new_dist = dict()
        for source in self.graph.iternodes():   # |V| times
            new_dist[source] = dict(old_dist[source]) # IMPORTANT, O(V)
            for edge in self.graph.iteredges():   # O(E) time
                new_dist[source][edge.target] = min(
                    new_dist[source][edge.target],
                    old_dist[source][edge.source] + edge.weight)
        return new_dist


class SlowAllPairsWithPaths:   # not for FasterAllPairsSP
    """O(V**4) time."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("graph is not directed")
        self.graph = graph
        self.dist = dict()
        self.weights = dict()
        self.prev = dict()
        for source in self.graph.iternodes():   # O(V**2) time
            self.dist[source] = dict()
            self.prev[source] = dict()
            for target in self.graph.iternodes():
                self.dist[source][target] = float("inf")
                self.prev[source][target] = None
            self.dist[source][source] = 0
        for edge in self.graph.iteredges():   # O(E) time
            self.dist[edge.source][edge.target] = edge.weight
            self.prev[edge.source][edge.target] = edge.source
        for source in self.graph.iternodes():
            self.weights[source] = dict(self.dist[source])

    def run(self):
        """Executable pseudocode."""
        for m in xrange(2, self.graph.v()):   # |V|-2 times
            self.dist = self.extended_shortest_paths(self.dist)
        if any(self.dist[node][node] < 0 for node in self.graph.iternodes()):
            raise ValueError("negative cycle")

    def extended_shortest_paths(self, old_dist):
        """O(V**3) time."""
        new_dist = dict()
        for source in self.graph.iternodes():
            new_dist[source] = dict(old_dist[source]) # IMPORTANT, copy
            for target in self.graph.iternodes():
                for node in self.graph.iternodes():
                    alt = old_dist[source][node] + self.weights[node][target]
                    if new_dist[source][target] > alt:
                        new_dist[source][target] = alt
                        self.prev[source][target] = node
        return new_dist


class FasterAllPairs:
    """O(V**3 log V) time."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("graph is not directed")
        self.graph = graph
        self.dist = dict()
        for source in self.graph.iternodes():   # O(V**2) time
            self.dist[source] = dict()
            for target in self.graph.iternodes():
                self.dist[source][target] = float("inf") # IMPORTANT
            self.dist[source][source] = 0
        for edge in self.graph.iteredges():   # O(E) time
            self.dist[edge.source][edge.target] = edge.weight

    def run(self):
        """Executable pseudocode."""
        m = 1
        while m < (self.graph.v() - 1):   # log(V) times
            self.dist = self.extended_shortest_paths(self.dist)
            m = 2 * m
        if any(self.dist[node][node] < 0 for node in self.graph.iternodes()):
            raise ValueError("negative cycle")

    def extended_shortest_paths(self, old_dist):
        """O(V**3) time."""
        new_dist = dict()
        for source in self.graph.iternodes():
            new_dist[source] = dict()
            for target in self.graph.iternodes():
                new_dist[source][target] = float("inf")
                for node in self.graph.iternodes():
                    new_dist[source][target] = min(new_dist[source][target],
                        old_dist[source][node] + old_dist[node][target])
        return new_dist

# EOF
