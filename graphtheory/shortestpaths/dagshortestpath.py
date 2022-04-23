#!/usr/bin/env python3

from graphtheory.structures.edges import Edge
from graphtheory.algorithms.topsort import TopologicalSortDFS


class DAGShortestPath:
    """The shortest path problem for a directed acyclic graph.
    
    Attributes
    ----------
    graph : input weighted directed acyclic graph
    parent : dict with nodes (shortest path tree)
    distance : dict with nodes (distances to source node)
    source : node
    
    Examples
    --------
    >>> from graphtheory.structures.edges import Edge
    >>> from graphtheory.structures.graphs import Graph
    >>> from graphtheory.shortestpaths.dagshortestpath import DAGShortestPath
    >>> G = Graph(n=10, True)    # an exemplary DAG
    # Add nodes and edges here.
    >>> algorithm = DAGShortestPath(G)   # initialization
    >>> algorithm.run(source)   # calculations
    >>> algorithm.parent   # shortest path tree as a dict
    >>> algorithm.distance[target]   # distance from source to target
    >>> algorithm.path(target)   # path from source to target
    
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
        graph : weighted directed acyclic graph
        """
        if not graph.is_directed():
            raise ValueError("graph is not directed")
        self.graph = graph
        # Shortest path tree as a dictionary.
        self.parent = dict((node, None) for node in self.graph.iternodes())
        self.distance = dict((node, float("inf")) for node in self.graph.iternodes())
        self.source = None

    def run(self, source):
        """Finding shortest paths from the source.
        
        Parameters
        ----------
        source : node
        """
        self.source = source
        self.distance[source] = 0
        algorithm = TopologicalSortDFS(self.graph)
        algorithm.run()
        for source in algorithm.sorted_nodes:
            for edge in self.graph.iteroutedges(source):
                self._relax(edge)

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
