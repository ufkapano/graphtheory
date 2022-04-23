#!/usr/bin/env python3

from operator import attrgetter
from graphtheory.structures.unionfind import UnionFind


class KruskalClustering:
    """Kruskal's algorithm used for finding clusters.
    
    Attributes
    ----------
    graph : input undirected weighted graph or multigraph
    n_clusters : the number of clusters given
    uf : disjoint-set data structure
    clusters : a dict with clusters
    """

    def __init__(self, graph, n_clusters):
        """The algorithm initialization.
        
        Parameters
        ----------
        graph : undirected weighted graph or multigraph
        n_clusters : the number of clusters given
        """
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.n_clusters = n_clusters
        self.uf = UnionFind()
        self.clusters = dict()

    def run(self):
        """Finding clusters."""
        for node in self.graph.iternodes():
            self.uf.create(node)
        n_sets = self.graph.v()
        for edge in sorted(self.graph.iteredges(), key=attrgetter("weight")):
            if n_sets == self.n_clusters:
                break
            if self.uf.find(edge.source) != self.uf.find(edge.target):
                self.uf.union(edge.source, edge.target)
                n_sets -= 1
        for node in self.graph.iternodes():
            rep = self.uf.find(node)
            if rep in self.clusters:
                self.clusters[rep].add(node)
            else:
                self.clusters[rep] = set([node])

# EOF
