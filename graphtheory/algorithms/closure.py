#!/usr/bin/env python3

#from graphtheory.traversing.bfs import BFSWithQueue as SimpleBFS
from graphtheory.traversing.bfs import SimpleBFS

#from graphtheory.traversing.dfs import DFSWithStack as SimpleDFS
#from graphtheory.traversing.dfs import DFSWithRecursion as SimpleDFS
from graphtheory.traversing.dfs import SimpleDFS


class TransitiveClosureSimple:
    """Based on the matrix multiplication, O(V^2 E) time."""

    def __init__(self, graph):
        """The algorithm initialization, O(V^2) time."""
        if not graph.is_directed():
            raise ValueError("the graph is not directed")
        self.graph = graph
        self.T = dict()
        for source in self.graph.iternodes():
            self.T[source] = dict()
            for target in self.graph.iternodes():
                self.T[source][target] = False
            self.T[source][source] = True

    def run(self):
        """Executable pseudocode."""
        for step in range(1, self.graph.v()):   # |V|-1 times
            for node in self.graph.iternodes():
                for edge in self.graph.iteredges():
                    self.T[node][edge.target] = (
                        self.T[node][edge.target] or
                        self.T[node][edge.source])


class TransitiveClosure:
    """Based on the Floyd-Warshall algorithm, O(V^3) time."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("the graph is not directed")
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


class TransitiveClosureBFS:
    """Based on the BFS, O(V*(V+E)) time."""

    def __init__(self, graph):
        """The algorithm initialization, O(V^2) time."""
        if not graph.is_directed():
            raise ValueError("the graph is not directed")
        self.graph = graph
        self.T = dict()
        for source in self.graph.iternodes():
            self.T[source] = dict()
            for target in self.graph.iternodes():
                self.T[source][target] = False
            self.T[source][source] = True

    def run(self):
        """Executable pseudocode."""
        for source in self.graph.iternodes():
            algorithm = SimpleBFS(self.graph)
            algorithm.run(source, pre_action=lambda node:
                self.T[source].__setitem__(node, True))


class TransitiveClosureDFS:
    """Based on the DFS, O(V*(V+E)) time."""

    def __init__(self, graph):
        """The algorithm initialization, O(V^2) time."""
        if not graph.is_directed():
            raise ValueError("the graph is not directed")
        self.graph = graph
        self.T = dict()
        for source in self.graph.iternodes():
            self.T[source] = dict()
            for target in self.graph.iternodes():
                self.T[source][target] = False
            self.T[source][source] = True

    def run(self):
        """Executable pseudocode."""
        for source in self.graph.iternodes():
            algorithm = SimpleDFS(self.graph)
            algorithm.run(source, pre_action=lambda node:
                self.T[source].__setitem__(node, True))

# EOF
