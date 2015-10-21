#!/usr/bin/python

from Queue import PriorityQueue
from graphtheory.structures.edges import Edge
from graphtheory.algorithms.bipartite import BipartiteGraphBFS
from graphtheory.flow.fordfulkerson import FordFulkersonSparse


class MatchingFordFulkersonSet:
    """Maximum-cardinality matching using the Ford-Fulkerson method."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.mate = dict((node, None) for node in self.graph.iternodes())
        self.cardinality = 0
        algorithm = BipartiteGraphBFS(self.graph)
        algorithm.run()
        self.v1 = set()
        self.v2 = set()
        for node in self.graph.iternodes():   # O(V) time
            if algorithm.color[node] == 1:
                self.v1.add(node)
            else:
                self.v2.add(node)

    def run(self):
        """Executable pseudocode."""
        size = self.graph.v()
        # Create flow network.
        network = self.graph.__class__(size + 2, directed=True)
        self.source = size
        self.sink = size + 1
        network.add_node(self.source)
        network.add_node(self.sink)
        for node in self.graph.iternodes():   # O(V) time
            network.add_node(node)
        for node in self.v1:   # edges from source to V1
            network.add_edge(Edge(self.source, node))
        for edge in self.graph.iteredges():   # edges from V1 to V2
            if edge.source in self.v1:   # weights are 1
                network.add_edge(Edge(edge.source, edge.target))
            else:
                network.add_edge(Edge(edge.target, edge.source))
        for node in self.v2:   # edges from V2 to sink
            network.add_edge(Edge(node, self.sink))
        algorithm = FordFulkersonSparse(network)
        algorithm.run(self.source, self.sink)   # O(V*E) time
        for source in self.v1:
            for target in self.v2:
                if algorithm.flow[source].get(target, 0) == 1:
                    self.mate[source] = target
                    self.mate[target] = source
        self.cardinality = algorithm.max_flow


class MatchingFordFulkersonColor:
    """Maximum-cardinality matching using the Ford-Fulkerson method."""
    # Sets are not used.

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.mate = dict((node, None) for node in self.graph.iternodes())
        self.cardinality = 0
        algorithm = BipartiteGraphBFS(self.graph)
        algorithm.run()
        self.color = algorithm.color

    def run(self):
        """Executable pseudocode."""
        size = self.graph.v()
        # Create flow network.
        network = self.graph.__class__(size + 2, directed=True)
        self.source = size
        self.sink = size + 1
        network.add_node(self.source)
        network.add_node(self.sink)
        for node in self.graph.iternodes():   # O(V) time
            network.add_node(node)
            if self.color[node] == 1:   # edges from source to V1
                network.add_edge(Edge(self.source, node))
            else:   # edges from V2 to sink
                network.add_edge(Edge(node, self.sink))
        for edge in self.graph.iteredges():   # edges from V1 to V2
            if self.color[edge.source] == 1:   # weights are 1
                network.add_edge(Edge(edge.source, edge.target))
            else:
                network.add_edge(Edge(edge.target, edge.source))
        algorithm = FordFulkersonSparse(network)
        algorithm.run(self.source, self.sink)   # O(V*E) time
        for source in self.graph.iternodes():   # O(V**2) time
            for target in self.graph.iternodes():
                if self.color[source] == 1 and self.color[target] != 1 \
                    and algorithm.flow[source].get(target, 0) == 1:
                        self.mate[source] = target
                        self.mate[target] = source
        self.cardinality = algorithm.max_flow


class MaximalMatching:
    """Find a maximal cardinality matching using a greedy method.
    
    Notes
    -----
    Based on ideas from NetworkX library:
    
    http://networkx.github.io/documentation/networkx-1.9.1/
    _modules/networkx/algorithms/matching.html#maximal_matching
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.mate = dict((node, None) for node in self.graph.iternodes())
        self.cardinality = 0

    def run(self):
        """Executable pseudocode."""
        for edge in self.graph.iteredges():   # O(E) time
            if (self.mate[edge.source] is None and 
                self.mate[edge.target] is None):
                    self.mate[edge.source] = edge.target
                    self.mate[edge.target] = edge.source
                    self.cardinality += 1


class MaximalMatchingWithEdges:
    """Find a maximal cardinality matching using a greedy method.
    
    Notes
    -----
    Based on ideas from NetworkX library:
    
    http://networkx.github.io/documentation/networkx-1.9.1/
    _modules/networkx/algorithms/matching.html#maximal_matching
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.mate = dict((node, None) for node in self.graph.iternodes())
        self.cardinality = 0

    def run(self):
        """Executable pseudocode."""
        for edge in self.graph.iteredges():   # O(E) time
            if (self.mate[edge.source] is None and 
                self.mate[edge.target] is None):
                    self.mate[edge.source] = edge
                    self.mate[edge.target] = ~edge
                    self.cardinality += 1


class MinimumWeightMatchingWithEdges:
    """Find a minimum weight matching using a greedy method."""
    # Bedzie potrzebne do problemu chinskiego listonosza.

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.mate = dict((node, None) for node in self.graph.iternodes())
        self.cardinality = 0
        self._pq = PriorityQueue()

    def run(self):
        """Executable pseudocode."""
        for edge in self.graph.iteredges():
            self._pq.put((edge.weight, edge))
        while not self._pq.empty():
            _, edge = self._pq.get()
            if (self.mate[edge.source] is None and 
                self.mate[edge.target] is None):
                    self.mate[edge.source] = edge
                    self.mate[edge.target] = ~edge
                    self.cardinality += 1

# EOF
