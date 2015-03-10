#!/usr/bin/python

from edges import Edge
from Queue import Queue


class BFSWithQueue:
    """Breadth-First Search."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.color = dict(((node, "WHITE") for node in self.graph.iternodes()))
        self.distance = dict(((node, float("inf")) for node in self.graph.iternodes()))
        self.parent = dict(((node, None) for node in self.graph.iternodes()))
        self.dag = self.graph.__class__(self.graph.v(), directed=True)

    def run(self, source=None, pre_action=None, post_action=None):
        """Executable pseudocode."""
        if source is not None:
            self._visit(source, pre_action, post_action)
        else:
            for node in self.graph.iternodes():
                if self.color[node] == "WHITE":
                    self._visit(node, pre_action, post_action)

    def _visit(self, node, pre_action=None, post_action=None):
        """Explore the connected component."""
        self.color[node] = "GREY"
        self.distance[node] = 0
        self.parent[node] = None
        Q = Queue()
        Q.put(node)  # node is GREY
        if pre_action:   # when Q.put
            pre_action(node)
        while not Q.empty():
            source = Q.get()
            for edge in self.graph.iteroutedges(source):
                if self.color[edge.target] == "WHITE":
                    self.color[edge.target] = "GREY"
                    self.distance[edge.target] = self.distance[source] + 1
                    self.parent[edge.target] = source
                    self.dag.add_edge(edge)
                    Q.put(edge.target)  # target is GREY
                    if pre_action:   # when Q.put
                        pre_action(edge.target)
            self.color[source] = "BLACK"
            if post_action:   # source became BLACK
                post_action(source)

    def path(self, source, target):
        """Construct a path from source to target."""
        if source == target:
            return [source]
        elif self.parent[target] is None:
            raise ValueError("no path to target")
        else:
            return self.path(source, self.parent[target]) + [target]


class SimpleBFS:
    """Breadth-First Search."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.parent = dict()
        self.dag = self.graph.__class__(self.graph.v(), directed=True)

    def run(self, source=None, pre_action=None, post_action=None):
        """Executable pseudocode."""
        if source is not None:
            self._visit(source, pre_action, post_action)
        else:
            for node in self.graph.iternodes():
                if node not in self.parent:
                    self._visit(node, pre_action, post_action)

    def _visit(self, node, pre_action=None, post_action=None):
        """Explore the connected component."""
        Q = Queue()
        self.parent[node] = None   # before Q.put
        Q.put(node)
        if pre_action:   # when Q.put
            pre_action(node)
        while not Q.empty():
            source = Q.get()
            for edge in self.graph.iteroutedges(source):
                if edge.target not in self.parent:
                    self.parent[edge.target] = source   # before Q.put
                    self.dag.add_edge(edge)
                    Q.put(edge.target)
                    if pre_action:   # when Q.put
                        pre_action(edge.target)
            if post_action:
                post_action(source)

    def path(self, source, target):
        """Construct a path from source to target."""
        if source == target:
            return [source]
        elif self.parent[target] is None:
            raise ValueError("no path to target")
        else:
            return self.path(source, self.parent[target]) + [target]

# EOF
