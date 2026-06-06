#!/usr/bin/env python3

import collections


class ShortestPathFasterAlgorithm:
    """The SPFA algorithm for the shortest path problem.
    
    Attributes
    ----------
    graph : input directed weighted graph
    parent : dict with nodes (shortest path tree)
    distance : dict with nodes (distances to source node)
    source : node
    
    Examples
    --------
    >>> from graphtheory.structures.edges import Edge
    >>> from graphtheory.structures.graphs import Graph
    >>> from graphtheory.shortestpaths.spfa import ShortestPathFasterAlgorithm
    >>> G = Graph(n=10, directed=True)    # an exemplary directed graph
    # Add nodes and edges here.
    >>> algorithm = ShortestPathFasterAlgorithm(G)     # initialization
    >>> algorithm.run(source)     # calculations
    >>> algorithm.parent   # shortest path tree as a dict
    >>> algorithm.distance[target]   # distance from source to target
    >>> algorithm.path(target)   # path from source to target
    >>> algorithm.path_iter(target)   # path from source to target
    
    Notes
    -----
    Based on:
    
    https://en.wikipedia.org/wiki/Bellman-Ford_algorithm#Improvements

    https://www.geeksforgeeks.org/dsa/shortest-path-faster-algorithm/
    """

    def __init__(self, graph):
        """The algorithm initialization.
        
        Parameters
        ----------
        graph : directed weighted graph
        """
        if not graph.is_directed():
            raise ValueError("the graph is not directed")
        self.graph = graph
        # Shortest path tree as a dictionary.
        self.parent = dict(((node, None) for node in self.graph.iternodes()))
        self.distance = dict(((node, float("inf"))
                              for node in self.graph.iternodes()))
        self.source = None

    def run(self, source):
        """Finding shortest paths from the source.
        
        Parameters
        ----------
        source : node
        """
        self.source = source
        self.distance[source] = 0

        queue = collections.deque()
        queue.append(self.source)
        in_queue = dict((node, False) for node in self.graph.iternodes())
        in_queue[self.source] = True

        while len(queue) > 0:   # worstcase: O(V) time
            node = queue.popleft()
            in_queue[node] = False
            for edge in self.graph.iteroutedges(node):   # O(E) time
                if self._relax(edge):
                    if not in_queue[edge.target]:
                        queue.append(edge.target)
                        in_queue[edge.target] = True
        # Check for negative cycles.
        for edge in self.graph.iteredges():   # O(E) time
            if (self.distance[edge.target] >
                    self.distance[edge.source] + edge.weight):
                raise ValueError("negative cycle detected")

    def _relax(self, edge):
        """Edge relaxation."""
        alt = self.distance[edge.source] + edge.weight
        if self.distance[edge.target] > alt:
            self.distance[edge.target] = alt
            self.parent[edge.target] = edge.source
            return True
        return False

    def path(self, target):
        """Construct a path from source to target."""
        if self.source == target:
            return [self.source]
        elif self.parent[target] is None:
            raise ValueError("no path to target")
        else:
            return self.path(self.parent[target]) + [target]

    def path_iter(self, target):
        """Construct a path from source to target."""
        if self.distance[target] == float("inf"):
            raise ValueError("no path to target")
        path = [target]
        while self.parent[target] is not None:
            target = self.parent[target]
            path.append(target)
        path.reverse()
        return path
