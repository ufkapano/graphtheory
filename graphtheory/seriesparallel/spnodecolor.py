#!/usr/bin/python

try:
    integer_types = (int, long)
    range = xrange
except NameError:   # Python 3
    integer_types = (int,)

from graphtheory.bipartiteness.bipartite import BipartiteGraphBFS
from graphtheory.connectivity.connected import is_connected
from graphtheory.seriesparallel.sptools import find_peo_spgraph


class SPNodeColoring:
    """Find sp-graph node coloring."""
    # Kolory sa kolejnymi liczbami 0, 1, 2, ...

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        if not is_connected(graph):
            raise ValueError("the graph is not connected")
        self.graph = graph
        self.color = dict((node, None) for node in self.graph.iternodes())
        self._color_list = [False] * self.graph.v()

    def run(self):
        """Executable pseudocode."""
        try:
            algorithm = BipartiteGraphBFS(self.graph)
            algorithm.run()
            self.color = algorithm.color
        except ValueError:
            order = find_peo_spgraph(self.graph)
            for source in reversed(order):
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
