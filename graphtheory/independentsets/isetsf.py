#!/usr/bin/env python3

try:
    integer_types = (int, long)
    range = xrange
except NameError:   # Python 3
    integer_types = (int,)

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
        self.source = None

    def run(self, source=None):
        """Executable pseudocode."""
        used = set()
        if source is not None:
            self.source = source
            self.independent_set.add(source)
            used.add(source)
            used.update(self.graph.iteradjacent(source))
        for source in sorted(self.graph.iternodes(), key=self.graph.degree):
            if source in used:
                continue
            self.independent_set.add(source)
            used.add(source)
            used.update(self.graph.iteradjacent(source))
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
        for source in sorted(self.graph.iternodes(), key=self.graph.degree):
            if used[source]:
                continue
            self.independent_set.add(source)
            used[source] = True
            for target in self.graph.iteradjacent(source):
                used[target] = True
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
        for source in sorted(self.graph.iternodes(), key=self.graph.degree):
            if used[source]:
                continue
            self.independent_set[source] = True
            used[source] = True
            self.cardinality += 1
            for target in self.graph.iteradjacent(source):
                used[target] = True

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
        self.source = None

    def run(self, source=None):
        """Executable pseudocode."""
        used = dict((node, False) for node in self.graph.iternodes())
        degree_dict = dict((node, self.graph.degree(node))
            for node in self.graph.iternodes())   # O(V) time
        if source is not None:
            self.source = source
            self.independent_set.add(source)
            used[source] = True
            for target in self.graph.iteradjacent(source):
                used[target] = True
                # Wpisy dla source i target nie trzeba uaktualniac.
                for node in self.graph.iteradjacent(target):
                    degree_dict[node] -= 1
        while not all(used[node] for node in self.graph.iternodes()):
            source = min((node for node in self.graph.iternodes()
                if not used[node]), key=degree_dict.__getitem__)
            self.independent_set.add(source)
            used[source] = True
            for target in self.graph.iteradjacent(source):
                used[target] = True
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
        self.source = None

    def run(self, source=None):
        """Executable pseudocode."""
        used = dict((node, False) for node in self.graph.iternodes())
        degree_dict = dict((node, self.graph.degree(node))
            for node in self.graph.iternodes())   # O(V) time
        if source is not None:
            self.source = source
            self.independent_set[source] = True
            used[source] = True
            self.cardinality += 1
            for target in self.graph.iteradjacent(source):
                used[target] = True
                # Wpisy dla source i target nie trzeba uaktualniac.
                for node in self.graph.iteradjacent(target):
                    degree_dict[node] -= 1
        while not all(used[node] for node in self.graph.iternodes()):
            source = min((node for node in self.graph.iternodes()
                if not used[node]), key=degree_dict.__getitem__)
            self.independent_set[source] = True
            used[source] = True
            self.cardinality += 1
            for target in self.graph.iteradjacent(source):
                used[target] = True
                # Wpisy dla source i target nie trzeba uaktualniac.
                for node in self.graph.iteradjacent(target):
                    degree_dict[node] -= 1

######################################################################
# Zastosowanie sortowania bukietowego.

class SmallestFirstIndependentSet7:
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
        self.source = None

    def run(self, source=None):
        """Executable pseudocode."""
        used = set()
        degree_dict = dict((node, self.graph.degree(node))
            for node in self.graph.iternodes())   # O(V) time
        # Grupujemy wierzcholki w bukietach wg stopni.
        bucket = list(set() for deg in range(self.graph.v()))   # O(V) time
        for node in self.graph.iternodes():   # O(V) time
            bucket[self.graph.degree(node)].add(node)

        # Liczba krokow do wykonania rowna sie liczbie wierzcholkow.
        steps = self.graph.v()
        if source is not None:
            self.source = source
            self.independent_set.add(source)
            used.add(source)
            steps -= 1   # bo usuniety source
            # Uaktualnienie degree_dict i bucket.
            deg = degree_dict[source] # tutaj deg moze byc dowolne
            bucket[deg].remove(source)
            # Usuwanie sasiadow source.
            for target in self.graph.iteradjacent(source):
                if target in used:   # nie bedzie takich
                    continue
                used.add(target)
                steps -= 1   # bo usuniety target
                # Uaktualnienie degree_dict i bucket.
                deg = degree_dict[target]
                bucket[deg].remove(target)
                degree_dict[target] = deg-1   # bo usuniety source
                degree_dict[source] -= 1
                # Uaktualnienie degree_dict i bucket.
                for node in self.graph.iteradjacent(target):
                    if node in used:   # node usuniety z bucket
                        continue
                    deg = degree_dict[node]
                    bucket[deg].remove(node)
                    bucket[deg-1].add(node)
                    degree_dict[node] = deg-1
                    degree_dict[target] -= 1
                assert degree_dict[target] == 0
            assert degree_dict[source] == 0

        while steps > 0:
            # Wybor wierzcholka o najmniejszym stopniu.
            for deg in range(self.graph.v()):
                if bucket[deg]:
                    source = bucket[deg].pop()
                    break
            self.independent_set.add(source)
            used.add(source)
            steps -= 1   # bo usuniety source
            # Usuwanie sasiadow source.
            for target in self.graph.iteradjacent(source):
                if target in used:   # target usuniety z bucket
                    continue
                used.add(target)
                steps -= 1   # bo usuniety target
                # Uaktualnienie degree_dict i bucket.
                deg = degree_dict[target]
                bucket[deg].remove(target)
                degree_dict[target] = deg-1   # bo usuniety source
                degree_dict[source] -= 1
                # Uaktualnienie degree_dict i bucket.
                for node in self.graph.iteradjacent(target):
                    if node in used:   # node usuniety z bucket
                        continue
                    deg = degree_dict[node]
                    bucket[deg].remove(node)
                    bucket[deg-1].add(node)
                    degree_dict[node] = deg-1
                    degree_dict[target] -= 1
                assert degree_dict[target] == 0
            assert degree_dict[source] == 0
        self.cardinality = len(self.independent_set)
        assert steps == 0


SmallestFirstIndependentSet = SmallestFirstIndependentSet7

# EOF
