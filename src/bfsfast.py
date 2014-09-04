#!/usr/bin/python

from edges import Edge
from collections import deque


class BFSWithQueue:
    """Breadth-First Search."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.color = dict(((node, "WHITE") for node in self.graph.iternodes()))
        self.dist = dict(((node, float("inf")) for node in self.graph.iternodes()))
        self.prev = dict(((node, None) for node in self.graph.iternodes()))

    def run(self, source=None, pre_action=None, post_action=None):
        """Executable pseudocode."""
        if source is not None:
            self.visit(source, pre_action, post_action)
        else:
            for node in self.graph.iternodes():
                if self.color[node] == "WHITE":
                    self.visit(node, pre_action, post_action)

    def visit(self, node, pre_action=None, post_action=None):
        """Explore the connected component."""
        self.color[node] = "GREY"
        self.dist[node] = 0
        self.prev[node] = None
        Q = deque()
        Q.append(node)  # node is GREY
        if pre_action:   # when Q.append
            pre_action(node)
        while len(Q) > 0:
            source = Q.popleft()
            for target in self.graph.iteradjacent(source):
                if self.color[target] == "WHITE":
                    self.color[target] = "GREY"
                    self.dist[target] = self.dist[source] + 1
                    self.prev[target] = source
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
            if self.prev[node] is not None:
                # tree edge (parent, node)
                tree.add_edge(Edge(self.prev[node], node))
        return tree

    def to_dag(self):
        """Returns the spanning tree as a dag."""
        dag = self.graph.__class__(self.graph.v(), directed=True)
        for node in self.graph.iternodes():
            if self.prev[node] is not None:
                # Edge(parent, node), out-tree
                dag.add_edge(Edge(self.prev[node], node))
        return dag


class SimpleBFS:
    """Breadth-First Search."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.prev = dict()

    def run(self, source=None, pre_action=None, post_action=None):
        """Executable pseudocode."""
        if source is not None:
            self.visit(source, pre_action, post_action)
        else:
            for node in self.graph.iternodes():
                if node not in self.prev:
                    self.visit(node, pre_action, post_action)

    def visit(self, node, pre_action=None, post_action=None):
        """Explore the connected component."""
        Q = deque()
        self.prev[node] = None   # before Q.append
        Q.append(node)
        if pre_action:   # when Q.append
            pre_action(node)
        while len(Q) > 0:
            source = Q.popleft()
            for target in self.graph.iteradjacent(source):
                if target not in self.prev:
                    self.prev[target] = source   # before Q.append
                    Q.append(target)
                    if pre_action:   # when Q.append
                        pre_action(target)
            if post_action:
                post_action(source)

    def to_tree(self):
        """The spanning tree is built."""
        tree = self.graph.__class__(self.graph.v(), directed=False)
        for node in self.graph.iternodes():
            if self.prev[node] is not None:
                # tree edge (parent, node)
                tree.add_edge(Edge(self.prev[node], node))
        return tree

    def to_dag(self):
        """Returns the spanning tree as a dag."""
        dag = self.graph.__class__(self.graph.v(), directed=True)
        for node in self.graph.iternodes():
            if self.prev[node] is not None:
                # Edge(parent, node), out-tree
                dag.add_edge(Edge(self.prev[node], node))
        return dag

# EOF
