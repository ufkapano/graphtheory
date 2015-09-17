#!/usr/bin/python

from Queue import PriorityQueue


class Dijkstra:
    """The Dijkstra's algorithm for the shortest path problem."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("the graph is not directed")
        self.graph = graph
        self.distance = dict((node, float("inf")) for node in self.graph.iternodes())
        # Shortest path tree as a dictionary.
        self.parent = dict((node, None) for node in self.graph.iternodes())
        self.in_queue = dict((node, True) for node in self.graph.iternodes())
        self.pq = PriorityQueue()

    def run(self, source):
        """Executable pseudocode."""
        self.source = source
        self.distance[source] = 0
        for node in self.graph.iternodes():
            self.pq.put((self.distance[node], node))
        while not self.pq.empty():
            _, node = self.pq.get()
            if self.in_queue[node]:
                self.in_queue[node] = False
            else:
                continue
            for edge in self.graph.iteroutedges(node):
                if self.in_queue[edge.target] and self._relax(edge):
                    self.pq.put((self.distance[edge.target], edge.target))

    def _relax(self, edge):
        """Edge relaxation."""
        alt = self.distance[edge.source] + edge.weight
        if self.distance[edge.target] > alt:
            self.distance[edge.target] = alt
            self.parent[edge.target] = edge.source
            return True
        return False

    def path(self, target):
        """Construct a path from source to target."""
        if self.source == target:
            return [self.source]
        elif self.parent[target] is None:
            raise ValueError("no path to target")
        else:
            return self.path(self.parent[target]) + [target]


class DijkstraMatrix:
    """The Dijkstra's algorithm with O(V**2) time."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("the graph is not directed")
        self.graph = graph
        self.distance = dict((node, float("inf")) for node in self.graph.iternodes())
        # Shortest path tree as a dictionary.
        self.parent = dict((node, None) for node in self.graph.iternodes())
        self.in_queue = dict((node, True) for node in self.graph.iternodes())

    def run(self, source):
        """Executable pseudocode."""
        self.source = source
        self.distance[source] = 0
        for step in xrange(self.graph.v()):   # |V| times
            # Find min node, O(V) time.
            node = min((node for node in self.graph.iternodes() 
                if self.in_queue[node]), key=self.distance.get)
            self.in_queue[node] = False
            for edge in self.graph.iteroutedges(node):   # O(V) time
                if self.in_queue[edge.target]:
                    self._relax(edge)

    def _relax(self, edge):
        """Edge relaxation."""
        alt = self.distance[edge.source] + edge.weight
        if self.distance[edge.target] > alt:
            self.distance[edge.target] = alt
            self.parent[edge.target] = edge.source
            return True
        return False

    def path(self, target):
        """Construct a path from source to target."""
        if self.source == target:
            return [self.source]
        elif self.parent[target] is None:
            raise ValueError("no path to target")
        else:
            return self.path(self.parent[target]) + [target]

# EOF
