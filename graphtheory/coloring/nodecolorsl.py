#!/usr/bin/env python3

try:
    range = xrange
except NameError:   # Python 3
    pass


class SmallestLastNodeColoring:
    """Find a smallest last (SL) node coloring.
    
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
        n = self.graph.v()
        degree_dict = dict((node, self.graph.degree(node))
            for node in self.graph.iternodes())   # O(V) time
        order = list()
        used = set()
        bucket = list(set() for deg in range(n))   # O(V) time
        for node in self.graph.iternodes():   # O(V) time
            bucket[self.graph.degree(node)].add(node)
        for step in range(n):   # O(V) time
            for deg in range(n):
                if bucket[deg]:
                    source = bucket[deg].pop()
                    break
            order.append(source)
            used.add(source)
            for target in self.graph.iteradjacent(source):
                if target in used:
                    continue
                deg = degree_dict[target]
                bucket[deg].remove(target)
                bucket[deg-1].add(target)
                degree_dict[target] = deg-1
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
