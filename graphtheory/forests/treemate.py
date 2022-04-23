#!/usr/bin/env python3

import sys

class BorieMatching:
    """Find a maximum matching for trees.
    
    Attributes
    ----------
    graph : input forest
    mate_set : set with edges
    mate : dict
    parent : dict (DFS tree)
    cardinality : number (the size of max matching)
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.parent = dict()
        self.mate_set = set()
        self.mate = dict((node, None) for node in self.graph.iternodes())
        self.cardinality = 0
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v() * 2, recursionlimit))

    def run(self, source=None):
        """Executable pseudocode."""
        if source is not None:
            # A single connected component, a single tree.
            self.parent[source] = None   # before _visit
            arg2 = self._visit(source)
            self.mate_set.update(max(arg2, key=len))
        else:
            # A forest is possible.
            for node in self.graph.iternodes():
                if node not in self.parent:
                    self.parent[node] = None   # before _visit
                    arg2 = self._visit(node)
                    self.mate_set.update(max(arg2, key=len))
        self.cardinality = len(self.mate_set)
        for edge in self.mate_set:   # O(V) time
            self.mate[edge.source] = edge.target
            self.mate[edge.target] = edge.source

    def _compose(self, arg1, arg2, edge):
        """Compose results with an edge connecting roots."""
        # a_set : max matching that includes root
        # b_set : max matching that excludes roota
        if edge.source > edge.target:
            edge = ~edge
        a1_set, b1_set = arg1
        a2_set, b2_set = arg2
        a_set = a1_set | max(arg2, key=len)
        a_set = max(a_set, b1_set | b2_set | set([edge]), key=len)
        b_set = b1_set | a2_set
        return (a_set, b_set)

    def _visit(self, root):
        """Explore recursively the connected component."""
        # Start from a single node.
        arg1 = (set(), set())   # (a1_set, b1_set)
        for edge in self.graph.iteroutedges(root):
            if edge.target not in self.parent:
                self.parent[edge.target] = root   # before _visit
                arg2 = self._visit(edge.target)
                arg1 = self._compose(arg1, arg2, edge)
        return arg1
