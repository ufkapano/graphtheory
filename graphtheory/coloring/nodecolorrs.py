#!/usr/bin/env python3

try:
    range = xrange
except NameError:   # Python 3
    pass

import random


class RandomSequentialNodeColoring:
    """Find a random sequential (RS) node coloring.
    
    Based on
    http://eduinf.waw.pl/inf/alg/001_search/0142.php
    
    Attributes
    ----------
    graph : input undirected graph or multigraph
    color : dict with nodes (values are colors)
    
    Notes
    -----
    Colors are 0, 1, 2, ...
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.color = dict((node, None) for node in self.graph.iternodes())
        for edge in self.graph.iteredges():
            if edge.source == edge.target:
                raise ValueError("a loop detected")
        self._color_list = [False] * self.graph.v()

    def run(self):
        """Executable pseudocode."""
        node_list = list(self.graph.iternodes())
        random.shuffle(node_list)   # O(V) time
        for source in node_list:
            self._greedy_color(source)

    def _greedy_color(self, source):
        """Give node the smallest possible color."""
        for target in self.graph.iteradjacent(source):
            if self.color[target] is not None:
                self._color_list[self.color[target]] = True
        for c in range(self.graph.v()):   # check colors
            if not self._color_list[c]:
                self.color[source] = c
                break
        for target in self.graph.iteradjacent(source):
            if self.color[target] is not None:
                self._color_list[self.color[target]] = False
        return c

# EOF
