#!/usr/bin/env python3

import sys
import collections


class BorieNodeCover:
    """Find a minimum cardinality node cover for trees.
    
    Attributes
    ----------
    graph : input forest
    node_cover : set with nodes
    parent : dict (DFS tree)
    cardinality : number (the size of min dset)
    
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
        self.node_cover = set()
        self.cardinality = 0
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v() * 2, recursionlimit))

    def run(self, source=None):
        """Executable pseudocode."""
        if source is not None:
            # A single connected component, a single tree.
            self.parent[source] = None   # before _visit
            arg2 = self._visit(source)
            self.node_cover.update(min(arg2, key=len))
            self.cardinality = len(self.node_cover)
        else:
            # A forest is possible.
            for node in self.graph.iternodes():
                if node not in self.parent:
                    self.parent[node] = None   # before _visit
                    arg2 = self._visit(node)
                    self.node_cover.update(min(arg2, key=len))
            self.cardinality = len(self.node_cover)

    def _compose(self, arg1, arg2):
        """Compose results."""
        # a_set : min cover includes root
        # b_set : min cover excludes root
        a1_set, b1_set = arg1
        a2_set, b2_set = arg2
        a_set = a1_set | min(arg2, key=len)
        b_set = b1_set | a2_set
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


class TreeNodeCover1:
    """Find a minimum cardinality node cover for forests.
    
    Attributes
    ----------
    graph : input forest
    node_cover : set with nodes
    cardinality : number (the size of min dset)
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.node_cover = set()
        self.cardinality = 0

    def run(self):
        """Executable pseudocode."""
        # A dictionary with node degrees, O(V) time.
        degree_dict = dict((node, self.graph.degree(node))
            for node in self.graph.iternodes())
        Q = collections.deque()   # for leafs
        # Put leafs to the queue, O(V) time.
        for node in self.graph.iternodes():
            if degree_dict[node] == 1:
                Q.append(node)
        while len(Q) > 0:
            source = Q.popleft()
            if degree_dict[source] == 0:   # isolated node
                continue
            assert degree_dict[source] == 1
            for target in self.graph.iteradjacent(source):
                if degree_dict[target] > 0:   # this is parent
                    self.node_cover.add(target)   # put parent to cover
                    self.cardinality += 1
                    # Remove edges going from target.
                    for node in self.graph.iteradjacent(target):
                        if degree_dict[node] > 0:
                            degree_dict[node] -= 1
                            degree_dict[target] -= 1
                            if degree_dict[node] == 1:   # new leaf
                                Q.append(node)
                    break


class TreeNodeCover2:
    """Find a minimum cardinality node cover for forests.
    
    Attributes
    ----------
    graph : input forest
    node_cover : set with nodes
    cardinality : number (the size of min dset)
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.node_cover = set()
        self.cardinality = 0

    def run(self):
        """Executable pseudocode."""
        # A dictionary with node degrees, O(V) time.
        degree_dict = dict((node, self.graph.degree(node))
            for node in self.graph.iternodes())
        Q = collections.deque()   # for leafs
        # Put leafs to the queue, O(V) time.
        for node in self.graph.iternodes():
            if degree_dict[node] == 1:
                Q.append(node)
        while len(Q) > 0:
            source = Q.popleft()
            if degree_dict[source] == 0:   # isolated node
                continue
            assert degree_dict[source] == 1
            for target in self.graph.iteradjacent(source):
                if degree_dict[target] > 0:   # this is parent
                    if (source not in self.node_cover and
                        target not in self.node_cover): # edge not covered
                        self.node_cover.add(target)   # put parent to cover
                        self.cardinality += 1
                    # Remove the edge from source to target.
                    degree_dict[source] -= 1
                    degree_dict[target] -= 1
                    if degree_dict[target] == 1:   # new leaf
                        Q.append(target)
                    break


TreeNodeCover = TreeNodeCover2
