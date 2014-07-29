#!/usr/bin/python

from dfs import SimpleDFS
from bfs import SimpleBFS


class FleuryDFS:
    """Fleury's algorithm for finding an Eulerian cycle."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:   # get first random node
            source = self.graph.iternodes().next()
        node = source
        self.euler_cycle = [node]
        self.graph_copy = self.graph.copy()
        while list(self.graph_copy.iteradjacent(node)):
            for edge in list(self.graph_copy.iteroutedges(node)):
                if not self.is_bridge(edge):
                    break
            self.graph_copy.del_edge(edge)
            self.euler_cycle.append(edge.target)
            node = edge.target

    def is_bridge(self, edge):
        """Bridge test."""
        dfs = SimpleDFS(self.graph_copy)
        list1 = list()
        list2 = list()
        dfs.run(edge.source, pre_action=lambda node: list1.append(node))
        self.graph_copy.del_edge(edge)
        dfs.run(edge.source, pre_action=lambda node: list2.append(node))
        self.graph_copy.add_edge(edge)
        return len(list1) != len(list2)


class FleuryBFS:
    """Fleury's algorithm for finding an Eulerian cycle."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:   # get first random node
            source = self.graph.iternodes().next()
        node = source
        self.euler_cycle = [node]
        self.graph_copy = self.graph.copy()
        while list(self.graph_copy.iteradjacent(node)):
            for edge in list(self.graph_copy.iteroutedges(node)):
                if not self.is_bridge(edge):
                    break
            self.graph_copy.del_edge(edge)
            self.euler_cycle.append(edge.target)
            node = edge.target

    def is_bridge(self, edge):
        """Bridge test."""
        dfs = SimpleBFS(self.graph_copy)
        list1 = list()
        list2 = list()
        dfs.run(edge.source, pre_action=lambda node: list1.append(node))
        self.graph_copy.del_edge(edge)
        dfs.run(edge.source, pre_action=lambda node: list2.append(node))
        self.graph_copy.add_edge(edge)
        return len(list1) != len(list2)

# EOF
