#!/usr/bin/env python3

import sys
import collections


class BorieIndependentSet:
    """Find a maximum independent set for trees.
    
    It works for trees and forests.
    
    Attributes
    ----------
    graph : input forest
    independent_set : set with nodes
    parent : dict (DFS tree)
    cardinality : number (the size of max iset)
    
    Notes
    -----
    Based on
    
    Richard B. Borie, R. Gary Parker, Craig A. Tovey, 
    Solving Problems on Recursively Constructed Graphs,
    ACM Computing Surveys 41, 4 (2008).
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.parent = dict()
        self.independent_set = set()
        self.cardinality = 0
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v() * 2, recursionlimit))

    def run(self, source=None):
        """Executable pseudocode."""
        if source is not None:
            # A single connected component, a single tree.
            self.parent[source] = None   # before _visit
            arg2 = self._visit(source)
            self.independent_set.update(max(arg2, key=len))
            self.cardinality = len(self.independent_set)
        else:
            # A forest is possible.
            for node in self.graph.iternodes():
                if node not in self.parent:
                    self.parent[node] = None   # before _visit
                    arg2 = self._visit(node)
                    self.independent_set.update(max(arg2, key=len))
            self.cardinality = len(self.independent_set)

    def _compose(self, arg1, arg2):
        """Compose results."""
        # a_set : max iset that includes root
        # b_set : max iset that excludes root
        a1_set, b1_set = arg1
        a2_set, b2_set = arg2
        a_set = a1_set | b2_set
        b_set = b1_set | max(arg2, key=len)
        return (a_set, b_set)

    def _visit(self, root):
        """Explore recursively the connected component."""
        # Start from a single node.
        arg1 = (set([root]), set())
        for target in self.graph.iteradjacent(root):
            if target not in self.parent:
                self.parent[target] = root   # before _visit
                arg2 = self._visit(target)
                arg1 = self._compose(arg1, arg2)
        return arg1


class TreeIndependentSet1:
    """Find a maximum independent set for forests.
    
    A single tree may become disconnected during computations.
    
    Attributes
    ----------
    graph : input forest
    independent_set : set with nodes
    cardinality : number (the size of max iset)
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.independent_set = set()
        self.cardinality = 0

    def run(self):
        """Executable pseudocode."""
        used = set()   # for iset and neighbors
        # A dictionary with node degrees, O(V) time.
        degree_dict = dict((node, self.graph.degree(node))
            for node in self.graph.iternodes())
        Q = collections.deque()   # for leafs
        # Put leafs to the queue, O(V) time.
        for node in self.graph.iternodes():
            if degree_dict[node] == 0:   # isolated node from the beginning
                self.independent_set.add(node)
                used.add(node)
                self.cardinality += 1
            elif degree_dict[node] == 1:   # leaf
                Q.append(node)
        while len(Q) > 0:
            source = Q.popleft()
            # A leaf may become isolated.
            if degree_dict[source] == 0:
                if source not in used:
                    self.independent_set.add(source)
                    used.add(source)
                    self.cardinality += 1
                continue
            assert degree_dict[source] == 1
            for target in self.graph.iteradjacent(source):
                if degree_dict[target] > 0:   # this is parent
                    self.independent_set.add(source)   # put leaf to iset
                    used.add(source)
                    used.add(target)
                    self.cardinality += 1
                    # Remove edges going from target.
                    for node in self.graph.iteradjacent(target):
                        if degree_dict[node] > 0:
                            degree_dict[node] -= 1
                            degree_dict[target] -= 1
                            if degree_dict[node] == 1:   # new leaf
                                Q.append(node)
                    break


class TreeIndependentSet2:
    """Find a maximum independent set for forests.
    
    A single tree is connected during computations.
    
    Attributes
    ----------
    graph : input forest
    independent_set : set with nodes
    cardinality : number (the size of max iset)
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.independent_set = set()
        self.cardinality = 0

    def run(self):
        """Executable pseudocode."""
        used = set()   # for iset and neighbors
        # A dictionary with node degrees, O(V) time.
        degree_dict = dict((node, self.graph.degree(node))
            for node in self.graph.iternodes())
        Q = collections.deque()   # for leafs
        # Put leafs to the queue, O(V) time.
        for node in self.graph.iternodes():
            if degree_dict[node] == 0:   # isolated node from the beginning
                self.independent_set.add(node)
                used.add(node)
                self.cardinality += 1
            elif degree_dict[node] == 1:   # leaf
                Q.append(node)
        while len(Q) > 0:
            source = Q.popleft()
            # A leaf may become isolated.
            if degree_dict[source] == 0:
                if source not in used:
                    self.independent_set.add(source)
                    used.add(source)
                    self.cardinality += 1
                continue
            assert degree_dict[source] == 1
            for target in self.graph.iteradjacent(source):
                if degree_dict[target] > 0:   # this is parent
                    if source not in used:
                        self.independent_set.add(source)   # put leaf to iset
                        used.add(source)
                        used.add(target)
                        self.cardinality += 1
                    # Remove the edge from source to target.
                    degree_dict[target] -= 1
                    degree_dict[source] -= 1
                    if degree_dict[target] == 1:   # parent is a new leaf
                        Q.append(target)
                    break


TreeIndependentSet = TreeIndependentSet2

# EOF
