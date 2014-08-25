#!/usr/bin/python
#
# acyclic.py
#
# Cycles detection.

from edges import Edge
from graphs import Graph

class AcyclicGraphDFS:
    """Cycles detection in graphs based on DFS."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.color = dict(((node, "WHITE") for node in self.graph.iternodes()))
        self.prev = dict(((node, None) for node in self.graph.iternodes()))
        # ciekawe ustawianie rekurencji
        import sys
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v()*2, recursionlimit))

    def run(self, source=None):
        """Executable pseudocode."""
        if source is not None:
            # only one connected component will be checked!
            self.visit(source)
        else:
            for node in self.graph.iternodes():
                if self.color[node] == "WHITE":
                    self.visit(node)

    def visit(self, node):
        """Explore recursively the connected component."""
        self.color[node] = "GREY"
        for target in self.graph.iteradjacent(node):
            if self.color[target] == "WHITE":
                self.prev[target] = node
                self.visit(target)
            elif self.color[target] == "GREY":   # back edge
                if self.graph.is_directed() or target != self.prev[node]:
                    raise ValueError("a cycle detected")
            else:   # directed graph, cross or forward edge
                pass
        self.color[node] = "BLACK"

# EOF
