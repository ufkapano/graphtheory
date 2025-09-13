#!/usr/bin/env python3

import sys
import collections
from graphtheory.forests.treepeo import TreePEO


class BorieDominatingSet:
    """Find a minimum cardinality dominating set for trees.
    
    Attributes
    ----------
    graph : input forest
    dominating_set : set with nodes
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
        a_set = a1_set | min(arg2, key=len)
        b_set = min(b1_set | a2_set, b1_set | b2_set, c1_set | a2_set, key=len)
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


class TreeDominatingSet1:
    """Find a minimum dominating set for forests.
    
    A single tree may become disconnected during computations.
    
    Attributes
    ----------
    graph : input forest
    dominating_set : set with nodes
    cardinality : number (the size of min dset)
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.dominating_set = set()
        self.cardinality = 0

    def run(self):
        """Executable pseudocode."""
        used = set()   # for dset and neighbors
        # A dictionary with node degrees, O(n) time.
        degree_dict = dict((node, self.graph.degree(node))
            for node in self.graph.iternodes())
        Q = collections.deque()   # for leaves
        # Put leaves to the queue, O(n) time.
        for node in self.graph.iternodes():
            if degree_dict[node] == 0:
                self.dominating_set.add(node)   # isolated node from the beginning
                used.add(node)
                self.cardinality += 1
            elif degree_dict[node] == 1:   # leaf
                Q.append(node)
        while len(Q) > 0:
            source = Q.popleft()
            # A leaf may become isolated.
            if degree_dict[source] == 0:
                if source not in used:   # parent not in dset
                    self.dominating_set.add(source)
                    used.add(source)
                    self.cardinality += 1
                continue
            assert degree_dict[source] == 1
            if source in used:
                # Remove such leaf.
                for node in self.graph.iteradjacent(source):
                    if degree_dict[node] > 0:   # this is parent
                        degree_dict[node] -= 1
                        degree_dict[source] -= 1
                        if degree_dict[node] == 1:   # new leaf
                            Q.append(node)
                        break
            else:   # source not in used, parent goes to dset
                for target in self.graph.iteradjacent(source):
                    if degree_dict[target] > 0:   # this is parent
                        self.dominating_set.add(target)
                        used.add(target)
                        self.cardinality += 1
                        # Remove edges going from target.
                        for node in self.graph.iteradjacent(target):
                            if degree_dict[node] > 0:
                                degree_dict[node] -= 1
                                degree_dict[target] -= 1
                                used.add(node)   # child goes to used
                                if degree_dict[node] == 1:   # new leaf
                                    Q.append(node)
                        break


class TreeDominatingSet2:
    """Find a minimum dominating set for forests.
    
    A single tree is connected during computations.
    
    Attributes
    ----------
    graph : input forest
    dominating_set : set with nodes
    cardinality : number (the size of min dset)
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.dominating_set = set()
        self.cardinality = 0

    def run(self):
        """Executable pseudocode."""
        used = set()   # for dset and neighbors
        # A dictionary with node degrees, O(n) time.
        degree_dict = dict((node, self.graph.degree(node))
            for node in self.graph.iternodes())
        Q = collections.deque()   # for leaves
        # Put leaves to the queue, O(n) time.
        for node in self.graph.iternodes():
            if degree_dict[node] == 0:
                self.dominating_set.add(node)   # isolated node from the beginning
                used.add(node)
                self.cardinality += 1
            elif degree_dict[node] == 1:   # leaf
                Q.append(node)
        while len(Q) > 0:
            source = Q.popleft()
            # A leaf may become isolated.
            if degree_dict[source] == 0:
                if source not in used:   # parent not in dset
                    self.dominating_set.add(source)
                    used.add(source)
                    self.cardinality += 1
                continue
            assert degree_dict[source] == 1
            for target in self.graph.iteradjacent(source):
                if degree_dict[target] > 0:   # this is parent
                    if source not in used:   # parent goes to dset
                        self.dominating_set.add(target)
                        used.add(target)
                        self.cardinality += 1
                        used.update(self.graph.iteradjacent(target))
                    # Remove the edge from source to target.
                    degree_dict[target] -= 1
                    degree_dict[source] -= 1
                    if degree_dict[target] == 1:   # parent is a new leaf
                        Q.append(target)
                    break


class TreeDominatingSet3:
    """Find a minimum dominating set and a maximum 2-stable set for trees.
    
    A single tree is connected during computations.
    
    Based on:
    
    Chang, G.J. (2013). Algorithmic Aspects of Domination in Graphs.
    In: Pardalos, P., Du, DZ., Graham, R. (eds) Handbook of Combinatorial
    Optimization. Springer, New York, NY.
    
    Attributes
    ----------
    graph : input forest
    dominating_set : set with nodes
    cardinality : number (the size of min dset)
    two_stable_set : set with nodes
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.dominating_set = set()
        self.cardinality = 0
        self.two_stable_set = set()

    def run(self):
        """Executable pseudocode."""
        used = set()   # for dset and neighbors
        # A dictionary with node degrees, O(n) time.
        degree_dict = dict((node, self.graph.degree(node))
            for node in self.graph.iternodes())
        Q = collections.deque()   # for leaves
        # Put leafs to the queue, O(n) time.
        for node in self.graph.iternodes():
            if degree_dict[node] == 0:
                self.dominating_set.add(node)   # isolated node from the beginning
                self.two_stable_set.add(node)
                used.add(node)
                self.cardinality += 1
            elif degree_dict[node] == 1:   # leaf
                Q.append(node)
        while len(Q) > 0:
            source = Q.popleft()
            # A leaf may become isolated.
            if degree_dict[source] == 0:
                if source not in used:   # parent is not in dset
                    self.dominating_set.add(source)
                    self.two_stable_set.add(source)
                    used.add(source)
                    self.cardinality += 1
                continue
            assert degree_dict[source] == 1
            for target in self.graph.iteradjacent(source):
                if degree_dict[target] > 0:   # this is parent
                    if source not in used:   # parent goes to dset
                        self.dominating_set.add(target)
                        self.two_stable_set.add(source)
                        used.add(target)
                        self.cardinality += 1
                        used.update(self.graph.iteradjacent(target))
                    # Remove the edge from source to target.
                    degree_dict[target] -= 1
                    degree_dict[source] -= 1
                    if degree_dict[target] == 1:   # parent is a new leaf
                        Q.append(target)
                    break


class TreeDominatingSet4:
    """Find a minimum dominating set and a maximum 2-stable set for trees.
    
    A single tree is connected during computations.
    TreePEO is used to find PEO and parent.
    
    Based on:
    
    Chang, G.J. (2013). Algorithmic Aspects of Domination in Graphs.
    In: Pardalos, P., Du, DZ., Graham, R. (eds) Handbook of Combinatorial
    Optimization. Springer, New York, NY.
    
    Attributes
    ----------
    graph : input forest
    dominating_set : set with nodes
    cardinality : number (the size of min dset)
    two_stable_set : set with nodes
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.dominating_set = set()
        self.cardinality = 0
        self.two_stable_set = set()

    def run(self):
        """Executable pseudocode."""
        algorithm = TreePEO(self.graph)
        algorithm.run()   # O(n) time
        used = set()   # for dset and neighbors
        for source in algorithm.peo:   # other leaves will be here
            target = algorithm.parent[source]
            if target is None:   # tha last node
                if source not in used:   # parent is not in dset
                    self.dominating_set.add(source)
                    self.two_stable_set.add(source)
                    used.add(source)
                    self.cardinality += 1
                continue
            if source not in used:   # parent goes to dset
                self.dominating_set.add(target)
                self.two_stable_set.add(source)
                used.add(target)
                self.cardinality += 1
                used.update(self.graph.iteradjacent(target))


TreeDominatingSet = TreeDominatingSet2

# EOF
