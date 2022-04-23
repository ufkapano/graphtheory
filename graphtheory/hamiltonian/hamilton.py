#!/usr/bin/env python3

import sys

class HamiltonianCycleDFS:
    """Finding a Hamiltonian cycle in a Hamiltonian graph.
    
    Attributes
    ----------
    graph : input graph
    hamiltonian_cycle : list of nodes
    source : starting node
    _stack : list of nodes, private
    _used : dict with nodes, private
    
    Notes
    -----
    Based on the description from:
    
    http://edu.i-lo.tarnow.pl/inf/alg/001_search/0136.php
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.hamiltonian_cycle = list()
        self.source = None
        self._stack = list()
        self._used = dict((node, False) for node in self.graph.iternodes())
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
        if self.hamiltonian_cycle:
            return
        self._stack.append(node)   # at the beginning of _hamilton_dfs
        if len(self._stack) == self.graph.v():
            # Hamiltonian path is possible.
            for edge in self.graph.iteroutedges(node):
                if edge.target == self.source:
                    self._stack.append(self.source)
                    self.hamiltonian_cycle = list(self._stack)
                    self._stack.pop()
        else:
            self._used[node] = True
            for edge in self.graph.iteroutedges(node):
                if not self._used[edge.target]:
                    self._hamilton_dfs(edge.target)
            self._used[node] = False
        self._stack.pop()   # at the end of _hamilton_dfs


class HamiltonianCycleDFSWithEdges:
    """Finding a Hamiltonian cycle in a Hamiltonian graph.
    
    Attributes
    ----------
    graph : input graph
    hamiltonian_cycle : list of edges
    source : starting node
    _stack : list of nodes, private
    _used : dict with nodes, private
    
    Notes
    -----
    Based on the description from:
    
    http://edu.i-lo.tarnow.pl/inf/alg/001_search/0136.php
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.hamiltonian_cycle = list()
        self.source = None
        self._stack = list()
        self._used = dict((node, False) for node in self.graph.iternodes())
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
        if self.hamiltonian_cycle:
            return
        if len(self._stack) == self.graph.v()-1:
            # Hamiltonian path is possible.
            for edge in self.graph.iteroutedges(node):
                if edge.target == self.source:
                    self._stack.append(edge)
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


class HamiltonianCycleDFSWithGraph:
    """Finding a Hamiltonian cycle in a Hamiltonian graph.
    
    Attributes
    ----------
    graph : input graph
    hamiltonian_cycle : cycle graph
    source : starting node
    _path : graph, private
    _used : dict with nodes, private
    
    Notes
    -----
    Based on the description from:
    
    http://edu.i-lo.tarnow.pl/inf/alg/001_search/0136.php
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.hamiltonian_cycle = None
        self.source = None
        self._path = self.graph.__class__(self.graph.v(), self.graph.is_directed())
        for node in self.graph.iternodes():
            self._path.add_node(node)
        self._used = dict((node, False) for node in self.graph.iternodes())
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
        if self.hamiltonian_cycle:
            return
        if self._path.e() == self.graph.v()-1:
            # Hamiltonian path is possible.
            for edge in self.graph.iteroutedges(node):
                if edge.target == self.source:
                    self._path.add_edge(edge)
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
