#!/usr/bin/python

from graphs import Graph


class AcyclicGraphDFS:
    """Cycles detection in graphs based on DFS."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.color = dict(((node, "WHITE") for node in self.graph.iternodes()))
        self.parent = dict(((node, None) for node in self.graph.iternodes()))
        import sys
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v() * 2, recursionlimit))

    def run(self, source=None):
        """Executable pseudocode."""
        if source is not None:
            # Only one connected component will be checked!
            self._visit(source)
        else:
            for node in self.graph.iternodes():
                if self.color[node] == "WHITE":
                    self._visit(node)

    def _visit(self, node):
        """Explore recursively the connected component."""
        self.color[node] = "GREY"
        for edge in self.graph.iteroutedges(node):
            if self.color[edge.target] == "WHITE":
                self.parent[edge.target] = node
                self._visit(edge.target)
            elif self.color[edge.target] == "GREY":   # back edge possible
                if self.graph.is_directed() or edge.target != self.parent[node]:
                    raise ValueError("a cycle detected")
            else:   # directed graph, cross or forward edge
                pass
        self.color[node] = "BLACK"

# EOF
