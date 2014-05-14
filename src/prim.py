#!/usr/bin/python
#
# prim.py
#
# Prim's algorithm for finding MST.

from edges import Edge
from graphs import Graph
from Queue import PriorityQueue


class PrimMST:
    """Prim's algorithm for finding MST."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.dist = dict((node, float("inf")) for node in self.graph.iternodes())
        self.prev = dict((node, None) for node in self.graph.iternodes()) # MST as a dict
        self.in_queue = dict((node, True) for node in self.graph.iternodes())
        self.mst = Graph()   # MST as a graph
        self.pq = PriorityQueue()

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:   # get first random node
            source = self.graph.iternodes().next()
        self.source = source
        self.dist[source] = 0
        for node in self.graph.iternodes():
            self.pq.put((self.dist[node], node))
        while not self.pq.empty():
            weight, node = self.pq.get()
            if self.in_queue[node]:
                self.in_queue[node] = False
            else:
                continue
            for edge in self.graph.iteroutedges(node):
                if (self.in_queue[edge.target] 
                and edge.weight < self.dist[edge.target]):
                    self.dist[edge.target] = edge.weight
                    self.prev[edge.target] = edge.source
                    # DECREASE-KEY
                    self.pq.put((edge.weight, edge.target))
        for node in self.graph.iternodes():   # O(V) time
            if self.prev[node] is not None:
                self.mst.add_edge(Edge(self.prev[node], node, self.dist[node]))


class PrimMatrixMST:
    """Prim's algorithm for finding MST in O(V**2) time."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.dist = dict((node, float("inf")) for node in self.graph.iternodes())
        self.prev = dict((node, None) for node in self.graph.iternodes()) # MST as a dict
        self.in_queue = dict((node, True) for node in self.graph.iternodes())
        self.mst = Graph()   # MST as a graph

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:   # get first random node
            source = self.graph.iternodes().next()
        self.source = source
        self.dist[source] = 0
        for step in xrange(self.graph.v()):    # |V| times
            # find min node in the graph - O(V) time
            node = min((node for node in self.graph.iternodes() 
            if self.in_queue[node]), key=self.dist.get)
            self.in_queue[node] = False
            for edge in self.graph.iteroutedges(node):  # O(V) time
                if (self.in_queue[edge.target] 
                and edge.weight < self.dist[edge.target]):
                    self.dist[edge.target] = edge.weight
                    self.prev[edge.target] = edge.source
        for node in self.graph.iternodes():   # O(V) time
            if self.prev[node] is not None:
                self.mst.add_edge(Edge(self.prev[node], node, self.dist[node]))

# EOF
