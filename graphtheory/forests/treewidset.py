#!/usr/bin/env python3

import sys
import collections


class TreeWeightedIndependentDominatingSet1:
    """Find a minimum weight independent dominating set for trees."""

    def __init__(self, graph, weight_dict):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.parent = dict()
        self.dominating_set = set()
        self.cardinality = 0
        self.weight_dict = weight_dict
        self.dominating_set_weight = 0
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v() * 2, recursionlimit))

    def run(self, source=None):
        """Executable pseudocode."""
        if source is not None:
            # A single connected component, a single tree.
            self.parent[source] = None   # before _visit
            a2_set, b2_set, c2_set = self._visit(source)
            self.dominating_set.update(min(a2_set, b2_set,
                key=self._calc_weight))
            self.cardinality = len(self.dominating_set)
            self.dominating_set_weight = self._calc_weight(self.dominating_set)
        else:
            # A forest is possible.
            for node in self.graph.iternodes():
                if node not in self.parent:
                    self.parent[node] = None   # before _visit
                    a2_set, b2_set, c2_set = self._visit(node)
                    self.dominating_set.update(min(a2_set, b2_set,
                        key=self._calc_weight))
            self.cardinality = len(self.dominating_set)
            self.dominating_set_weight = self._calc_weight(self.dominating_set)

    def _calc_weight(self, aset):
        """Find the weight of a given vertex set."""
        return sum(self.weight_dict[node] for node in aset)

    def _compose(self, arg1, arg2):
        """Compose results."""
        # a_set : min dset that includes root
        # b_set : min dset that excludes root
        # c_set : root undominated
        a1_set, b1_set, c1_set = arg1
        a2_set, b2_set, c2_set = arg2
        a_set = a1_set | min(b2_set, c2_set, key=self._calc_weight)   # ZMIANA
        b_set = min(b1_set | a2_set, b1_set | b2_set, c1_set | a2_set, 
            key=self._calc_weight)
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


class TreeWeightedIndependentDominatingSet2:
    """Find a minimum weight independent dominating set for trees."""

    def __init__(self, graph, weight_dict):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.parent = dict()
        self.dominating_set = set()
        self.cardinality = 0
        self.weight_dict = weight_dict
        self.dominating_set_weight = 0
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v() * 2, recursionlimit))

    def run(self, source=None):
        """Executable pseudocode."""
        if source is not None:
            # A single connected component, a single tree.
            self.parent[source] = None   # before _visit
            a2_pair, b2_pair, c2_pair = self._visit(source)
            pair1 = min(a2_pair, b2_pair, key=lambda pair: pair[0])
            self.dominating_set.update(pair1[1])
            self.cardinality += len(pair1[1])
            self.dominating_set_weight += pair1[0]
        else:
            # A forest is possible.
            for node in self.graph.iternodes():
                if node not in self.parent:
                    self.parent[node] = None   # before _visit
                    a2_pair, b2_pair, c2_pair = self._visit(node)
                    pair1 = min(a2_pair, b2_pair, key=lambda pair: pair[0])
                    self.dominating_set.update(pair1[1])
                    self.cardinality += len(pair1[1])
                    self.dominating_set_weight += pair1[0]

    def _compose(self, arg1, arg2):
        """Compose results."""
        # a_set : min dset that includes root
        # b_set : min dset that excludes root
        # c_set : root undominated
        a1_pair, b1_pair, c1_pair = arg1
        a2_pair, b2_pair, c2_pair = arg2

        pair1 = a1_pair
        pair2 = min(b2_pair, c2_pair, key=lambda pair: pair[0])   # ZMIANA
        a_pair = (pair1[0] + pair2[0], pair1[1] | pair2[1])

        pair1 = (b1_pair[0] + a2_pair[0], b1_pair[1] | a2_pair[1])
        pair2 = (b1_pair[0] + b2_pair[0], b1_pair[1] | b2_pair[1])
        pair3 = (c1_pair[0] + a2_pair[0], c1_pair[1] | a2_pair[1])
        b_pair = min(pair1, pair2, pair3, key=lambda pair: pair[0])

        c_pair = (c1_pair[0] + b2_pair[0], c1_pair[1] | b2_pair[1])
        return (a_pair, b_pair, c_pair)

    def _visit(self, root):
        """Explore recursively the connected component."""
        # Start from a single node.
        arg1 = ((self.weight_dict[root], set([root])),
            (self.weight_dict[root], set([root])),
            (0, set()))
        for target in self.graph.iteradjacent(root):
            if target not in self.parent:
                self.parent[target] = root   # before _visit
                arg2 = self._visit(target)
                arg1 = self._compose(arg1, arg2)
        return arg1


TreeWeightedIndependentDominatingSet = TreeWeightedIndependentDominatingSet2

# EOF
