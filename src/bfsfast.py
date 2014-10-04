#!/usr/bin/python

from edges import Edge
from collections import deque


class BFSWithQueue:
    """Breadth-First Search."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.color = dict(((node, "WHITE") for node in self.graph.iternodes()))
        self.distance = dict(((node, float("inf")) for node in self.graph.iternodes()))
        self.parent = dict(((node, None) for node in self.graph.iternodes()))

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
        Q = deque()
        Q.append(node)  # node is GREY
        if pre_action:   # when Q.append
            pre_action(node)
        while len(Q) > 0:
            source = Q.popleft()
            for target in self.graph.iteradjacent(source):
                if self.color[target] == "WHITE":
                    self.color[target] = "GREY"
                    self.distance[target] = self.distance[source] + 1
                    self.parent[target] = source
                    Q.append(target)  # target is GREY
                    if pre_action:   # when Q.append
                        pre_action(target)
            self.color[source] = "BLACK"
            if post_action:   # source became BLACK
                post_action(source)

    def to_tree(self):
        """The spanning tree is built."""
        tree = self.graph.__class__(self.graph.v(), directed=False)
        for node in self.graph.iternodes():
            if self.parent[node] is not None:
                tree.add_edge(Edge(self.parent[node], node))
        return tree

    def to_dag(self):
        """Returns the spanning tree as a dag."""
        dag = self.graph.__class__(self.graph.v(), directed=True)
        for node in self.graph.iternodes():
            if self.parent[node] is not None:
                dag.add_edge(Edge(self.parent[node], node))
        return dag


class SimpleBFS:
    """Breadth-First Search."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.parent = dict()

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
        Q = deque()
        self.parent[node] = None   # before Q.append
        Q.append(node)
        if pre_action:   # when Q.append
            pre_action(node)
        while len(Q) > 0:
            source = Q.popleft()
            for target in self.graph.iteradjacent(source):
                if target not in self.parent:
                    self.parent[target] = source   # before Q.append
                    Q.append(target)
                    if pre_action:   # when Q.append
                        pre_action(target)
            if post_action:
                post_action(source)

    def to_tree(self):
        """The spanning tree is built."""
        tree = self.graph.__class__(self.graph.v(), directed=False)
        for node in self.graph.iternodes():
            if self.parent[node] is not None:
                tree.add_edge(Edge(self.parent[node], node))
        return tree

    def to_dag(self):
        """Returns the spanning tree as a dag."""
        dag = self.graph.__class__(self.graph.v(), directed=True)
        for node in self.graph.iternodes():
            if self.parent[node] is not None:
                dag.add_edge(Edge(self.parent[node], node))
        return dag

# EOF
