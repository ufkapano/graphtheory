#!/usr/bin/env python3

import sys
import random

class BacktrackingIndependentSet:
    """Find a maximum independent set using backtracking."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        for edge in self.graph.iteredges():
            if edge.source == edge.target:   # for multigraphs
                raise ValueError("a loop detected")
        self.independent_set = set()
        self.current_set = set()
        self.cardinality = 0
        self._used = dict((node, 0) for node in self.graph.iternodes())
        self.node_list = list(self.graph.iternodes())
        #random.shuffle(self.node_list)
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v()*2, recursionlimit))

    def run(self):
        """Executable pseudocode."""
        # Musimy sprawdzic wszystkie mozliwosci, aby znalezc max iset.
        self._try_node(0)
        self.cardinality = len(self.independent_set)

    def _try_node(self, k):
        """Try to add node_list[k] to an iset."""
        node = self.node_list[k]
        if self._used[node] > 0:   # moge wstawiac tylko ze nie nalezy
            if k < self.graph.v() - 1:
                self._try_node(k+1)
            else:
                if len(self.current_set) > len(self.independent_set):
                    self.independent_set = set(self.current_set)
        else:   # _used[node]==0
            # Najpierw sprawdzam mozliwosc, ze nalezy do iset.
            self._add_iset(node)
            if k < self.graph.v() - 1:
                self._try_node(k+1)
            else:
                if len(self.current_set) > len(self.independent_set):
                    self.independent_set = set(self.current_set)
            self._del_iset(node)
            # Teraz sprawdzam mozliwosc, ze nie nalezy do iset.
            if k < self.graph.v() - 1:
                self._try_node(k+1)
            else:
                if len(self.current_set) > len(self.independent_set):
                    self.independent_set = set(self.current_set)

    def _add_iset(self, node):
        """Add a node to iset."""
        self.current_set.add(node)
        self._used[node] += 1
        for target in self.graph.iteradjacent(node):
            self._used[target] += 1

    def _del_iset(self, node):
        """Remove a node from iset."""
        self.current_set.remove(node)
        self._used[node] -= 1
        for target in self.graph.iteradjacent(node):
            self._used[target] -= 1

# EOF
