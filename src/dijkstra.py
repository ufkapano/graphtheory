#!/usr/bin/python
#
# dijkstra.py
#
# The Dijkstra's algorithm.

from edges import Edge
from graphs import Graph
from Queue import PriorityQueue


class Dijkstra:
    """The Dijkstra's algorithm for the shortest path problem."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.dist = dict((node, float("inf")) for node in self.graph.iternodes())
        # shortest path tree
        self.prev = dict((node, None) for node in self.graph.iternodes())
        self.in_queue = dict((node, True) for node in self.graph.iternodes())
        self.pq = PriorityQueue()

    def run(self, source):
        """Executable pseudocode."""
        self.source = source
        self.dist[source] = 0
        for node in self.graph.iternodes():
            self.pq.put((self.dist[node], node))
        while not self.pq.empty():
            pri, node = self.pq.get()
            if self.in_queue[node]:
                self.in_queue[node] = False
            else:
                continue
            for edge in self.graph.iteroutedges(node):
                if self.in_queue[edge.target] and self.relax(edge):
                    self.pq.put((self.dist[edge.target], edge.target))

    def relax(self, edge):
        """Edge relaxation."""
        alt = self.dist[edge.source] + edge.weight
        if self.dist[edge.target] > alt:
            self.dist[edge.target] = alt
            self.prev[edge.target] = edge.source
            return True
        return False

    def path_to(self, target):
        """Construct a path from source to target."""
        if self.source == target:
            return [self.source]
        elif self.prev[target] is None:
            raise Exception("no path to node")
        else:
            return self.path_to(self.prev[target]) + [target]


class DijkstraMatrix:
    """The Dijkstra's algorithm with O(V**2) time."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.dist = dict((node, float("inf")) for node in self.graph.iternodes())
        # shortest path tree
        self.prev = dict((node, None) for node in self.graph.iternodes())
        self.in_queue = dict((node, True) for node in self.graph.iternodes())

    def run(self, source):
        """Executable pseudocode."""
        self.source = source
        self.dist[source] = 0
        for step in xrange(self.graph.v()):   # |V| times
            # find min node - O(V) time
            node = min((node for node in self.graph.iternodes() 
                if self.in_queue[node]), key=self.dist.get)
            self.in_queue[node] = False
            for edge in self.graph.iteroutedges(node):   # O(V) time
                if self.in_queue[edge.target]:
                    self.relax(edge)

    def relax(self, edge):
        """Edge relaxation."""
        alt = self.dist[edge.source] + edge.weight
        if self.dist[edge.target] > alt:
            self.dist[edge.target] = alt
            self.prev[edge.target] = edge.source
            return True
        return False

    def path_to(self, target):
        """Construct a path from source to target."""
        if self.source == target:
            return [self.source]
        elif self.prev[target] is None:
            raise Exception("no path to node")
        else:
            return self.path_to(self.prev[target]) + [target]

# EOF
