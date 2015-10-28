#!/usr/bin/python

from Queue import PriorityQueue
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
    
    Kruskal, J. B., 1956, On the shortest spanning subtree of a graph 
    and the traveling salesman prob lem, Proc. Amer. Math. Soc. 7, 48-50. 
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

# EOF
