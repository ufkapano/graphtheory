#!/usr/bin/env python3

try:
    from Queue import PriorityQueue
except ImportError:   # Python 3
    from queue import PriorityQueue

from graphtheory.structures.edges import Edge


class MaximalMatching:
    """Find a maximal cardinality matching using a greedy method.
    
    Attributes
    ----------
    graph : input undirected graph
    mate : dict with nodes (values are nodes or None)
    cardinality : number
    
    Notes
    -----
    Based on ideas from NetworkX library:
    
    http://networkx.github.io/documentation/networkx-1.9.1/
    _modules/networkx/algorithms/matching.html#maximal_matching
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
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
    
    Attributes
    ----------
    graph : input undirected graph
    mate : dict with nodes (values are edges or None)
    cardinality : number
    
    Notes
    -----
    Based on ideas from NetworkX library:
    
    http://networkx.github.io/documentation/networkx-1.9.1/
    _modules/networkx/algorithms/matching.html#maximal_matching
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
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
    """Find a minimum weight matching using a greedy method.
    
    Attributes
    ----------
    graph : input undirected graph
    mate : dict with nodes (values are edges or None)
    cardinality : number
    """
    # Bedzie potrzebne do problemu chinskiego listonosza.

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
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
