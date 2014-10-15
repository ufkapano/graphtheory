#!/usr/bin/python

from edges import Edge
from dfs import SimpleDFS


class EulerianCycleDFS:
    """Finding an Eulerian cycle."""

    def __init__(self, multigraph):
        """The algorithm initialization."""
        if multigraph.is_directed():
            raise ValueError("graph is directed")
        self.multigraph = multigraph
        if not self._is_eulerian():
            raise ValueError("the multigraph is not eulerian")
        self.eulerian_cycle = list()

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:   # get first random node
            source = self.multigraph.iternodes().next()
        self.multigraph_copy = self.multigraph.copy()
        self.stack = list()
        self._visit(source)
        self.eulerian_cycle = self.stack[1:]
        self.eulerian_cycle.reverse()
        del self.stack
        del self.multigraph_copy

    def _visit(self, source):
        """Visiting node."""
        for target in self.multigraph_copy.iternodes():
            edge = Edge(source, target)
            while self.multigraph_copy.has_edge(edge):
                self.multigraph_copy.del_edge(edge)
                self._visit(target)
        self.stack.append(source)

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
