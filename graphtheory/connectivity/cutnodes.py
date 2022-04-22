#!/usr/bin/env python3

import sys
from graphtheory.traversing.dfs import SimpleDFS
from graphtheory.connectivity.connected import is_connected


class TrivialCutNode:
    """Trivial algorithm for finding cut nodes (articulation points).
    
    The algorithm runs in O(V*(V+E)) time.
    
    Attributes
    ----------
    graph : input undirected graph
    cut_nodes : list of nodes
    
    Notes
    -----
    Based on the description from:
    
    http://eduinf.waw.pl/inf/alg/001_search/0130b.php
    
    https://en.wikipedia.org/wiki/Connectivity_(graph_theory)
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.cut_nodes = list()

    def run(self, source=None):
        """Executable pseudocode."""
        old_ncc = self._find_ncc()
        for source in self.graph.iternodes():
            removed = list(self.graph.iteroutedges(source))
            for edge in removed:
                self.graph.del_edge(edge)
            new_ncc = self._find_ncc()
            for edge in removed:
                self.graph.add_edge(edge)
            if new_ncc > old_ncc + 1:   # source was not removed
                self.cut_nodes.append(source)

    def _find_ncc(self):
        """Return the number of connected components."""
        visited = dict((node, False) for node in self.graph.iternodes())
        ncc = 0
        algorithm = SimpleDFS(self.graph)
        for source in self.graph.iternodes():
            if not visited[source]:
                algorithm.run(source, pre_action=lambda node:
                    visited.__setitem__(node, True))
                ncc += 1
        return ncc


class TarjanCutNode:
    """Tarjan's algorithm for finding cut nodes in O(V+E) time.
    
    Attributes
    ----------
    graph : input undirected graph
    cut_nodes : list of nodes
    low : dict with nodes
    parent : dict with nodes (DFS tree)
    _time : number, private
    _dd : dict with nodes (values are numbers, time stamps), private
    dag : graph (DFS tree)
    
    Notes
    -----
    Based on the description from:
    
    http://eduinf.waw.pl/inf/alg/001_search/0130b.php
    
    https://en.wikipedia.org/wiki/Connectivity_(graph_theory)
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.cut_nodes = list()
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
            self._visit_root(source)
        else:
            for node in self.graph.iternodes():
                if self._dd[node] == 0:   # not visited
                    self._visit_root(node)

    def _visit_root(self, node):
        """Explore recursively the connected component from root."""
        self._time = self._time + 1
        self._dd[node] = self._time
        self.low[node] = self._time
        n_sons = 0   # number of sons for the root
        for edge in self.graph.iteroutedges(node):
            if self._dd[edge.target] == 0:   # not visited
                n_sons += 1
                self.parent[edge.target] = node
                self.dag.add_edge(edge)
                self._visit(edge.target)
        # Is the root an articulation point?
        if n_sons > 1:
            self.cut_nodes.append(node)

    def _visit(self, node):
        """Explore recursively the connected component."""
        self._time += 1
        self._dd[node] = self._time
        self.low[node] = self._time   # temporary
        is_cut_node = False
        for edge in self.graph.iteroutedges(node):
            if edge.target == self.parent[node]:   # can be None!
                continue
            if self._dd[edge.target] == 0:   # not visited
                self.parent[edge.target] = node
                self.dag.add_edge(edge)
                self._visit(edge.target)
                self.low[node] = min(self.low[node], self.low[edge.target])
                # Test for an articulation point.
                if self.low[edge.target] >= self._dd[node]:
                    is_cut_node = True
            else:   # back edge
                self.low[node] = min(self.low[node], self._dd[edge.target])
        # All neighbors are visited. Check the test.
        if is_cut_node:
            self.cut_nodes.append(node)


def is_biconnected(graph):
    """Test if the undirected graph is biconnected."""
    if graph.is_directed():
        raise ValueError("the graph is directed")
    if not is_connected(graph):
        return False
    algorithm = TarjanCutNode(graph)
    algorithm.run()
    return len(algorithm.cut_nodes) == 0

# EOF
