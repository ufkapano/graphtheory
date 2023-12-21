#!/usr/bin/env python3

try:
    range = xrange
except NameError:   # Python 3
    pass

import random

class RandomSequentialEdgeColoring:
    """Find a random sequential (RS) edge coloring.
    
    Attributes
    ----------
    graph : input undirected graph or multigraph
    color : dict with edges (values are colors)
    m : number (the number od edges)
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

    def run(self):
        """Executable pseudocode."""
        edge_list = list(self.graph.iteredges())
        random.shuffle(edge_list)   # O(E) time
        for edge in edge_list:
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

# EOF
