#!/usr/bin/env python3

import collections


class Hierholzer:
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
    
    https://en.wikipedia.org/wiki/Eulerian_path
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        if not self._is_eulerian():
            raise ValueError("the graph is not eulerian")
        self.eulerian_cycle = list()
        self._graph_copy = self.graph.copy()
        self._stack = collections.deque()

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:   # get first random node
            source = next(self.graph.iternodes())
        self.eulerian_cycle.append(source)
        while True:
            if self._graph_copy.outdegree(source) > 0:
                edge = next(self._graph_copy.iteroutedges(source))
                self._stack.append(source)
                self._graph_copy.del_edge(edge)
                source = edge.target
            else:
                source = self._stack.pop()
                self.eulerian_cycle.append(source)
            if len(self._stack) == 0:
                break
        self.eulerian_cycle.reverse()
        #del self._stack
        #del self._graph_copy

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


class HierholzerWithEdges:
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
    
    https://en.wikipedia.org/wiki/Eulerian_path
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        if not self._is_eulerian():
            raise ValueError("the graph is not eulerian")
        self.eulerian_cycle = list()
        self._graph_copy = self.graph.copy()
        self._stack = collections.deque()

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:   # get first random node
            source = next(self.graph.iternodes())
        while True:
            if self._graph_copy.outdegree(source) > 0:
                edge = next(self._graph_copy.iteroutedges(source))
                self._stack.append(edge)
                self._graph_copy.del_edge(edge)
                source = edge.target
            else:
                edge = self._stack.pop()
                source = edge.source
                self.eulerian_cycle.append(edge)
            if len(self._stack) == 0:
                break
        self.eulerian_cycle.reverse()
        #del self._stack
        #del self._graph_copy

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
