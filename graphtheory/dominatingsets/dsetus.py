#!/usr/bin/env python3

class UnorderedSequentialDominatingSet:
    """Find a (unordered sequential) dominating set in O(V+E) time."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.dominating_set = set()
        self.cardinality = 0
        self.source = None

    def run(self, source=None):
        """Executable pseudocode."""
        used = set()
        if source is not None:
            self.source = source
            self.dominating_set.add(source)
            used.add(source)
            used.update(self.graph.iteradjacent(source))
        for node in self.graph.iternodes():
            if node in used:
                continue
            self.dominating_set.add(node)
            used.add(node)
            used.update(self.graph.iteradjacent(node))
        self.cardinality = len(self.dominating_set)

# EOF
