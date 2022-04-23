#!/usr/bin/env python3

class FloydWarshall:
    """The Floyd-Warshall algorithm (all-pairs shortest paths).
    
    Negative cycles are forbidden.
    
    Attributes
    ----------
    graph : input directed weighted graph
    distance : dict-of-dict
    
    Examples
    --------
    >>> from graphtheory.structures.edges import Edge
    >>> from graphtheory.structures.graphs import Graph
    >>> from graphtheory.shortestpaths.floydwarshall import FloydWarshall
    >>> G = Graph(n=10, True)    # an exemplary directed graph
    # Add nodes and edges here.
    >>> algorithm = FloydWarshall(G)     # initialization
    >>> algorithm.run()     # calculations
    >>> algorithm.distance[source][target]   # distance from source to target
    
    Notes
    -----
    Based on:
    
    Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C., 2009, 
        Introduction to Algorithms, third edition, The MIT Press, 
        Cambridge, London.
    
    https://en.wikipedia.org/wiki/Floyd-Warshall_algorithm
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
        self.distance = dict()
        for source in self.graph.iternodes():
            self.distance[source] = dict()
            for target in self.graph.iternodes():
                self.distance[source][target] = float("inf")
            self.distance[source][source] = 0
        for edge in self.graph.iteredges():
            self.distance[edge.source][edge.target] = edge.weight

    def run(self):
        """Finding all shortest paths."""
        for node in self.graph.iternodes():
            for source in self.graph.iternodes():
                for target in self.graph.iternodes():
                    self.distance[source][target] = min(
                        self.distance[source][target],
                        self.distance[source][node] 
                        + self.distance[node][target])
        if any(self.distance[node][node] < 0 
            for node in self.graph.iternodes()):
                raise ValueError("negative cycle detected")


class FloydWarshallPaths:
    """The Floyd-Warshall algorithm with path reconstruction.
    
    Negative cycles are forbidden.
    
    Attributes
    ----------
    graph : input directed weighted graph
    parent : dict-of-dict
    distance : dict-of-dict
    
    Examples
    --------
    >>> from graphtheory.structures.edges import Edge
    >>> from graphtheory.structures.graphs import Graph
    >>> from graphtheory.shortestpaths.floydwarshall import FloydWarshallPaths
    >>> G = Graph(n=10, True)    # an exemplary directed graph
    # Add nodes and edges here.
    >>> algorithm = FloydWarshallPaths(G)     # initialization
    >>> algorithm.run()     # calculations
    >>> algorithm.distance[source][target]   # distance from source to target
    >>> algorithm.path(source, target)   # path from source to target
    
    Notes
    -----
    Based on:
    
    Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C., 2009, 
        Introduction to Algorithms, third edition, The MIT Press, 
        Cambridge, London.
    
    https://en.wikipedia.org/wiki/Floyd-Warshall_algorithm
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
        self.distance = dict()
        self.parent = dict()
        for source in self.graph.iternodes():
            self.distance[source] = dict()
            self.parent[source] = dict()
            for target in self.graph.iternodes():
                self.distance[source][target] = float("inf")
                self.parent[source][target] = None
            self.distance[source][source] = 0
        for edge in self.graph.iteredges():
            self.distance[edge.source][edge.target] = edge.weight
            self.parent[edge.source][edge.target] = edge.source

    def run(self):
        """Finding all shortest paths."""
        for node in self.graph.iternodes():
            for source in self.graph.iternodes():
                for target in self.graph.iternodes():
                    alt = self.distance[source][node] \
                        + self.distance[node][target]
                    if self.distance[source][target] > alt:
                        self.distance[source][target] = alt
                        self.parent[source][target] = self.parent[node][target]
        if any(self.distance[node][node] < 0
            for node in self.graph.iternodes()):
                raise ValueError("negative cycle detected")

    def path(self, source, target):
        """Path reconstruction."""
        if source == target:
            return [source]
        elif self.parent[source][target] is None:
            raise ValueError("no path to target")
        else:
            return self.path(source, self.parent[source][target]) + [target]


class FloydWarshallAllGraphs:
    """The Floyd-Warshall algorithm, nonnegative edge weights.
    
    Negative cycles are forbidden.
    
    Attributes
    ----------
    graph : input weighted graph (directed or undirected)
    distance : dict-of-dict
    
    Examples
    --------
    >>> from graphtheory.structures.edges import Edge
    >>> from graphtheory.structures.graphs import Graph
    >>> from graphtheory.shortestpaths.floydwarshall \
        import FloydWarshallAllGraphs
    >>> G = Graph(n=10, True)    # an exemplary directed graph
    # Add nodes and edges here.
    >>> algorithm = FloydWarshallAllGraphs(G)   # initialization
    >>> algorithm.run()     # calculations
    >>> algorithm.distance[source][target]   # distance from source to target
    
    Notes
    -----
    Based on:
    
    Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C., 2009, 
        Introduction to Algorithms, third edition, The MIT Press, 
        Cambridge, London.
    
    https://en.wikipedia.org/wiki/Floyd-Warshall_algorithm
    """

    def __init__(self, graph):
        """The algorithm initialization.
        
        Parameters
        ----------
        graph : directed or undirected weighted graph
        """
        self.graph = graph
        self.distance = dict()
        for source in self.graph.iternodes():
            self.distance[source] = dict()
            for target in self.graph.iternodes():
                self.distance[source][target] = float("inf")
            self.distance[source][source] = 0
        if self.graph.is_directed():
            for edge in self.graph.iteredges():
                self.distance[edge.source][edge.target] = edge.weight
        else:
            for edge in self.graph.iteredges():
                self.distance[edge.source][edge.target] = edge.weight
                self.distance[edge.target][edge.source] = edge.weight

    def run(self):
        """Finding all shortest paths."""
        for node in self.graph.iternodes():
            for source in self.graph.iternodes():
                for target in self.graph.iternodes():
                    self.distance[source][target] = min(
                        self.distance[source][target],
                        self.distance[source][node] 
                        + self.distance[node][target])
        if any(self.distance[node][node] < 0 
            for node in self.graph.iternodes()):
                raise ValueError("negative cycle detected")

# EOF
