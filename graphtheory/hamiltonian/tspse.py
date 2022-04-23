#!/usr/bin/env python3

try:
    from Queue import PriorityQueue
    range = xrange
except ImportError:   # Python 3
    from queue import PriorityQueue

from graphtheory.structures.unionfind import UnionFind


class SortedEdgeTSPWithEdges:
    """The sorted edge algorithm (a.k.a. cheapest link) for TSP.
    
    Attributes
    ----------
    graph : input weighted complete graph
    hamiltonian_cycle : list of edges
    _uf : disjoint-set data structure, private
    _pq : priority queue, private
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.hamiltonian_cycle = list()
        self._uf = UnionFind()
        self._pq = PriorityQueue()

    def run(self, source=None):
        """Executable pseudocode."""
        degree_dict = dict((node, 0) for node in self.graph.iternodes())
        for node in self.graph.iternodes():
            self._uf.create(node)
        for edge in self.graph.iteredges():
            self._pq.put((edge.weight, edge))
        while not self._pq.empty():
            _, edge = self._pq.get()
            degree1 = degree_dict[edge.source]
            degree2 = degree_dict[edge.target]
            # Zabezpieczam przed skrzyzowaniami T, X, itp.
            if degree1 == 2 or degree2 == 2:
                continue
            if degree1 == 0 or degree2 == 0:
                self._uf.union(edge.source, edge.target)
                self.hamiltonian_cycle.append(edge)
                degree_dict[edge.source] += 1
                degree_dict[edge.target] += 1
                continue
            # Here degree1 = degree2 = 1.
            if self._uf.find(edge.source) != self._uf.find(edge.target):
                # Join pieces.
                self._uf.union(edge.source, edge.target)
                self.hamiltonian_cycle.append(edge)
                degree_dict[edge.source] += 1
                degree_dict[edge.target] += 1
            elif len(self.hamiltonian_cycle) == self.graph.v()-1:
                # Close the Hamiltonian cycle.
                self.hamiltonian_cycle.append(edge)
                degree_dict[edge.source] += 1
                degree_dict[edge.target] += 1
        # Create the corrected (directed) list of edges.
        # Przeksztalcam cykl Hamiltona do postaci poprawnej listy krawedzi.
        # Na razie krawedzie moga miec zla kolejnosc i kierunek.
        # Tworze slownik z krawedziami w obie strony.
        edge_dict = dict((node, []) for node in self.graph.iternodes())
        for edge in self.hamiltonian_cycle:   # O(V) time
            edge_dict[edge.source].append(edge)
            edge_dict[edge.target].append(~edge)
        edge = self.hamiltonian_cycle[0]
        self.hamiltonian_cycle = [edge]
        # Kompletuje kolejne krawedzie.
        for step in range(self.graph.v()-1):   # O(V) time
            edge1, edge2 = edge_dict[edge.target]
            if edge1.target == edge.source:
                self.hamiltonian_cycle.append(edge2)
                edge = edge2
            else:
                self.hamiltonian_cycle.append(edge1)
                edge = edge1


class SortedEdgeTSPWithGraph:
    """The sorted edge algorithm for TSP.
    
    Attributes
    ----------
    graph : input weighted complete graph
    hamiltonian_cycle : cycle graph
    _uf : disjoint-set data structure, private
    _pq : priority queue, private
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.hamiltonian_cycle = self.graph.__class__(self.graph.v())
        for node in self.graph.iternodes():
            self.hamiltonian_cycle.add_node(node)
        self._uf = UnionFind()
        self._pq = PriorityQueue()

    def run(self, source=None):
        """Executable pseudocode."""
        for node in self.graph.iternodes():
            self._uf.create(node)
        for edge in self.graph.iteredges():
            self._pq.put((edge.weight, edge))
        while not self._pq.empty():
            _, edge = self._pq.get()
            degree1 = self.hamiltonian_cycle.degree(edge.source)
            degree2 = self.hamiltonian_cycle.degree(edge.target)
            # Zabezpieczam przed skrzyzowaniami T, X, itp.
            if degree1 == 2 or degree2 == 2:
                continue
            if degree1 == 0 or degree2 == 0:
                self._uf.union(edge.source, edge.target)
                self.hamiltonian_cycle.add_edge(edge)
                continue
            # Here degree1 = degree2 = 1.
            if self._uf.find(edge.source) != self._uf.find(edge.target):
                # Join pieces.
                self._uf.union(edge.source, edge.target)
                self.hamiltonian_cycle.add_edge(edge)
            elif self.hamiltonian_cycle.e() == self.hamiltonian_cycle.v()-1:
                # Close the Hamiltonian cycle.
                self.hamiltonian_cycle.add_edge(edge)

# EOF
