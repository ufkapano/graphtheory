#!/usr/bin/python

from Queue import LifoQueue


class EulerianCycleDFS:
    """Finding an Eulerian cycle in a multigraph.
    
    Attributes
    ----------
    graph : input graph
    eulerian_cycle : list of nodes
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
        self._stack = LifoQueue()
        import sys
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v() * 2, recursionlimit))

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:   # get first random node
            source = self.graph.iternodes().next()
        self._visit(source)
        while not self._stack.empty():
            self.eulerian_cycle.append(self._stack.get())
        #del self._stack
        #del self._graph_copy

    def _visit(self, source):
        """Visiting node."""
        while self._graph_copy.outdegree(source) > 0:
            edge = self._graph_copy.iteroutedges(source).next()
            self._graph_copy.del_edge(edge)
            self._visit(edge.target)
        self._stack.put(source)

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
    """Finding an Eulerian cycle in a multigraph.
    
    Attributes
    ----------
    graph : input graph
    eulerian_cycle : list of edges
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
        self._stack = LifoQueue()

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:   # get first random node
            start_edge = self.graph.iteredges().next()
        else:
            start_edge = self.graph.iteroutedges(source).next()
        self._graph_copy.del_edge(start_edge)
        self._visit(start_edge)
        while not self._stack.empty():
            self.eulerian_cycle.append(self._stack.get())
        #del self._stack
        #del self._graph_copy

    def _visit(self, start_edge):
        """Visiting edge."""
        while self._graph_copy.outdegree(start_edge.target) > 0:
            edge = self._graph_copy.iteroutedges(start_edge.target).next()
            self._graph_copy.del_edge(edge)
            self._visit(edge)
        self._stack.put(start_edge)

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
