#!/usr/bin/python
#
# bfs.py
#
# Breadth First Search.

from edges import Edge
from graphs import Graph
from Queue import Queue


class BFSWithQueue:

    def __init__(self, graph):
        self.graph = graph
        self.color = dict(((node, "WHITE") for node in self.graph.iternodes()))
        self.dist = dict(((node, float("inf")) for node in self.graph.iternodes()))
        self.prev = dict(((node, None) for node in self.graph.iternodes()))
        self.tree = Graph()   # spanning tree

    def run(self, source=None, action=None):
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
        # Graf poprzednikow (skierowany).
        dag = Graph(directed=True)
        for node in self.graph.iternodes():
            if self.prev[node] is not None:
                # Edge(parent, node)
                dag.add_edge(Edge(self.prev[node], node))
        return dag

# EOF
