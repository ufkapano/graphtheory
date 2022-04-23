#!/usr/bin/env python3

try:
    integer_types = (int, long)
    range = xrange
except NameError:   # Python 3
    integer_types = (int,)


class RepeatedNearestNeighborTSPWithEdges:
    """The repeated nearest neighbor algorithm for TSP.
    
    Attributes
    ----------
    graph : input weighted complete graph
    hamiltonian_cycle : list of edges
    best_weight : number
    _used : dict with nodes, private
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.hamiltonian_cycle = None
        self.best_weight = float("inf")
        self._used = None

    def run(self, source=None):
        """Executable pseudocode."""
        for source in self.graph.iternodes():
            start_node = source
            cycle = list()
            self._used = dict((node, False) for node in self.graph.iternodes())
            self._used[source] = True
            # Szukamy n-1 kolejnych krawedzi. Unikamy tworzenia cyklu.
            for step in range(self.graph.v()-1):
                edge = min(edge for edge in self.graph.iteroutedges(source)
                    if not self._used[edge.target])
                cycle.append(edge)
                self._used[edge.target] = True
                source = edge.target
            # We have to close the cycle.
            for edge in self.graph.iteroutedges(source):
                if edge.target == start_node:
                    cycle.append(edge)
                    break
            weight = sum(edge.weight for edge in cycle)
            if weight < self.best_weight:
                self.best_weight = weight
                self.hamiltonian_cycle = cycle


class RepeatedNearestNeighborTSPWithGraph:
    """The repeated nearest neighbor algorithm for TSP.
    
    Attributes
    ----------
    graph : input weighted complete graph
    hamiltonian_cycle : cycle graph
    best_weight : number
    _used : dict with nodes, private
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.hamiltonian_cycle = None
        self.best_weight = float("inf")
        self._used = None

    def run(self, source=None):
        """Executable pseudocode."""
        for source in self.graph.iternodes():
            start_node = source
            cycle = self.graph.__class__(self.graph.v())
            for node in self.graph.iternodes():
                cycle.add_node(node)
            self._used = dict((node, False) for node in self.graph.iternodes())
            self._used[source] = True
            # Szukamy n-1 kolejnych krawedzi. Unikamy tworzenia cyklu.
            for step in range(self.graph.v()-1):
                edge = min(edge for edge in self.graph.iteroutedges(source)
                    if not self._used[edge.target])
                cycle.add_edge(edge)
                self._used[edge.target] = True
                source = edge.target
            # We have to close the cycle.
            for edge in self.graph.iteroutedges(source):
                if edge.target == start_node:
                    cycle.add_edge(edge)
                    break
            weight = sum(edge.weight for edge in cycle.iteredges())
            if weight < self.best_weight:
                self.best_weight = weight
                self.hamiltonian_cycle = cycle

# EOF
