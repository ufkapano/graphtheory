#!/usr/bin/env python3

try:
    from Queue import PriorityQueue
except ImportError:   # Python 3
    from queue import PriorityQueue

from graphtheory.structures.unionfind import UnionFind


class KruskalMST:
    """Kruskal's algorithm for finding a minimum spanning tree.
    
    Attributes
    ----------
    graph : input undirected graph or multigraph
    mst : graph (MST)
    _uf : disjoint-set data structure, private
    _pq : priority queue, private
    
    Examples
    --------
    >>> from graphtheory.structures.edges import Edge
    >>> from graphtheory.structures.graphs import Graph
    >>> from graphtheory.spanningtrees.kruskal import KruskalMST
    >>> G = Graph(n=10, False) # an exemplary undirected graph
    # Add nodes and edges here.
    >>> algorithm = KruskalMST(G)     # initialization
    >>> algorithm.run()         # calculations
    >>> algorithm.mst.show()   # MST as an undirected graph
    
    Notes
    -----
    Based on:
    
    Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C., 2009, 
        Introduction to Algorithms, third edition, The MIT Press, 
        Cambridge, London.
    
    https://en.wikipedia.org/wiki/Kruskal's_algorithm
    
    J. B. Kruskal, On the shortest spanning subtree of a graph 
        and the traveling salesman problem,
        Proc. Amer. Math. Soc. 7, 48-50 (1956).
    """

    def __init__(self, graph):
        """The algorithm initialization.
        
        Parameters
        ----------
        graph : undirected weighted graph or multigraph
        """
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.mst = self.graph.__class__(self.graph.v())
        for node in self.graph.iternodes():   # isolated nodes are possible
            self.mst.add_node(node)
        self._uf = UnionFind()
        self._pq = PriorityQueue()

    def run(self):
        """Finding MST."""
        for node in self.graph.iternodes():
            self._uf.create(node)
        for edge in self.graph.iteredges():
            self._pq.put((edge.weight, edge))
        while not self._pq.empty():
            _, edge = self._pq.get()
            if self._uf.find(edge.source) != self._uf.find(edge.target):
                self._uf.union(edge.source, edge.target)
                self.mst.add_edge(edge)

    def to_tree(self):
        """Compatibility with other classes."""
        return self.mst


class KruskalMSTSorted:
    """Kruskal's algorithm for finding a minimum spanning tree.
    
    Attributes
    ----------
    graph : input undirected graph or multigraph
    mst : graph (MST)
    _uf : disjoint-set data structure, private
    
    Examples
    --------
    >>> from graphtheory.structures.edges import Edge
    >>> from graphtheory.structures.graphs import Graph
    >>> from graphtheory.spanningtrees.kruskal import KruskalMSTSorted
    >>> G = Graph(n=10, False) # an exemplary undirected graph
    # Add nodes and edges here.
    >>> algorithm = KruskalMSTSorted(G)     # initialization
    >>> algorithm.run()         # calculations
    >>> algorithm.mst.show()   # MST as an undirected graph
    
    Notes
    -----
    Based on:
    
    Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C., 2009, 
        Introduction to Algorithms, third edition, The MIT Press, 
        Cambridge, London.
    
    https://en.wikipedia.org/wiki/Kruskal's_algorithm
    
    J. B. Kruskal, On the shortest spanning subtree of a graph 
        and the traveling salesman problem,
        Proc. Amer. Math. Soc. 7, 48-50 (1956).
    
    D. Eppstein, Kruskal's algorithm for minimum spanning trees, 2006,
        https://www.ics.uci.edu/~eppstein/PADS/MinimumSpanningTree.py
    """

    def __init__(self, graph):
        """The algorithm initialization.
        
        Parameters
        ----------
        graph : undirected weighted graph or multigraph
        """
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.mst = self.graph.__class__(self.graph.v())
        for node in self.graph.iternodes():   # isolated nodes are possible
            self.mst.add_node(node)
        self._uf = UnionFind()

    def run(self):
        """Finding MST."""
        for node in self.graph.iternodes():
            self._uf.create(node)
        #for edge in sorted(self.graph.iteredges()):   # very slow
        #for (_, edge) in sorted((edge.weight, edge) for edge in self.graph.iteredges()):
        from operator import attrgetter
        for edge in sorted(self.graph.iteredges(), key=attrgetter("weight")):
            if self._uf.find(edge.source) != self._uf.find(edge.target):
                self._uf.union(edge.source, edge.target)
                self.mst.add_edge(edge)

    def to_tree(self):
        """Compatibility with other classes."""
        return self.mst

# EOF
