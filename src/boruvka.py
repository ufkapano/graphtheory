#!/usr/bin/python
#
# boruvka.py
#
# Boruvka's algorithm for finding MST.

from edges import Edge
from graphs import Graph
from unionfind import UnionFind


class BoruvkaMST:
    """Boruvka's algorithm for finding MST."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.mst = Graph()   # MST is a graph
        self.uf = UnionFind()

    def find_cheapest_edge(self, source):
        """Find the cheapest edge from the component to outside."""
        min_edge = Edge(None, None, float("inf"))
        source = self.uf.find(source)
        for edge in self.graph.iteredges():
            if ((self.uf.find(edge.source) == source) 
            == (self.uf.find(edge.target) != source)):
                # edge to a node outside of the component
                if edge < min_edge:
                    min_edge = edge
        return min_edge

    def run(self):
        """Executable pseudocode."""
        for node in self.graph.iternodes():
            self.uf.create(node)
        forest = set(node for node in self.graph.iternodes())
        while len(forest) > 1:
            new_edges = []
            for node in forest:  # total time O(V*E)
                edge = self.find_cheapest_edge(node)
                new_edges.append(edge)
            # Connecting components.
            forest = set()
            for edge in new_edges:
                source = self.uf.find(edge.source)
                target = self.uf.find(edge.target)
                if source != target:
                    self.uf.union(source, target)
                    forest.add(self.uf.find(source))
                    self.mst.add_edge(edge)
            # remove duplicates, total time O(V)
            forest = set(self.uf.find(node) for node in forest)

# EOF
