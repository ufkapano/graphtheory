#!/usr/bin/python
#
# topsort.py
#
# Topological sorting of nodes from a dag.

from edges import Edge
from graphs import Graph
from Queue import Queue


class TopologicalSort:

    def __init__(self, graph):
        self.graph = graph
        self.in_edges = dict((node, 0) for node in self.graph.iternodes())
        self.sorted_nodes = []
        self.Q = Queue()

    def run(self):
        # Calculate indegree of nodes.
        for edge in self.graph.iteredges():
            self.in_edges[edge.target] = self.in_edges[edge.target] + 1
        for node in self.graph.iternodes():
            if self.in_edges[node] == 0:
                self.Q.put(node)
        while not self.Q.empty():
            node = self.Q.get()
            self.sorted_nodes.append(node)
            # Remove all outedges.
            for target in self.graph.iteradjacent(node):
                self.in_edges[target] = self.in_edges[target]-1
                if self.in_edges[target] == 0:
                    self.Q.put(target)

# EOF
