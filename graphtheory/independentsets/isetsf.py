#!/usr/bin/python

# Wersja malo wydajna.
# Tutaj _used i independent_set jest typu set.
class SmallestFirstIndependentSet1:
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
        self._used = set()
        self.source = None

    def run(self, source=None):
        """Executable pseudocode."""
        if source is not None:
            self.source = source
            self.independent_set.add(source)
            self._used.add(source)
            self._used.update(self.graph.iteradjacent(source))
        for source in sorted(self.graph.iternodes(), key=self.graph.degree):
            if source in self._used:
                continue
            self.independent_set.add(source)
            self._used.add(source)
            self._used.update(self.graph.iteradjacent(source))
        self.cardinality = len(self.independent_set)


# Tutaj _used to dict.
class SmallestFirstIndependentSet2:
    """Find a maximal independent set."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        for edge in self.graph.iteredges():
            if edge.source == edge.target:
                raise ValueError("a loop detected")
        self.independent_set = set()
        self.cardinality = 0
        self._used = dict((node, False) for node in self.graph.iternodes())
        self.source = None

    def run(self, source=None):
        """Executable pseudocode."""
        if source is not None:
            self.source = source
            self.independent_set.add(source)
            self._used[source] = True
            for target in self.graph.iteradjacent(source):
                self._used[target] = True
        for source in sorted(self.graph.iternodes(), key=self.graph.degree):
            if self._used[source]:
                continue
            self.independent_set.add(source)
            self._used[source] = True
            for target in self.graph.iteradjacent(source):
                self._used[target] = True
        self.cardinality = len(self.independent_set)


# Tutaj nie uzywam zbiorow, tylko dict. Dobre dla C++.
class SmallestFirstIndependentSet3:
    """Find a maximal independent set."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        for edge in self.graph.iteredges():
            if edge.source == edge.target:
                raise ValueError("a loop detected")
        self.independent_set = dict((node, False) for node in self.graph.iternodes())
        self.cardinality = 0
        self._used = dict((node, False) for node in self.graph.iternodes())
        self.source = None

    def run(self, source=None):
        """Executable pseudocode."""
        if source is not None:
            self.source = source
            self.independent_set[source] = True
            self._used[source] = True
            self.cardinality += 1
            for target in self.graph.iteradjacent(source):
                self._used[target] = True
        for source in sorted(self.graph.iternodes(), key=self.graph.degree):
            if self._used[source]:
                continue
            self.independent_set[source] = True
            self._used[source] = True
            self.cardinality += 1
            for target in self.graph.iteradjacent(source):
                self._used[target] = True

######################################################################
# Szukamy wierzcholka o najmniejszym stopniu w malejacym grafie indukowanym.

# Korzystamy ze zbiorow.
class SmallestFirstIndependentSet4:
    """Find a maximal independent set."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        for edge in self.graph.iteredges():
            if edge.source == edge.target:
                raise ValueError("a loop detected")
        self.independent_set = set()
        self.cardinality = 0
        # Bede szukal min() z wierzcholkow nalezacych do zbioru free.
        self.free = set(self.graph.iternodes())
        self.source = None

    def run(self, source=None):
        """Executable pseudocode."""
        degree_dict = dict((node, self.graph.degree(node))
            for node in self.graph.iternodes())   # O(V) time
        if source is not None:
            self.source = source
            self.independent_set.add(source)
            self.free.remove(source)
            for target in self.graph.iteradjacent(source):
                self.free.discard(target)
                # Wpisy dla source i target nie trzeba uaktualniac.
                for node in self.graph.iteradjacent(target):
                    degree_dict[node] -= 1
        while len(self.free) > 0:
            source = min(self.free, key=degree_dict.__getitem__)
            self.independent_set.add(source)
            self.free.remove(source)
            for target in self.graph.iteradjacent(source):
                self.free.discard(target)
                # Wpisy dla source i target nie trzeba uaktualniac,
                # bo te wierzcholki usuwamy z self.free.
                # node moze prowadzic do self.free, wiec trzeba uaktualnic.
                for node in self.graph.iteradjacent(target):
                    degree_dict[node] -= 1
        self.cardinality = len(self.independent_set)


# iset to set, used to dict.
class SmallestFirstIndependentSet5:
    """Find a maximal independent set."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        for edge in self.graph.iteredges():
            if edge.source == edge.target:
                raise ValueError("a loop detected")
        self.independent_set = set()
        self.cardinality = 0
        self._used = dict((node, False) for node in self.graph.iternodes())
        self.source = None

    def run(self, source=None):
        """Executable pseudocode."""
        degree_dict = dict((node, self.graph.degree(node))
            for node in self.graph.iternodes())   # O(V) time
        if source is not None:
            self.source = source
            self.independent_set.add(source)
            self._used[source] = True
            for target in self.graph.iteradjacent(source):
                self._used[target] = True
                # Wpisy dla source i target nie trzeba uaktualniac.
                for node in self.graph.iteradjacent(target):
                    degree_dict[node] -= 1
        while not all(self._used[node] for node in self.graph.iternodes()):
            source = min((node for node in self.graph.iternodes()
                if not self._used[node]), key=degree_dict.__getitem__)
            self.independent_set.add(source)
            self._used[source] = True
            for target in self.graph.iteradjacent(source):
                self._used[target] = True
                # Wpisy dla source i target nie trzeba uaktualniac.
                for node in self.graph.iteradjacent(target):
                    degree_dict[node] -= 1
        self.cardinality = len(self.independent_set)


# Tutaj nie uzywam zbiorow.
class SmallestFirstIndependentSet6:
    """Find a maximal independent set."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        for edge in self.graph.iteredges():
            if edge.source == edge.target:
                raise ValueError("a loop detected")
        self.independent_set = dict((node, False) for node in self.graph.iternodes())
        self.cardinality = 0
        self._used = dict((node, False) for node in self.graph.iternodes())
        self.source = None

    def run(self, source=None):
        """Executable pseudocode."""
        degree_dict = dict((node, self.graph.degree(node))
            for node in self.graph.iternodes())   # O(V) time
        if source is not None:
            self.source = source
            self.independent_set[source] = True
            self._used[source] = True
            self.cardinality += 1
            for target in self.graph.iteradjacent(source):
                self._used[target] = True
                # Wpisy dla source i target nie trzeba uaktualniac.
                for node in self.graph.iteradjacent(target):
                    degree_dict[node] -= 1
        while not all(self._used[node] for node in self.graph.iternodes()):
            source = min((node for node in self.graph.iternodes()
                if not self._used[node]), key=degree_dict.__getitem__)
            self.independent_set[source] = True
            self._used[source] = True
            self.cardinality += 1
            for target in self.graph.iteradjacent(source):
                self._used[target] = True
                # Wpisy dla source i target nie trzeba uaktualniac.
                for node in self.graph.iteradjacent(target):
                    degree_dict[node] -= 1


SmallestFirstIndependentSet = SmallestFirstIndependentSet1

# EOF
