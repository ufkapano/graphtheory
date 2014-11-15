#!/usr/bin/python

from Queue import LifoQueue
from edges import Edge
from dfs import SimpleDFS


class EulerianCycleDFS:
    """Finding an Eulerian cycle."""

    def __init__(self, multigraph):
        """The algorithm initialization."""
        self.multigraph = multigraph
        if not self._is_eulerian():
            raise ValueError("the multigraph is not eulerian")
        self.eulerian_cycle = list()

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:   # get first random node
            source = self.multigraph.iternodes().next()
        self.multigraph_copy = self.multigraph.copy()
        self.stack = LifoQueue()
        self._visit(source)
        while not self.stack.empty():
            self.eulerian_cycle.append(self.stack.get())
        #self.eulerian_cycle.pop()
        del self.stack
        del self.multigraph_copy

    def _visit(self, source):
        """Visiting node."""
        while self.multigraph_copy.outdegree(source) > 0:
            edge = self.multigraph_copy.iteroutedges(source).next()
            self.multigraph_copy.del_edge(edge)
            self._visit(edge.target)
        self.stack.put(source)

    def _is_eulerian(self):
        """Test if the multigraph is eulerian."""
        if self.multigraph.is_directed():
            # we assume that the multigraph is strongly connected
            for node in self.multigraph.iternodes():
                if self.multigraph.indegree(node) != self.multigraph.outdegree(node):
                    return False
        else:
            # we assume that the multigraph is connected
            for node in self.multigraph.iternodes():
                if self.multigraph.degree(node) % 2 == 1:
                    return False
        return True


class Hierholzer:
    """Finding an Eulerian cycle."""

    def __init__(self, multigraph):
        """The algorithm initialization."""
        self.multigraph = multigraph
        if not self._is_eulerian():
            raise ValueError("the multigraph is not eulerian")
        self.eulerian_cycle = list()

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:   # get first random node
            source = self.multigraph.iternodes().next()
        self.multigraph_copy = self.multigraph.copy()
        self.stack = LifoQueue()
        self.eulerian_cycle.append(source)
        while True:
            if self.multigraph_copy.outdegree(source) > 0:
                edge = self.multigraph_copy.iteroutedges(source).next()
                self.stack.put(source)
                self.multigraph_copy.del_edge(edge)
                source = edge.target
            else:
                source = self.stack.get()
                self.eulerian_cycle.append(source)
            if self.stack.empty():
                break
        self.eulerian_cycle.reverse()
        #self.eulerian_cycle.pop()
        del self.stack
        del self.multigraph_copy

    def _is_eulerian(self):
        """Test if the multigraph is eulerian."""
        if self.multigraph.is_directed():
            # we assume that the multigraph is strongly connected
            for node in self.multigraph.iternodes():
                if self.multigraph.indegree(node) != self.multigraph.outdegree(node):
                    return False
        else:
            # we assume that the multigraph is connected
            for node in self.multigraph.iternodes():
                if self.multigraph.degree(node) % 2 == 1:
                    return False
        return True

# EOF
