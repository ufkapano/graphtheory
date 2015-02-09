#!/usr/bin/python
#
# topsort.py
#
# Topological sorting of nodes from a dag.

from edges import Edge
from graphs import Graph
from Queue import Queue
#from dfs import DFSWithRecursion as SimpleDFS
from dfs import SimpleDFS


class TopologicalSortDFS:
    """Topological sorting of nodes from a dag."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.sorted_nodes = []

    def run(self):
        """Executable pseudocode."""
        algorithm = SimpleDFS(self.graph)
        algorithm.run(post_action=lambda node: self.sorted_nodes.append(node))
        self.sorted_nodes.reverse()


class TopologicalSortQueue:
    """Topological sorting of nodes from a dag."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.sorted_nodes = []

    def run(self):
        """Executable pseudocode."""
        Q = Queue()   # queue or stack or set
        # Calculate indegree of nodes.
        inedges = dict((node, 0) for node in self.graph.iternodes())
        for edge in self.graph.iteredges():
            inedges[edge.target] = inedges[edge.target] + 1
        for node in self.graph.iternodes():
            if inedges[node] == 0:
                Q.put(node)
        while not Q.empty():
            node = Q.get()
            self.sorted_nodes.append(node)
            # Remove all outedges.
            for target in self.graph.iteradjacent(node):
                inedges[target] = inedges[target]-1
                if inedges[target] == 0:
                    Q.put(target)


class TopologicalSortSet:
    """Topological sorting of nodes from a dag."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.sorted_nodes = []

    def run(self):
        """Executable pseudocode."""
        Q = set()   # queue or stack or set
        # Calculate indegree of nodes.
        inedges = dict((node, 0) for node in self.graph.iternodes())
        for edge in self.graph.iteredges():
            inedges[edge.target] = inedges[edge.target] + 1
        for node in self.graph.iternodes():
            if inedges[node] == 0:
                Q.add(node)
        while Q:
            node = Q.pop()
            self.sorted_nodes.append(node)
            # Remove all outedges.
            for target in self.graph.iteradjacent(node):
                inedges[target] = inedges[target]-1
                if inedges[target] == 0:
                    Q.add(target)

# EOF
