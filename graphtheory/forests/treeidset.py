#!/usr/bin/env python3

import sys
import collections


class TreeIndependentDominatingSet:
    """Find a minimum cardinality independent dominating set for trees."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.parent = dict()
        self.dominating_set = set()
        self.cardinality = 0
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v() * 2, recursionlimit))

    def run(self, source=None):
        """Executable pseudocode."""
        if source is not None:
            # A single connected component, a single tree.
            self.parent[source] = None   # before _visit
            a2_set, b2_set, c2_set = self._visit(source)
            self.dominating_set.update(min(a2_set, b2_set, key=len))
            self.cardinality = len(self.dominating_set)
        else:
            # A forest is possible.
            for node in self.graph.iternodes():
                if node not in self.parent:
                    self.parent[node] = None   # before _visit
                    a2_set, b2_set, c2_set = self._visit(node)
                    self.dominating_set.update(min(a2_set, b2_set, key=len))
            self.cardinality = len(self.dominating_set)

    def _compose(self, arg1, arg2):
        """Compose results."""
        # a_set : min dset that includes root
        # b_set : min dset that excludes root
        # c_set : root undominated
        a1_set, b1_set, c1_set = arg1
        a2_set, b2_set, c2_set = arg2
        a_set = a1_set | min(b2_set, c2_set, key=len)   # ZMIANA
        b_set = min(b1_set | a2_set, b1_set | b2_set,
            c1_set | a2_set, key=len)
        c_set = c1_set | b2_set
        return (a_set, b_set, c_set)

    def _visit(self, root):
        """Explore recursively the connected component."""
        # Start from a single node.
        arg1 = (set([root]), set([root]), set())
        for target in self.graph.iteradjacent(root):
            if target not in self.parent:
                self.parent[target] = root   # before _visit
                arg2 = self._visit(target)
                arg1 = self._compose(arg1, arg2)
        return arg1

# EOF
