#!/usr/bin/python

class UnorderedSequentialEdgeColoring:
    """Find an unordered sequential (US) edge coloring."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.color = dict()   # {edge: int}
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
        for edge in self.graph.iteredges():
            self._greedy_color_with_saturation(edge)

    def _greedy_color_with_saturation(self, edge):
        """Give edge the smallest possible color."""
        for c in xrange(self.m):
            if (c in self.saturation[edge.source] or 
                c in self.saturation[edge.target]):
                continue   # color is used
            else:   # color is free
                self.color[edge] = c
                self.saturation[edge.source].add(c)
                self.saturation[edge.target].add(c)
                break
        return c

# EOF
