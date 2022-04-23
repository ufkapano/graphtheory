#!/usr/bin/env python3

class ApproximationNodeCover:
    """Find a minimum node cover (2-approximation) in O(V+E) time.
    
    Based on ideas from Cormen.
    len(node_cover) <= 2 * len(minimum_node_cover)
    """

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
                self.node_cover.add(edge.source)
                self.node_cover.add(edge.target)
        self.cardinality = len(self.node_cover)

# EOF
