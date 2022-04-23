#!/usr/bin/env python3

# Tutaj _used i independent_set jest typu set.
class UnorderedSequentialIndependentSet1:
    """Find a maximal independent set."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        for edge in self.graph.iteredges():
            if edge.source == edge.target:   # for multigraphs
                raise ValueError("a loop detected")
        self.independent_set = set()
        self.cardinality = 0
        self.source = None

    def run(self, source=None):
        """Executable pseudocode."""
        used = set()
        if source is not None:
            self.source = source
            self.independent_set.add(source)
            used.add(source)
            used.update(self.graph.iteradjacent(source))
        for source in self.graph.iternodes():
            if source in used:
                continue
            self.independent_set.add(source)
            used.add(source)
            used.update(self.graph.iteradjacent(source))
        self.cardinality = len(self.independent_set)


# Tutaj _used jest dict, a independent_set jest typu set.
class UnorderedSequentialIndependentSet2:
    """Find a maximal independent set."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        for edge in self.graph.iteredges():
            if edge.source == edge.target:   # for multigraphs
                raise ValueError("a loop detected")
        self.independent_set = set()
        self.cardinality = 0
        self.source = None

    def run(self, source=None):
        """Executable pseudocode."""
        used = dict((node, False) for node in self.graph.iternodes())
        if source is not None:
            self.source = source
            self.independent_set.add(source)
            used[source] = True
            for target in self.graph.iteradjacent(source):
                used[target] = True
        for source in self.graph.iternodes():
            if used[source]:
                continue
            self.independent_set.add(source)
            used[source] = True
            for target in self.graph.iteradjacent(source):
                used[target] = True
        self.cardinality = len(self.independent_set)


# Tutaj _used i independent_set jest dict. Wygodne dla C++.
class UnorderedSequentialIndependentSet3:
    """Find a maximal independent set."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        for edge in self.graph.iteredges():
            if edge.source == edge.target:   # for multigraphs
                raise ValueError("a loop detected")
        self.independent_set = dict((node, False) for node in self.graph.iternodes())
        self.cardinality = 0
        self.source = None

    def run(self, source=None):
        """Executable pseudocode."""
        used = dict((node, False) for node in self.graph.iternodes())
        if source is not None:
            self.source = source
            self.independent_set[source] = True
            used[source] = True
            self.cardinality += 1
            for target in self.graph.iteradjacent(source):
                used[target] = True
        for source in self.graph.iternodes():
            if used[source]:
                continue
            self.independent_set[source] = True
            used[source] = True
            self.cardinality += 1
            for target in self.graph.iteradjacent(source):
                used[target] = True


UnorderedSequentialIndependentSet = UnorderedSequentialIndependentSet1

# EOF
