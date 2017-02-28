#!/usr/bin/python

from graphtheory.traversing.bfs import SimpleBFS


class ConnectedSequentialNodeColoring:
    """Find a connected sequential (CS) node coloring."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.color = dict((node, None) for node in self.graph.iternodes())
        for edge in self.graph.iteredges():
            if edge.source == edge.target:
                raise ValueError("a loop detected")

    def run(self):
        """Executable pseudocode."""
        order = list()
        algorithm = SimpleBFS(self.graph)
        algorithm.run(pre_action=lambda node: order.append(node))
        for source in order:
            self._greedy_color(source)

    def _greedy_color(self, source):
        """Give node the smallest possible color."""
        n = self.graph.v()   # memory O(V)
        used = [False] * n   # is color used?
        for target in self.graph.iteradjacent(source):
            if self.color[target] is not None:
                used[self.color[target]] = True
        for c in xrange(n):   # check colors
            if not used[c]:
                self.color[source] = c
                break
        return c

# EOF
