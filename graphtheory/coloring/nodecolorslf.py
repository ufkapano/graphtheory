#!/usr/bin/env python3

try:
    range = xrange
except NameError:   # Python 3
    pass


class SLFNodeColoring:
    """Find a saturated largest first (SLF) node coloring.
    Computational complexity is O(V^2).
    
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
        # Saturacja moze sie przydac po zakonczeniu algorytmu.
        self.saturation = dict((node, set()) for node in self.graph.iternodes())

    def run(self):
        """Executable pseudocode."""
        n = self.graph.v()
        for step in range(n):
            source = max((node for node in self.graph.iternodes()
                if self.color[node] is None), key=lambda x:
                n * len(self.saturation[x]) + self.graph.degree(x))
            self._greedy_color_with_saturation(source)

    def _greedy_color_with_saturation(self, source):
        """Give node the smallest possible color."""
        for c in range(self.graph.v()):
            if c not in self.saturation[source]:
                self.color[source] = c
                break
        # Sasiadom podwyzszamy stopien nasycenia dodajac kolory.
        for edge in self.graph.iteroutedges(source):
            self.saturation[edge.target].add(c)
        return c

# EOF
