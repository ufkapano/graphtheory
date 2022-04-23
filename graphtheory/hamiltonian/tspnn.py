#!/usr/bin/env python3

try:
    integer_types = (int, long)
    range = xrange
except NameError:   # Python 3
    integer_types = (int,)


class NearestNeighborTSPWithEdges:
    """The nearest neighbor algorithm for TSP.
    
    Attributes
    ----------
    graph : input weighted complete graph
    hamiltonian_cycle : list of edges
    source : starting node
    _used : dict with nodes, private
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.hamiltonian_cycle = list()
        self.source = None
        self._used = dict((node, False) for node in self.graph.iternodes())

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:
            source = next(self.graph.iternodes())
        start_node = source
        self._used[source] = True
        # Szukamy n-1 kolejnych krawedzi. Unikamy tworzenia cyklu.
        for step in range(self.graph.v()-1):
            edge = min(edge for edge in self.graph.iteroutedges(source)
                if not self._used[edge.target])
            self.hamiltonian_cycle.append(edge)
            self._used[edge.target] = True
            source = edge.target
        # We have to close the cycle.
        for edge in self.graph.iteroutedges(source):
            if edge.target == start_node:
                self.hamiltonian_cycle.append(edge)
                break


class NearestNeighborTSPWithGraph:
    """The nearest neighbor algorithm for TSP.
    
    Attributes
    ----------
    graph : input weighted complete graph
    hamiltonian_cycle : cycle graph
    source : starting node
    _used : dict with nodes, private
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.hamiltonian_cycle = self.graph.__class__(self.graph.v(), self.graph.is_directed())
        for node in self.graph.iternodes():
            self.hamiltonian_cycle.add_node(node)
        self.source = None
        self._used = dict((node, False) for node in self.graph.iternodes())

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:
            source = next(self.graph.iternodes())
        self.source = source
        self._used[self.source] = True
        # Szukamy n-1 kolejnych krawedzi. Unikamy tworzenia cyklu.
        for step in range(self.graph.v()-1):
            edge = min(edge for edge in self.graph.iteroutedges(source)
                if not self._used[edge.target])
            self.hamiltonian_cycle.add_edge(edge)
            self._used[edge.target] = True
            source = edge.target
        # We have to close the cycle.
        for edge in self.graph.iteroutedges(source):
            if edge.target == self.source:
                self.hamiltonian_cycle.add_edge(edge)
                break

# EOF
