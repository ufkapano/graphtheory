#!/usr/bin/env python3

try:
    integer_types = (int, long)
    range = xrange
except NameError:   # Python 3
    integer_types = (int,)


class BellmanFord:
    """The Bellman-Ford algorithm for the shortest path problem.
    
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
    >>> from graphtheory.shortestpaths.bellmanford import BellmanFord
    >>> G = Graph(n=10, True)    # an exemplary directed graph
    # Add nodes and edges here.
    >>> algorithm = BellmanFord(G)     # initialization
    >>> algorithm.run(source)     # calculations
    >>> algorithm.parent   # shortest path tree as a dict
    >>> algorithm.distance[target]   # distance from source to target
    >>> algorithm.path(target)   # path from source to target
    
    Notes
    -----
    Based on:
    
    Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C., 2009, 
        Introduction to Algorithms, third edition, The MIT Press, 
        Cambridge, London.
    
    https://en.wikipedia.org/wiki/Bellman-Ford_algorithm
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
        self.distance = dict(((node, float("inf")) for node in self.graph.iternodes()))
        self.source = None

    def run(self, source):
        """Finding shortest paths from the source.
        
        Parameters
        ----------
        source : node
        """
        self.source = source
        self.distance[source] = 0
        for step in range(self.graph.v()-1):   # |V|-1 times
            for edge in self.graph.iteredges():   # O(E) time
                self._relax(edge)
        # Check for negative cycles.
        for edge in self.graph.iteredges():   # O(E) time
            if self.distance[edge.target] > self.distance[edge.source] + edge.weight:
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

# EOF
