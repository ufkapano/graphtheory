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

    def run(self):
        """Executable pseudocode."""
        for node in self.graph.iternodes():
            self.uf.create(node)
        forest = set(node for node in self.graph.iternodes())
        dummy_edge = Edge(None, None, float("inf"))
        while len(forest) > 1:
            min_edges = dict(((node, dummy_edge) for node in forest))
            # finding the cheapest eadges
            for edge in self.graph.iteredges(): # O(E) time
                source = self.uf.find(edge.source)
                target = self.uf.find(edge.target)
                if source != target:   # different components
                    if edge < min_edges[source]:
                        min_edges[source] = edge
                    if edge < min_edges[target]:
                        min_edges[target] = edge
            # connecting components, total time is O(V)
            forest = set()
            for edge in min_edges.itervalues():
                source = self.uf.find(edge.source)
                target = self.uf.find(edge.target)
                if source != target:   # different components
                    self.uf.union(source, target)
                    forest.add(source)
                    self.mst.add_edge(edge)
            # remove duplicates, total time is O(V)
            forest = set(self.uf.find(node) for node in forest)

# EOF
