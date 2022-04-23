#!/usr/bin/env python3

class DegreeNodeCover:
    """Find a minimum node cover (greedy algorithm) in O(V+E) time."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.node_cover = set()
        self.cardinality = 0

    def run(self):
        """Executable pseudocode."""
        for edge in self.graph.iteredges():
            if (edge.source not in self.node_cover and
                edge.target not in self.node_cover):
                if self.graph.degree(edge.source) > self.graph.degree(edge.target):
                    self.node_cover.add(edge.source)
                else:
                    self.node_cover.add(edge.target)
        self.cardinality = len(self.node_cover)

# EOF
