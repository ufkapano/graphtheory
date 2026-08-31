#!/usr/bin/env python3

import sys
from graphtheory.traversing.dfs import SimpleDFS


class TrivialCutEdge:
    """Trivial bridge-finding algorithm, O(E*(V+E)) time.
    
    Attributes
    ----------
    graph : input undirected graph
    cut_edges : list of nodes
    
    Notes
    -----
    Based on the description from:
    
    http://eduinf.waw.pl/inf/alg/001_search/0130a.php
    
    https://en.wikipedia.org/wiki/Bridge_(graph_theory)
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.cut_edges = []

    def run(self, source=None):
        """Executable pseudocode."""
        old_ncc = self._find_ncc()
        for edge in list(self.graph.iteredges()):
            # Warning! You can not iterate over edges and remove edges!
            self.graph.del_edge(edge)
            #print("removed {}".format(edge))
            new_ncc = self._find_ncc()
            #print("new_ncc {}".format(new_ncc))
            self.graph.add_edge(edge)
            if new_ncc > old_ncc:
                self.cut_edges.append(edge)

    def _find_ncc(self):
        """Return the number of connected components."""
        visited = dict((node, False) for node in self.graph.iternodes())
        ncc = 0
        algorithm = SimpleDFS(self.graph)
        for source in self.graph.iternodes():
            #print("source {}".format(source))
            if not visited[source]:
                #print("not visited {}".format(source))
                algorithm.run(source, pre_action=lambda node:
                    visited.__setitem__(node, True))
                ncc += 1
        return ncc


class TarjanCutEdge:
    """Tarjan's bridge-finding algorithm, O(V+E) time.
    
    Attributes
    ----------
    graph : input undirected graph
    cut_edges : list of nodes
    low : dict with nodes
    parent : dict with nodes (DFS tree)
    time : number, private
    dd : dict with nodes (values are numbers, time stamps), private
    dag : graph (DFS tree)
    
    Notes
    -----
    Based on the description from:
    
    http://eduinf.waw.pl/inf/alg/001_search/0130a.php
    
    https://en.wikipedia.org/wiki/Bridge_(graph_theory)
    
    R. E. Tarjan, A note on finding the bridges of a graph,
        Information Processing Letters 2, 160-161 (1974).
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.cut_edges = []
        # Parametr dla wierzcholka wprowadzony przez Tarjana.
        self.low = dict(((node, None) for node in self.graph.iternodes()))
        self.parent = dict(((node, None) for node in self.graph.iternodes()))
        self.time = 0    # time stamp
        self.dd = dict(((node, 0) for node in self.graph.iternodes()))
        self.dag = self.graph.__class__(n=self.graph.v(), directed=True)
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v() * 2, recursionlimit))

    def run(self, source=None):
        """Executable pseudocode."""
        if source is not None:
            self._visit(source)
        else:
            for node in self.graph.iternodes():
                if self.dd[node] == 0:   # not visited
                    self._visit(node)

    def _visit(self, node):
        """Explore recursively the connected component."""
        self.time += 1
        self.dd[node] = self.time
        self.low[node] = self.time
        for edge in self.graph.iteroutedges(node):
            if (self.parent[node] is not None and
                edge.target == self.parent[node]):
                continue   # self.parent[node] is None for root
            if self.dd[edge.target] == 0:   # not visited
                self.parent[edge.target] = node
                self.dag.add_edge(edge)
                self._visit(edge.target)
                self.low[node] = min(self.low[node], self.low[edge.target])
            else:   # back edge
                self.low[node] = min(self.low[node], self.dd[edge.target])
        # All neighbors are visited. Check the bridge condition.
        if self.parent[node] is not None and self.low[node] == self.dd[node]:
            # Most to jest krawedz prowadzaca do node od jego rodzica.
            # Tu jest klopotliwe wyciaganie calej krawedzi.
            for edge in self.dag.iteroutedges(self.parent[node]):
                if edge.target == node:
                    if edge.source < edge.target:
                        self.cut_edges.append(edge)
                    else:
                        self.cut_edges.append(~edge)


class TarjanCutEdgeWithEdges:
    """Tarjan's bridge-finding algorithm, O(V+E) time.
    
    Attributes
    ----------
    graph : input undirected graph
    cut_edges : list of nodes
    low : dict with nodes
    parent : dict with edges (DFS tree)
    time : number, private
    dd : dict with nodes (values are numbers, time stamps), private
    
    Notes
    -----
    Based on the description from:
    
    http://eduinf.waw.pl/inf/alg/001_search/0130a.php
    
    https://en.wikipedia.org/wiki/Bridge_(graph_theory)
    
    R. E. Tarjan, A note on finding the bridges of a graph,
        Information Processing Letters 2, 160-161 (1974).
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.cut_edges = []
        # Parametr dla wierzcholka wprowadzony przez Tarjana.
        self.low = dict(((node, None) for node in self.graph.iternodes()))
        self.parent = dict(((node, None) for node in self.graph.iternodes()))
        self.time = 0    # time stamp
        self.dd = dict(((node, 0) for node in self.graph.iternodes()))
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v() * 2, recursionlimit))

    def run(self, source=None):
        """Executable pseudocode."""
        if source is not None:   # scanning a single connected component
            self._visit(source)
        else:
            for node in self.graph.iternodes():
                if self.dd[node] == 0:   # not visited
                    self._visit(node)

    def _visit(self, node):
        """Explore recursively the connected component."""
        self.time += 1
        self.dd[node] = self.time
        self.low[node] = self.time
        for edge in self.graph.iteroutedges(node):
            if (self.parent[node] is not None and
                edge.target == self.parent[node].target):
                continue   # self.parent[node] is None for root
            if self.dd[edge.target] == 0:   # not visited
                self.parent[edge.target] = ~edge
                self._visit(edge.target)
                # Po wyjsciu z rekurencji obliczamy low().
                self.low[node] = min(self.low[node], self.low[edge.target])
            else:   # back edge
                self.low[node] = min(self.low[node], self.dd[edge.target])
        # All neighbors are visited. Check the bridge condition.
        if self.parent[node] is not None and self.low[node] == self.dd[node]:
            # Most to jest krawedz prowadzaca do node od jego rodzica.
            edge = self.parent[node]
            if edge.source < edge.target:
                self.cut_edges.append(edge)
            else:
                self.cut_edges.append(~edge)

# EOF
