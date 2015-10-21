#!/usr/bin/python

from Queue import LifoQueue


class EulerianCycleDFS:
    """Finding an Eulerian cycle in a multigraph."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        if not self._is_eulerian():
            raise ValueError("the graph is not eulerian")
        self.eulerian_cycle = list()
        self.graph_copy = self.graph.copy()
        self.stack = LifoQueue()
        import sys
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v() * 2, recursionlimit))

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:   # get first random node
            source = self.graph.iternodes().next()
        self._visit(source)
        while not self.stack.empty():
            self.eulerian_cycle.append(self.stack.get())
        del self.stack
        del self.graph_copy

    def _visit(self, source):
        """Visiting node."""
        while self.graph_copy.outdegree(source) > 0:
            edge = self.graph_copy.iteroutedges(source).next()
            self.graph_copy.del_edge(edge)
            self._visit(edge.target)
        self.stack.put(source)

    def _is_eulerian(self):
        """Test if the graph is eulerian."""
        if self.graph.is_directed():
            # we assume that the graph is strongly connected
            for node in self.graph.iternodes():
                if self.graph.indegree(node) != self.graph.outdegree(node):
                    return False
        else:
            # we assume that the graph is connected
            for node in self.graph.iternodes():
                if self.graph.degree(node) % 2 == 1:
                    return False
        return True


class EulerianCycleDFSWithEdges:
    """Finding an Eulerian cycle in a multigraph."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        if not self._is_eulerian():
            raise ValueError("the graph is not eulerian")
        self.eulerian_cycle = list()   # list of edges
        self.graph_copy = self.graph.copy()
        self.stack = LifoQueue()

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:   # get first random node
            start_edge = self.graph.iteredges().next()
        else:
            start_edge = self.graph.iteroutedges(source).next()
        self.graph_copy.del_edge(start_edge)
        self._visit(start_edge)
        while not self.stack.empty():
            self.eulerian_cycle.append(self.stack.get())
        del self.stack
        del self.graph_copy

    def _visit(self, start_edge):
        """Visiting edge."""
        while self.graph_copy.outdegree(start_edge.target) > 0:
            edge = self.graph_copy.iteroutedges(start_edge.target).next()
            self.graph_copy.del_edge(edge)
            self._visit(edge)
        self.stack.put(start_edge)

    def _is_eulerian(self):
        """Test if the graph is eulerian."""
        if self.graph.is_directed():
            # we assume that the graph is strongly connected
            for node in self.graph.iternodes():
                if self.graph.indegree(node) != self.graph.outdegree(node):
                    return False
        else:
            # we assume that the graph is connected
            for node in self.graph.iternodes():
                if self.graph.degree(node) % 2 == 1:
                    return False
        return True

# EOF
