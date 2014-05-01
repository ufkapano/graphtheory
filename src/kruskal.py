#!/usr/bin/python
#
# kruskal.py
#
# Kruskal's algorithm for finding MST.

from edges import Edge
from graphs import Graph
from unionfind import UnionFind
from Queue import PriorityQueue


class KruskalMST:
    """Kruskal's algorithm for finding MST."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.mst = Graph()   # MST is a graph
        self.uf = UnionFind()
        self.pq = PriorityQueue()

    def run(self):
        """Executable pseudocode."""
        for node in self.graph.iternodes():
            self.uf.create(node)
        for edge in self.graph.iteredges():
            self.pq.put((edge.weight, edge))
        while not self.pq.empty():
            weight, edge = self.pq.get()
            if self.uf.find(edge.source) != self.uf.find(edge.target):
                self.uf.union(edge.source, edge.target)
                self.mst.add_edge(edge)

# EOF
