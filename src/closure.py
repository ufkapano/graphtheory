#! /usr/bin/python

class TransitiveClosureSimple:
    """Based on the matrix multiplication, O(V**2 E) time."""

    def __init__(self, graph):
        """The algorithm initialization, O(V**2) time."""
        if not graph.is_directed():
            raise ValueError("graph is not directed")
        self.graph = graph
        self.T = dict()
        for source in self.graph.iternodes():
            self.T[source] = dict()
            for target in self.graph.iternodes():
                self.T[source][target] = False
            self.T[source][source] = True

    def run(self):
        """Executable pseudocode."""
        for step in range(1, self.graph.v()):
            for node in self.graph.iternodes():
                for edge in self.graph.iteredges():
                    self.T[node][edge.target] = (
                    self.T[node][edge.target] or self.T[node][edge.source])


class TransitiveClosure:
    """Based on the Floyd-Warshall algorithm, O(V**3) time."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("graph is not directed")
        self.graph = graph
        self.T = dict()
        for source in self.graph.iternodes():
            self.T[source] = dict()
            for target in self.graph.iternodes():
                self.T[source][target] = False
            self.T[source][source] = True
        for edge in self.graph.iteredges():
            self.T[edge.source][edge.target] = True

    def run(self):
        """Executable pseudocode."""
        for node in self.graph.iternodes():
            for source in self.graph.iternodes():
                for target in self.graph.iternodes():
                    self.T[source][target] = self.T[source][target] or (
                        self.T[source][node] and self.T[node][target])

# EOF
