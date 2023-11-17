#!/usr/bin/env python3

import sys
import collections


class BipartiteGraphBFS:
    """Bipartite graphs detection based on BFS, O(V+E) time.
    
    Attributes
    ----------
    graph : input bipartite graph or multigraph
    color : dict with nodes (values are colors)
    
    Notes
    -----
    Colors are 0 and 1.
    """

    def __init__(self, graph):
        """The algorithm initialization.
        
        Parameters
        ----------
        graph : undirected graph or multigraph
        """
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.color = dict((node, None) for node in self.graph.iternodes())

    def run(self, source=None):
        """Node coloring using BFS."""
        if source is not None:
            self._visit(source)
        else:
            for node in self.graph.iternodes():
                if self.color[node] is None:
                    self._visit(node)

    def _visit(self, node):
        """Explore the connected component."""
        queue = collections.deque()
        self.color[node] = 0   # before Q.append
        queue.append(node)
        while len(queue) > 0:
            source = queue.popleft()
            for target in self.graph.iteradjacent(source):
                if self.color[target] is None:
                    self.color[target] = (self.color[source] + 1) % 2  # before Q.append
                    queue.append(target)
                else:   # target was visited
                    if self.color[target] == self.color[source]:
                        raise ValueError("the graph is not bipartite")


class BipartiteGraphDFS:
    """Bipartite graphs detection based on DFS, O(V+E) time.
    
    Attributes
    ----------
    graph : input bipartite graph or multigraph
    color : dict with nodes (values are colors)
    
    Notes
    -----
    Colors are 0 and 1.
    """

    def __init__(self, graph):
        """The algorithm initialization.
        
        Parameters
        ----------
        graph : undirected graph or multigraph
        """
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.color = dict(((node, None) for node in self.graph.iternodes()))
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v() * 2, recursionlimit))

    def run(self, source=None):
        """Node coloring using DFS."""
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
        for target in self.graph.iteradjacent(node):
            if self.color[target] is None:
                self.color[target] = (self.color[node] + 1) % 2  # before _visit
                self._visit(target)
            else:   # target was visited
                if self.color[target] == self.color[node]:
                    raise ValueError("the graph is not bipartite")


def is_bipartite(graph):
    """Bipartite graphs detection."""
    try:
        algorithm = BipartiteGraphBFS(graph)   # no recursion
        algorithm.run()
        return True
    except ValueError:
        return False

# EOF
