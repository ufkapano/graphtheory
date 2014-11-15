#!/usr/bin/python

from dfs import SimpleDFS
from bfs import SimpleBFS


class FleuryDFS:
    """Fleury's algorithm for finding an Eulerian cycle."""

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
        node = source
        self.eulerian_cycle.append(node)
        self.multigraph_copy = self.multigraph.copy()
        while self.multigraph_copy.outdegree(node) > 0:
            for edge in list(self.multigraph_copy.iteroutedges(node)):
                # multigraph_copy is changing!
                if not self._is_bridge(edge):
                    break
            self.multigraph_copy.del_edge(edge)
            self.eulerian_cycle.append(edge.target)
            node = edge.target
        del self.multigraph_copy
        self.eulerian_cycle.pop()

    def _is_bridge(self, edge):
        """Bridge test."""
        list1 = list()
        list2 = list()
        algorithm = SimpleDFS(self.multigraph_copy)
        algorithm.run(edge.source, pre_action=lambda node: list1.append(node))
        self.multigraph_copy.del_edge(edge)
        algorithm = SimpleDFS(self.multigraph_copy)
        algorithm.run(edge.source, pre_action=lambda node: list2.append(node))
        self.multigraph_copy.add_edge(edge)
        return len(list1) != len(list2)

    def _is_eulerian(self):
        """Test if the multigraph is eulerian."""
        if self.multigraph.is_directed():
            # We assume that the multigraph is strongly connected.
            for node in self.multigraph.iternodes():
                if self.multigraph.indegree(node) != self.multigraph.outdegree(node):
                    return False
        else:
            # We assume that the multigraph is connected.
            for node in self.multigraph.iternodes():
                if self.multigraph.degree(node) % 2 == 1:
                    return False
        return True


class FleuryBFS:
    """Fleury's algorithm for finding an Eulerian cycle."""

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
        node = source
        self.eulerian_cycle.append(node)
        self.multigraph_copy = self.multigraph.copy()
        while self.multigraph_copy.outdegree(node) > 0:
            for edge in list(self.multigraph_copy.iteroutedges(node)):
                # multigraph_copy is changing!
                if not self._is_bridge(edge):
                    break
            self.multigraph_copy.del_edge(edge)
            self.eulerian_cycle.append(edge.target)
            node = edge.target
        del self.multigraph_copy
        self.eulerian_cycle.pop()

    def _is_bridge(self, edge):
        """Bridge test."""
        list1 = list()
        list2 = list()
        algorithm = SimpleBFS(self.multigraph_copy)
        algorithm.run(edge.source, pre_action=lambda node: list1.append(node))
        self.multigraph_copy.del_edge(edge)
        algorithm = SimpleBFS(self.multigraph_copy)
        algorithm.run(edge.source, pre_action=lambda node: list2.append(node))
        self.multigraph_copy.add_edge(edge)
        return len(list1) != len(list2)

    def _is_eulerian(self):
        """Test if the multigraph is eulerian."""
        if self.multigraph.is_directed():
            # We assume that the multigraph is strongly connected.
            for node in self.multigraph.iternodes():
                if self.multigraph.indegree(node) != self.multigraph.outdegree(node):
                    return False
        else:
            # We assume that the multigraph is connected.
            for node in self.multigraph.iternodes():
                if self.multigraph.degree(node) % 2 == 1:
                    return False
        return True

# EOF
