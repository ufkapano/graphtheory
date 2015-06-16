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
        self.used = dict((node, False) for node in self.graph.iternodes())

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
        self.stack.append(node)   # at the beginning of _hamilton_dfs
        if len(self.stack) == self.graph.v():
            # Hamiltonian path is possible.
            for edge in self.graph.iteroutedges(node):
                if edge.target == self.source:
                    self.stack.append(self.source)
                    self.hamilton_cycle = list(self.stack)
                    self.stack.pop()
        else:
            self.used[node] = True
            for edge in self.graph.iteroutedges(node):
                if not self.used[edge.target]:
                    self._hamilton_dfs(edge.target)
            self.used[node] = False
        self.stack.pop()   # at the end of _hamilton_dfs


class HamiltonCycleDFSWithEdges:
    """Finding a Hamiltonian cycle in a Hamiltonian graph."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.hamilton_cycle = list()
        self.stack = list()
        self.used = dict((node, False) for node in self.graph.iternodes())

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
            for edge in self.graph.iteroutedges(node):
                if edge.target == self.source:
                    self.stack.append(edge)
                    self.hamilton_cycle = list(self.stack)
                    self.stack.pop()
        else:
            self.used[node] = True
            for edge in self.graph.iteroutedges(node):
                if not self.used[edge.target]:
                    self.stack.append(edge)
                    self._hamilton_dfs(edge.target)
                    self.stack.pop()
            self.used[node] = False

# EOF
