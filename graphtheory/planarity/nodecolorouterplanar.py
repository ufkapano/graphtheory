#!/usr/bin/env python3

from graphtheory.bipartiteness.bipartite import BipartiteGraphBFS
from graphtheory.coloring.nodecolorsl import SmallestLastNodeColoring


class OuterplanarNodeColoring:
    """Find an optimal node coloring for outerplanar graphs in linear time."""
    # Kolory sa kolejnymi liczbami 0, 1, 2, ...

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.color = dict((node, None) for node in self.graph.iternodes())

    def run(self):
        """Executable pseudocode."""
        try:   # try 2 colors
            algorithm = BipartiteGraphBFS(self.graph)
            algorithm.run()
            self.color = algorithm.color
        except ValueError:   # 3 colors are needed
            algorithm = SmallestLastNodeColoring(self.graph)
            algorithm.run()
            self.color = algorithm.color

# EOF
