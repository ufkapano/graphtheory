#!/usr/bin/python

from Queue import LifoQueue


class Hierholzer:
    """Finding an Eulerian cycle in a multigraph."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        if not self._is_eulerian():
            raise ValueError("the graph is not eulerian")
        self.eulerian_cycle = list()   # list of nodes
        self.graph_copy = self.graph.copy()
        self.stack = LifoQueue()

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:   # get first random node
            source = self.graph.iternodes().next()
        self.eulerian_cycle.append(source)
        while True:
            if self.graph_copy.outdegree(source) > 0:
                edge = self.graph_copy.iteroutedges(source).next()
                self.stack.put(source)
                self.graph_copy.del_edge(edge)
                source = edge.target
            else:
                source = self.stack.get()
                self.eulerian_cycle.append(source)
            if self.stack.empty():
                break
        self.eulerian_cycle.reverse()
        del self.stack
        del self.graph_copy

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


class HierholzerWithEdges:
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
            source = self.graph.iternodes().next()
        while True:
            if self.graph_copy.outdegree(source) > 0:
                edge = self.graph_copy.iteroutedges(source).next()
                self.stack.put(edge)
                self.graph_copy.del_edge(edge)
                source = edge.target
            else:
                edge = self.stack.get()
                source = edge.source
                self.eulerian_cycle.append(edge)
            if self.stack.empty():
                break
        self.eulerian_cycle.reverse()
        del self.stack
        del self.graph_copy

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
