#!/usr/bin/python
#
# bfs.py
#
# Breadth-First Search.

from edges import Edge
from Queue import Queue


class BFSWithQueue:

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.tree = graph.__class__(self.graph.v()) # spanning tree
        self.color = dict(((node, "WHITE") for node in self.graph.iternodes()))
        self.dist = dict(((node, float("inf")) for node in self.graph.iternodes()))
        self.prev = dict(((node, None) for node in self.graph.iternodes()))

    def run(self, source=None, action=None):
        """Executable pseudocode."""
        if source is not None:
            self.visit(source, action)
        else:
            for node in self.graph.iternodes():
                if self.color[node] == "WHITE":
                    self.visit(node, action)
        # budujemy spanning tree
        for node in self.graph.iternodes():
            if self.prev[node] is not None:
                # krawedz drzewowa (parent, node)
                self.tree.add_edge(Edge(self.prev[node], node))

    def visit(self, node, action=None):
        """Explore the connected component."""
        self.color[node] = "GREY"
        self.dist[node] = 0
        self.prev[node] = None
        if action:
            action(node)
        Q = Queue()
        Q.put(node)  # do kolejki ida szare
        while not Q.empty():
            source = Q.get()
            for target in self.graph.iteradjacent(source):
                if self.color[target] == "WHITE":
                    self.color[target] = "GREY"
                    self.dist[target] = self.dist[source] + 1
                    self.prev[target] = source
                    if action:
                        action(target)
                    Q.put(target)  # do kolejki ida szare
            self.color[source] = "BLACK"

    def to_dag(self):
        """Returns the spanning tree as a dag."""
        dag = graph.__class__(self.graph.v(), directed=True)
        for node in self.graph.iternodes():
            if self.prev[node] is not None:
                # Edge(parent, node), out-tree
                dag.add_edge(Edge(self.prev[node], node))
        return dag

# EOF
