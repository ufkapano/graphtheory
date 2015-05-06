#!/usr/bin/python
#
# Based on the description from:
# http://edu.i-lo.tarnow.pl/inf/alg/001_search/0136.php

class HamiltonCycleDFS:
    """Finding a Hamiltonian cycle in a Hamiltonian graph."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.hamilton_cycle = list()
        self.stack = list()
        self.used = set()

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:   # get first random node
            source = self.graph.iternodes().next()
        self.source = source
        self._hamilton_dfs(self.source)

    def _hamilton_dfs(self, node):
        """Modified DFS from the node."""
        if self.hamilton_cycle:
            return
        self.stack.append(node)
        if len(self.stack) == self.graph.v():
            # Hamiltonian path is possible.
            for edge in self.graph.iteroutedges(self.stack[-1]):
                if edge.target == self.source:
                    self.hamilton_cycle = list(self.stack)
        else:
            self.used.add(node)
            for edge in self.graph.iteroutedges(node):
                if edge.target not in self.used:
                    self._hamilton_dfs(edge.target)
            self.used.discard(node)
        self.stack.pop()


class HamiltonCycleDFSWithEdges:
    """Finding a Hamiltonian cycle in a Hamiltonian graph."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.hamilton_cycle = list()
        self.stack = list()
        self.used = set()

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:   # get first random node
            source = self.graph.iternodes().next()
        self.source = source
        self._hamilton_dfs(self.source)

    def _hamilton_dfs(self, node):
        """Modified DFS from the node."""
        if self.hamilton_cycle:
            return
        if len(self.stack) == self.graph.v()-1:
            # Hamiltonian path is possible.
            for edge in self.graph.iteroutedges(self.stack[-1].target):
                if edge.target == self.source:
                    self.stack.append(edge)
                    self.hamilton_cycle = list(self.stack)
        else:
            self.used.add(node)
            for edge in self.graph.iteroutedges(node):
                if edge.target not in self.used:
                    self.stack.append(edge)
                    self._hamilton_dfs(edge.target)
            self.used.discard(node)
        self.stack.pop()

# EOF
