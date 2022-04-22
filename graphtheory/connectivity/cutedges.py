#!/usr/bin/env python3

import sys
from graphtheory.traversing.dfs import SimpleDFS


class TrivialCutEdge:
    """Trivial bridge-finding algorithm.
    
    The algorithm runs in O(E*(V+E)) time.
    
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
        self.cut_edges = list()

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
    """Tarjan's bridge-finding algorithm in O(V+E) time.
    
    Attributes
    ----------
    graph : input undirected graph
    cut_edges : list of nodes
    low : dict with nodes
    parent : dict with nodes (DFS tree)
    _time : number, private
    _dd : dict with nodes (values are numbers, time stamps), private
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
        self.cut_edges = list()
        # Parametr dla wierzcholka wprowadzony przez Tarjana.
        self.low = dict(((node, None) for node in self.graph.iternodes()))
        self.parent = dict(((node, None) for node in self.graph.iternodes()))
        self._time = 0    # time stamp
        self._dd = dict(((node, 0) for node in self.graph.iternodes()))
        self.dag = self.graph.__class__(self.graph.v(), directed=True)
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v() * 2, recursionlimit))

    def run(self, source=None):
        """Executable pseudocode."""
        if source is not None:
            self._visit(source)
        else:
            for node in self.graph.iternodes():
                if self._dd[node] == 0:   # not visited
                    self._visit(node)

    def _visit(self, node):
        """Explore recursively the connected component."""
        self._time += 1
        self._dd[node] = self._time
        self.low[node] = self._time
        for edge in self.graph.iteroutedges(node):
            if edge.target == self.parent[node]:   # can be None!
                continue
            if self._dd[edge.target] == 0:   # not visited
                self.parent[edge.target] = node
                self.dag.add_edge(edge)
                self._visit(edge.target)
                self.low[node] = min(self.low[node], self.low[edge.target])
            else:   # back edge
                self.low[node] = min(self.low[node], self._dd[edge.target])
        # All neighbors are visited. Check the bridge condition.
        if self.parent[node] is not None and self.low[node] == self._dd[node]:
            # Most to jest krawedz prowadzaca do node od jego rodzica.
            # Tu jest klopotliwe wyciaganie calej krawedzi.
            for edge in self.dag.iteroutedges(self.parent[node]):
                if edge.target == node:
                    self.cut_edges.append(edge)

# EOF
