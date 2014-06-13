#!/usr/bin/python

class TransitiveClosure:

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
