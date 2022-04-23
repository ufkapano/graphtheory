#!/usr/bin/env python3

from graphtheory.structures.edges import Edge
from graphtheory.structures.unionfind import UnionFind


class BoruvkaMST:
    """Boruvka's algorithm for finding a minimum spanning tree.
    
    Attributes
    ----------
    graph : input undirected graph or multigraph
    mst : graph (MST)
    _uf : disjoint-set data structure, private
    
    Examples
    --------
    >>> from graphtheory.structures.edges import Edge
    >>> from graphtheory.structures.graphs import Graph
    >>> from graphtheory.spanningtrees.boruvka import BoruvkaMST
    >>> G = Graph(n=10, False) # an exemplary undirected graph
    # Add nodes and edges here.
    >>> algorithm = BoruvkaMST(G)
    >>> algorithm.run()     # calculations
    >>> algorithm.mst.show()     # MST as an undirected graph
    
    Notes
    -----
    Based on pseudocode from Wikipedia:
    
    https://en.wikipedia.org/wiki/Boruvka's_algorithm
    
    https://en.wikipedia.org/wiki/Minimum_spanning_tree
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
        forest = set(self.graph.iternodes())
        dummy_edge = Edge(None, None, float("inf"))
        new_len = len(forest)
        old_len = new_len + 1
        while old_len > new_len:
            old_len = new_len
            min_edges = dict(((node, dummy_edge) for node in forest))
            # Finding the cheapest edges.
            for edge in self.graph.iteredges(): # O(E) time
                source = self._uf.find(edge.source)
                target = self._uf.find(edge.target)
                if source != target:   # different components
                    if edge < min_edges[source]:
                        min_edges[source] = edge
                    if edge < min_edges[target]:
                        min_edges[target] = edge
            # Connecting components, total time is O(V).
            for node in min_edges:
                edge = min_edges[node]
                if edge is dummy_edge: # a disconnected graph
                    continue
                source = self._uf.find(edge.source)
                target = self._uf.find(edge.target)
                if source != target:   # different components
                    self._uf.union(source, target)
                    self.mst.add_edge(edge)
            # Remove duplicates, total time is O(V).
            forest = set(self._uf.find(node) for node in forest)
            new_len = len(forest)
            if new_len == 1:   # a connected graph
                break

    def to_tree(self):
        """Return the minimum spanning tree."""
        return self.mst

# EOF
