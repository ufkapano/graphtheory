#!/usr/bin/env python3

try:
    integer_types = (int, long)
    range = xrange
except NameError:   # Python 3
    integer_types = (int,)


class SlowAllPairs:
    """All-pairs shortest paths algorithm in O(V^4) time.
    
    Attributes
    ----------
    graph : input directed weighted graph
    distance : dict-of-dict
    weights : dict-of-dict, private
    
    Examples
    --------
    >>> from graphtheory.structures.edges import Edge
    >>> from graphtheory.structures.graphs import Graph
    >>> from graphtheory.shortestpaths.allpairs import SlowAllPairs
    >>> G = Graph(n=10, True)    # an exemplary directed graph
    # Add nodes and edges here.
    >>> algorithm = SlowAllPairs(G)     # initialization
    >>> algorithm.run()     # calculations
    >>> algorithm.distance[source][target]   # distance from source to target
    
    Notes
    -----
    Based on:
    
    Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C., 2009, 
        Introduction to Algorithms, third edition, The MIT Press, 
        Cambridge, London.
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
        self.weights = dict()
        for source in self.graph.iternodes():   # O(V^2) time
            self.distance[source] = dict()
            for target in self.graph.iternodes():
                self.distance[source][target] = float("inf")
            self.distance[source][source] = 0
        for edge in self.graph.iteredges():   # O(E) time
            self.distance[edge.source][edge.target] = edge.weight
        for source in self.graph.iternodes():
            self.weights[source] = dict(self.distance[source])

    def run(self):
        """Executable pseudocode."""
        for m in range(2, self.graph.v()):   # |V|-2 times
            self.distance = self.extended_shortest_paths(self.distance)
        if any(self.distance[node][node] < 0 for node in self.graph.iternodes()):
            raise ValueError("negative cycle detected")

    def extended_shortest_paths(self, old_distance):
        """O(V^3) time."""
        new_distance = dict()
        for source in self.graph.iternodes():
            new_distance[source] = dict()
            for target in self.graph.iternodes():
                new_distance[source][target] = float("inf")
                for node in self.graph.iternodes():
                    new_distance[source][target] = min(new_distance[source][target],
                        old_distance[source][node] + self.weights[node][target])
        return new_distance


class SlowAllPairsEdges:
    """All-pairs shortest paths algorithm in O(V^2 (V+E)) time.
    
    Attributes
    ----------
    graph : input directed weighted graph
    distance : dict-of-dict
    weights : dict-of-dict, private
    
    Examples
    --------
    >>> from graphtheory.structures.edges import Edge
    >>> from graphtheory.structures.graphs import Graph
    >>> from graphtheory.shortestpaths.allpairs import SlowAllPairsEdges
    >>> G = Graph(n=10, True)    # an exemplary directed graph
    # Add nodes and edges here.
    >>> algorithm = SlowAllPairsEdges(G)     # initialization
    >>> algorithm.run()     # calculations
    >>> algorithm.distance[source][target]   # distance from source to target
    
    Notes
    -----
    Based on:
    
    Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C., 2009, 
        Introduction to Algorithms, third edition, The MIT Press, 
        Cambridge, London.
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
        self.weights = dict()
        for source in self.graph.iternodes():   # O(V^2) time
            self.distance[source] = dict()
            for target in self.graph.iternodes():
                self.distance[source][target] = float("inf")
            self.distance[source][source] = 0
        for edge in self.graph.iteredges():   # O(E) time
            self.distance[edge.source][edge.target] = edge.weight
        for source in self.graph.iternodes():
            self.weights[source] = dict(self.distance[source])

    def run(self):
        """Executable pseudocode."""
        for m in range(2, self.graph.v()):   # |V|-2 times
            self.distance = self.extended_shortest_paths(self.distance)
        if any(self.distance[node][node] < 0 for node in self.graph.iternodes()):
            raise ValueError("negative cycle detected")

    def extended_shortest_paths(self, old_distance):
        """O(V*(V+E)) time."""
        new_distance = dict()
        for source in self.graph.iternodes():   # |V| times
            new_distance[source] = dict(old_distance[source]) # IMPORTANT, O(V)
            for edge in self.graph.iteredges():   # O(E) time
                new_distance[source][edge.target] = min(
                    new_distance[source][edge.target],
                    old_distance[source][edge.source] + edge.weight)
        return new_distance


class SlowAllPairsWithPaths:   # not for FasterAllPairsSP
    """All-pairs shortest paths algorithm in O(V^4) time.
    
    Attributes
    ----------
    graph : input directed weighted graph
    distance : dict-of-dict
    weights : dict-of-dict, private
    parent : dict with nodes
    
    Examples
    --------
    >>> from graphtheory.structures.edges import Edge
    >>> from graphtheory.structures.graphs import Graph
    >>> from graphtheory.shortestpaths.allpairs import SlowAllPairsWithPaths
    >>> G = Graph(n=10, True)    # an exemplary directed graph
    # Add nodes and edges here.
    >>> algorithm = SlowAllPairsWithPaths(G)     # initialization
    >>> algorithm.run()     # calculations
    >>> algorithm.distance[source][target]   # distance from source to target
    >>> algorithm.path(source, target)   # path from source to target
    
    Notes
    -----
    Based on:
    
    Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C., 2009, 
        Introduction to Algorithms, third edition, The MIT Press, 
        Cambridge, London.
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
        self.weights = dict()
        self.parent = dict()
        for source in self.graph.iternodes():   # O(V^2) time
            self.distance[source] = dict()
            self.parent[source] = dict()
            for target in self.graph.iternodes():
                self.distance[source][target] = float("inf")
                self.parent[source][target] = None
            self.distance[source][source] = 0
        for edge in self.graph.iteredges():   # O(E) time
            self.distance[edge.source][edge.target] = edge.weight
            self.parent[edge.source][edge.target] = edge.source
        for source in self.graph.iternodes():
            self.weights[source] = dict(self.distance[source])

    def run(self):
        """Executable pseudocode."""
        for m in range(2, self.graph.v()):   # |V|-2 times
            self.distance = self.extended_shortest_paths(self.distance)
        if any(self.distance[node][node] < 0 for node in self.graph.iternodes()):
            raise ValueError("negative cycle detected")

    def extended_shortest_paths(self, old_distance):
        """O(V^3) time."""
        new_distance = dict()
        for source in self.graph.iternodes():
            new_distance[source] = dict(old_distance[source]) # IMPORTANT, copy
            for target in self.graph.iternodes():
                for node in self.graph.iternodes():
                    alt = old_distance[source][node] + self.weights[node][target]
                    if new_distance[source][target] > alt:
                        new_distance[source][target] = alt
                        self.parent[source][target] = node
        return new_distance

    def path(self, source, target):
        """Path reconstruction."""
        if source == target:
            return [source]
        elif self.parent[source][target] is None:
            raise ValueError("no path to target")
        else:
            return self.path(source, self.parent[source][target]) + [target]


class FasterAllPairs:
    """All-pairs shortest paths algorithm in O(V^3 log V) time.
    
    Attributes
    ----------
    graph : input directed weighted graph
    distance : dict-of-dict
    
    Examples
    --------
    >>> from graphtheory.structures.edges import Edge
    >>> from graphtheory.structures.graphs import Graph
    >>> from graphtheory.shortestpaths.allpairs import FasterAllPairs
    >>> G = Graph(n=10, True)    # an exemplary directed graph
    # Add nodes and edges here.
    >>> algorithm = FasterAllPairs(G)     # initialization
    >>> algorithm.run()     # calculations
    >>> algorithm.distance[source][target]   # distance from source to target
    
    Notes
    -----
    Based on:
    
    Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C., 2009, 
        Introduction to Algorithms, third edition, The MIT Press, 
        Cambridge, London.
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
        for source in self.graph.iternodes():   # O(V^2) time
            self.distance[source] = dict()
            for target in self.graph.iternodes():
                self.distance[source][target] = float("inf") # IMPORTANT
            self.distance[source][source] = 0
        for edge in self.graph.iteredges():   # O(E) time
            self.distance[edge.source][edge.target] = edge.weight

    def run(self):
        """Executable pseudocode."""
        m = 1
        while m < (self.graph.v() - 1):   # log(V) times
            self.distance = self.extended_shortest_paths(self.distance)
            m = 2 * m
        if any(self.distance[node][node] < 0 for node in self.graph.iternodes()):
            raise ValueError("negative cycle detected")

    def extended_shortest_paths(self, old_distance):
        """O(V^3) time."""
        new_distance = dict()
        for source in self.graph.iternodes():
            new_distance[source] = dict()
            for target in self.graph.iternodes():
                new_distance[source][target] = float("inf")
                for node in self.graph.iternodes():
                    new_distance[source][target] = min(new_distance[source][target],
                        old_distance[source][node] + old_distance[node][target])
        return new_distance

# EOF
