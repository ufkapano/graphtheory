#!/usr/bin/env python3

import sys

class BruteForceTSPWithEdges:
    """The brute force algorithm (a.k.a. exhaustive search) for TSP.
    
    Attributes
    ----------
    graph : input weighted complete graph
    hamiltonian_cycle : list of edges
    source : starting node
    best_weight : number
    _stack : list of nodes, private
    _used : dict with nodes, private
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.hamiltonian_cycle = list()
        self.source = None
        self._stack = list()
        self._used = dict((node, False) for node in self.graph.iternodes())
        self.best_weight = float("inf")
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v() * 2, recursionlimit))

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:   # get first random node
            source = next(self.graph.iternodes())
        self.source = source
        self._hamilton_dfs(self.source)

    def _hamilton_dfs(self, node):
        """Modified DFS from the node."""
        if len(self._stack) == self.graph.v()-1:
            # Hamiltonian path is possible.
            for edge in self.graph.iteroutedges(node):
                if edge.target == self.source:
                    # We have a Hamiltonian cycle.
                    self._stack.append(edge)
                    weight = sum(edge.weight for edge in self._stack)
                    if weight < self.best_weight:
                        self.best_weight = weight
                        self.hamiltonian_cycle = list(self._stack)
                    self._stack.pop()
        else:
            self._used[node] = True
            for edge in self.graph.iteroutedges(node):
                if not self._used[edge.target]:
                    self._stack.append(edge)
                    self._hamilton_dfs(edge.target)
                    self._stack.pop()
            self._used[node] = False


class BruteForceTSPWithGraph:
    """The brute force algorithm (a.k.a. exhaustive search) for TSP.
    
    Attributes
    ----------
    graph : input weighted complete graph
    hamiltonian_cycle : cycle graph
    source : starting node
    best_weight : number
    _path : graph, private
    _used : dict with nodes, private
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.hamiltonian_cycle = None
        self.source = None
        self._path = self.graph.__class__(self.graph.v(), self.graph.is_directed())
        for node in self.graph.iternodes():
            self._path.add_node(node)
        self._used = dict((node, False) for node in self.graph.iternodes())
        self.best_weight = float("inf")
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v() * 2, recursionlimit))

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:   # get first random node
            source = next(self.graph.iternodes())
        self.source = source
        self._hamilton_dfs(self.source)

    def _hamilton_dfs(self, node):
        """Modified DFS from the node."""
        if self._path.e() == self.graph.v()-1:
            # Hamiltonian path is possible.
            for edge in self.graph.iteroutedges(node):
                if edge.target == self.source:
                    # We have a Hamiltonian cycle.
                    self._path.add_edge(edge)
                    weight = sum(edge.weight for edge in self._path.iteredges())
                    if weight < self.best_weight:
                        self.best_weight = weight
                        self.hamiltonian_cycle = self._path.copy()
                    self._path.del_edge(edge)
        else:
            self._used[node] = True
            for edge in self.graph.iteroutedges(node):
                if not self._used[edge.target]:
                    self._path.add_edge(edge)
                    self._hamilton_dfs(edge.target)
                    self._path.del_edge(edge)
            self._used[node] = False

# EOF
