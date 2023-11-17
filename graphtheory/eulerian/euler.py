#!/usr/bin/env python3

import sys
import collections


class EulerianCycleDFS:
    """Finding an Eulerian cycle in a multigraph, complexity O(E).
    
    Attributes
    ----------
    graph : input graph
    eulerian_cycle : list of nodes (length |E|+1)
    _graph_copy : graph, private
    _stack : LIFO queue, private
    
    Notes
    -----
    Based on the description from:
    
    http://eduinf.waw.pl./inf/alg/001_search/0135.php
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        if not self._is_eulerian():
            raise ValueError("the graph is not eulerian")
        self.eulerian_cycle = list()
        self._graph_copy = self.graph.copy()
        self._stack = collections.deque()
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v() ** 2, recursionlimit))

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:   # get first random node
            source = next(self.graph.iternodes())
        self._visit(source)
        while len(self._stack) > 0:
            self.eulerian_cycle.append(self._stack.pop())
        #del self._stack
        #del self._graph_copy

    def _visit(self, source):
        """Visiting node."""
        while self._graph_copy.outdegree(source) > 0:
            edge = next(self._graph_copy.iteroutedges(source))
            self._graph_copy.del_edge(edge)
            self._visit(edge.target)
        self._stack.append(source)

    def _is_eulerian(self):
        """Test if the graph is eulerian."""
        if self.graph.is_directed():
            # We assume that the graph is strongly connected.
            for node in self.graph.iternodes():
                if self.graph.indegree(node) != self.graph.outdegree(node):
                    return False
        else:
            # We assume that the graph is connected
            for node in self.graph.iternodes():
                if self.graph.degree(node) % 2 == 1:
                    return False
        return True


class EulerianCycleDFSWithEdges:
    """Finding an Eulerian cycle in a multigraph, complexity O(E).
    
    Attributes
    ----------
    graph : input graph
    eulerian_cycle : list of edges (length |E|)
    _graph_copy : graph, private
    _stack : LIFO queue, private
    
    Notes
    -----
    Based on the description from:
    
    Notes
    -----
    Based on the description from:
    
    http://eduinf.waw.pl./inf/alg/001_search/0135.php
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        if not self._is_eulerian():
            raise ValueError("the graph is not eulerian")
        self.eulerian_cycle = list()
        self._graph_copy = self.graph.copy()
        self._stack = collections.deque()
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v() ** 2, recursionlimit))

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:   # get first random node
            start_edge = next(self.graph.iteredges())
        else:
            start_edge = next(self.graph.iteroutedges(source))
        self._graph_copy.del_edge(start_edge)
        self._visit(start_edge)
        while len(self._stack) > 0:
            self.eulerian_cycle.append(self._stack.pop())
        #del self._stack
        #del self._graph_copy

    def _visit(self, start_edge):
        """Visiting edge."""
        while self._graph_copy.outdegree(start_edge.target) > 0:
            edge = next(self._graph_copy.iteroutedges(start_edge.target))
            self._graph_copy.del_edge(edge)
            self._visit(edge)
        self._stack.append(start_edge)

    def _is_eulerian(self):
        """Test if the graph is eulerian."""
        if self.graph.is_directed():
            # We assume that the graph is strongly connected.
            for node in self.graph.iternodes():
                if self.graph.indegree(node) != self.graph.outdegree(node):
                    return False
        else:
            # We assume that the graph is connected.
            for node in self.graph.iternodes():
                if self.graph.degree(node) % 2 == 1:
                    return False
        return True

# EOF
