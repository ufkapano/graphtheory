#!/usr/bin/python

from edges import Edge
from Queue import Queue


class BipartiteGraphBFS:
    """Bipartite graphs detection based on BFS, O(V+E) time."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("graph is directed")
        self.graph = graph
        # colors are 0 and 1
        self.color = dict(((node, None) for node in self.graph.iternodes()))

    def run(self, source=None):
        """Executable pseudocode."""
        if source is not None:
            self._visit(source)
        else:
            for node in self.graph.iternodes():
                if self.color[node] is None:
                    self._visit(node)

    def _visit(self, node):
        """Explore the connected component."""
        Q = Queue()
        self.color[node] = 0   # before Q.put
        Q.put(node)
        while not Q.empty():
            source = Q.get()
            for edge in self.graph.iteroutedges(source):
                if self.color[edge.target] is None:
                    self.color[edge.target] = (self.color[source] + 1) % 2  # before Q.put
                    Q.put(edge.target)
                else:   # target was visited
                    if self.color[edge.target] == self.color[source]:
                        raise ValueError("graph is not bipartite")


class BipartiteGraphDFS:
    """Bipartite graphs detection based on DFS, O(V+E) time."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("graph is directed")
        self.graph = graph
        # colors are 0 and 1
        self.color = dict(((node, None) for node in self.graph.iternodes()))
        import sys
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v() * 2, recursionlimit))

    def run(self, source=None):
        """Executable pseudocode."""
        if source is not None:
            self.color[source] = 0   # before _visit
            self._visit(source)
        else:
            for node in self.graph.iternodes():
                if self.color[node] is None:
                    self.color[node] = 0   # before _visit
                    self._visit(node)

    def _visit(self, node):
        """Explore recursively the connected component."""
        for edge in self.graph.iteroutedges(node):
            if self.color[edge.target] is None:
                self.color[edge.target] = (self.color[node] + 1) % 2  # before _visit
                self._visit(edge.target)
            else:   # target was visited
                if self.color[edge.target] == self.color[node]:
                    raise ValueError("graph is not bipartite")

# EOF
