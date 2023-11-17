#!/usr/bin/env python3

try:
    range = xrange   # range będzie zawsze generatorem
except NameError:   # Py3
    pass

import collections


class ConnectedSequentialEdgeColoring1:
    """Find a connected sequential (CS) edge coloring.
    
    Attributes
    ----------
    graph : input undirected graph or multigraph
    color : dict with edges (values are colors)
    parent : dict (BFS tree)
    m : number (the number of edges)
    saturation : dict with nodes (values are sets of adjacent node colors)
    
    Notes
    -----
    Colors are 0, 1, 2, ...
    edge.source < edge.target for any edge in color.
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.parent = dict()
        self.color = dict()
        self.m = 0   # graph.e() is slow
        for edge in self.graph.iteredges():
            if edge.source == edge.target:
                raise ValueError("a loop detected")
            else:
                self.color[edge] = None   # edge.source < edge.target
                self.m += 1
        if len(self.color) < self.m:
            raise ValueError("edges are not unique")
        self.saturation = dict((node, set()) for node in self.graph.iternodes())

    def run(self, source=None):
        """Using BFS to color edges.."""
        if source is not None:   # only one connected component
            self._visit(source)
        else:
            for node in self.graph.iternodes():
                if node not in self.parent:
                    self._visit(node)

    def _visit(self, node):
        """Explore the connected component."""
        Q = collections.deque()
        self.parent[node] = None   # before Q.append
        Q.append(node)
        while len(Q) > 0:
            source = Q.popleft()
            for edge in self.graph.iteroutedges(source):
                if edge.target not in self.parent:
                    self.parent[edge.target] = source   # before Q.append
                    Q.append(edge.target)
                if edge.source > edge.target:
                    edge = ~edge
                if self.color[edge] is None:
                    self._greedy_color_with_saturation(edge)

    def _greedy_color_with_saturation(self, edge):
        """Give edge the smallest possible color."""
        for c in range(self.m):
            if (c in self.saturation[edge.source] or 
                c in self.saturation[edge.target]):
                continue   # color is used
            else:   # color is free
                self.color[edge] = c
                self.saturation[edge.source].add(c)
                self.saturation[edge.target].add(c)
                break
        return c

    def _get_color(self, edge):
        """Get color."""
        if edge.source > edge.target:
            edge = ~edge
        return self.color[edge]

    def show_colors(self):
        """Show edge coloring (undirected graphs)."""
        L = []
        for source in self.graph.iternodes():
            L.append("{} : ".format(source))
            for edge in self.graph.iteroutedges(source):
                # It should work for multigraphs.
                c = self._get_color(edge)
                L.append("{}({}) ".format(edge.target, c))
            L.append("\n")
        print("".join(L))


class ConnectedSequentialEdgeColoring2:
    """Find a connected sequential (CS) edge coloring.
    
    Attributes
    ----------
    graph : input undirected graph or multigraph
    color : dict with edges (values are colors)
    m : number (the number of edges)
    saturation : dict with nodes (values are sets of adjacent node colors)
    
    Notes
    -----
    Colors are 0, 1, 2, ...
    edge.source < edge.target for any edge in color.
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.color = dict()
        self.m = 0   # graph.e() is slow
        for edge in self.graph.iteredges():
            if edge.source == edge.target:
                raise ValueError("a loop detected")
            else:
                self.color[edge] = None   # edge.source < edge.target
                self.m += 1
        if len(self.color) < self.m:
            raise ValueError("edges are not unique")
        self.saturation = dict((node, set()) for node in self.graph.iternodes())

    def run(self, source=None):
        """Using BFS to color edges."""
        if source is not None:   # only one connected component
            start_edge = next(self.graph.iteroutedges(source))
        else:
            start_edge = next(self.graph.iteredges())
        for edge in self.graph.iteredges_connected(start_edge):
            self._greedy_color_with_saturation(edge)

    def _greedy_color_with_saturation(self, edge):
        """Give edge the smallest possible color."""
        for c in range(self.m):
            if (c in self.saturation[edge.source] or 
                c in self.saturation[edge.target]):
                continue   # color is used
            else:   # color is free
                self.color[edge] = c
                self.saturation[edge.source].add(c)
                self.saturation[edge.target].add(c)
                break
        return c

    def _get_color(self, edge):
        """Get color."""
        if edge.source > edge.target:
            edge = ~edge
        return self.color[edge]

    def show_colors(self):
        """Show edge coloring (undirected graphs)."""
        L = []
        for source in self.graph.iternodes():
            L.append("{} : ".format(source))
            for edge in self.graph.iteroutedges(source):
                # It should work for multigraphs.
                c = self._get_color(edge)
                L.append("{}({}) ".format(edge.target, c))
            L.append("\n")
        print("".join(L))


ConnectedSequentialEdgeColoring = ConnectedSequentialEdgeColoring2

# EOF
