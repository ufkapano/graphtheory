#!/usr/bin/python
#
# dfs.py
#

from edges import Edge
from graphs import Graph
from Queue import LifoQueue


class DFSWithStack:

    def __init__(self, graph):
        self.graph = graph
        self.color = dict(((node, "WHITE") for node in self.graph.iternodes()))
        self.prev = dict(((node, None) for node in self.graph.iternodes()))
        self.time = 0    # time stamp
        self.dd = dict()
        self.ff = dict()
        self.tree = Graph()   # undirected graph

    def run(self, source=None, pre_action=None, post_action=None):
        if source is not None:
            self.visit(source, pre_action, post_action)
        else:
            for node in self.graph.iternodes():
                if self.color[node] == "WHITE":
                    self.dfs_visit(node, pre_action, post_action)
        for node in self.graph.iternodes():
            if self.prev[node] is not None:
                # Edge(parent, node)
                self.tree.add_edge(Edge(self.prev[node], node))

    def visit(self, node, pre_action=None, post_action=None):
        self.time = self.time + 1
        self.dd[node] = self.time
        self.color[node] = "GREY"
        if pre_action:
            pre_action(node)
        Q = LifoQueue()
        Q.put(node)   # na stos ida szare
        while not Q.empty():
            source = Q.get()    # przetwarzam szary node
            for target in self.graph.iteradjacent(source):
                if self.color[target] == "WHITE":
                    self.prev[target] = source
                    self.time = self.time + 1
                    self.dd[target] = self.time
                    self.color[target] = "GREY"
                    if pre_action:
                        pre_action(target)
                    Q.put(target)
            self.time = self.time + 1
            self.ff[source] = self.time
            self.color[source] = "BLACK"
            if post_action:
                post_action(source)

    def to_dag(self):
        dag = Graph(directed=True)
        for node in self.graph.iternodes():
            if self.prev[node] is not None:
                # Edge(parent, node)
                dag.add_edge(Edge(self.prev[node], node))
        return dag

#=====================================================================

class DFSWithRecursion:

    def __init__(self, graph):
        self.graph = graph
        self.color = dict(((node, "WHITE") for node in self.graph.iternodes()))
        self.prev = dict(((node, None) for node in self.graph.iternodes()))
        self.time = 0    # time stamp
        self.dd = dict()
        self.ff = dict()
        self.tree = Graph()   # graf nieskierowany
        # ciekawe ustawianie rekurencji
        import sys
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v()*2, recursionlimit))

    def run(self, source=None, pre_action=None, post_action=None):
        if source is not None:
            self.visit(source, pre_action, post_action)
        else:
            for node in self.graph.iternodes():
                if self.color[node] == "WHITE":
                    self.dfs_visit(node, pre_action, post_action)
        for node in self.graph.iternodes():
            if self.prev[node] is not None:
                # Edge(parent, node)
                self.tree.add_edge(Edge(self.prev[node], node))

    def visit(self, node, pre_action=None, post_action=None):
        self.time = self.time + 1
        self.dd[node] = self.time
        self.color[node] = "GREY"
        if pre_action:
            pre_action(node)
        for target in self.graph.iteradjacent(node):
            if self.color[target] == "WHITE":
                self.prev[target] = node
                self.visit(target, pre_action, post_action)
        self.time = self.time + 1
        self.ff[node] = self.time
        self.color[node] = "BLACK"
        if post_action:
            post_action(node)

    def to_dag(self):
        dag = Graph(directed=True)
        for node in self.graph.iternodes():
            if self.prev[node] is not None:
                # Edge(parent, node)
                dag.add_edge(Edge(self.prev[node], node))
        return dag

# EOF
