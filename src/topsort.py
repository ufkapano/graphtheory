#!/usr/bin/python
#
# topsort.py
#
# Topological sorting of nodes from a dag.

from edges import Edge
from graphs import Graph
from Queue import Queue
#from dfs import DFSWithRecursion
from dfs import SimpleDFS as DFSWithRecursion


class TopologicalSortDFS:
    """Topological sorting of nodes from a dag."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.sorted_nodes = []

    def run(self):
        """Executable pseudocode."""
        algorythm = DFSWithRecursion(self.graph)
        algorythm.run(post_action=lambda node: self.sorted_nodes.append(node))
        self.sorted_nodes.reverse()


class TopologicalSortQueue:
    """Topological sorting of nodes from a dag."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.sorted_nodes = []
        self.inedges = dict((node, 0) for node in self.graph.iternodes())
        self.Q = Queue()   # queue or stack or set

    def run(self):
        """Executable pseudocode."""
        # Calculate indegree of nodes.
        for edge in self.graph.iteredges():
            self.inedges[edge.target] = self.inedges[edge.target] + 1
        for node in self.graph.iternodes():
            if self.inedges[node] == 0:
                self.Q.put(node)
        while not self.Q.empty():
            node = self.Q.get()
            self.sorted_nodes.append(node)
            # Remove all outedges.
            for target in self.graph.iteradjacent(node):
                self.inedges[target] = self.inedges[target]-1
                if self.inedges[target] == 0:
                    self.Q.put(target)


class TopologicalSortSet:
    """Topological sorting of nodes from a dag."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.sorted_nodes = []
        self.inedges = dict((node, 0) for node in self.graph.iternodes())
        self.Q = set()   # queue or stack or set

    def run(self):
        """Executable pseudocode."""
        # Calculate indegree of nodes.
        for edge in self.graph.iteredges():
            self.inedges[edge.target] = self.inedges[edge.target] + 1
        for node in self.graph.iternodes():
            if self.inedges[node] == 0:
                self.Q.add(node)
        while self.Q:
            node = self.Q.pop()
            self.sorted_nodes.append(node)
            # Remove all outedges.
            for target in self.graph.iteradjacent(node):
                self.inedges[target] = self.inedges[target]-1
                if self.inedges[target] == 0:
                    self.Q.add(target)

# EOF
