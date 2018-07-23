#!/usr/bin/python
#
# Algorytmy heurystyczne z usuwaniem wierzcholkow.
# Zamiast degree_dict mozna usuwac wierzcholki z kopii grafu.

# Lista wierzcholkow wg stopni ustalona na poczatku.
class LargestLastIndependentSet1:
    """Find a maximal independent set."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        for edge in self.graph.iteredges():
            if edge.source == edge.target:
                raise ValueError("a loop detected")
        self.independent_set = set(self.graph.iternodes())
        self.cardinality = self.graph.v()
        self.source = None

    def run(self, source=None):
        """Executable pseudocode."""
        if source is not None:
            self.source = source
        for source in sorted(self.graph.iternodes(),
            key=self.graph.degree, reverse=True):
                if source == self.source:   # tego nie wyrzucam
                    continue
                if self._is_independent():
                    break
                else:
                    # Usuwam tylko jak ma sasiadow w iset.
                    for target in self.graph.iteradjacent(source):
                        if target in self.independent_set:
                            self.independent_set.discard(source)
        self.cardinality = len(self.independent_set)

    def _is_independent(self):
        """Independence test."""
        for edge in self.graph.iteredges():   # O(E) time
            if (edge.source in self.independent_set and
                edge.target in self.independent_set):
                    return False
        return True


# iset to dict.
class LargestLastIndependentSet2:
    """Find a maximal independent set."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        for edge in self.graph.iteredges():
            if edge.source == edge.target:
                raise ValueError("a loop detected")
        self.independent_set = dict((node, True) for node in self.graph.iternodes())
        self.cardinality = self.graph.v()
        self.source = None

    def run(self, source=None):
        """Executable pseudocode."""
        if source is not None:
            self.source = source
        for source in sorted(self.graph.iternodes(),
            key=self.graph.degree, reverse=True):
                if source == self.source:   # tego nie wyrzucam
                    continue
                if self._is_independent():
                    break
                else:
                    # Usuwam source tylko jak ma sasiadow w iset.
                    for target in self.graph.iteradjacent(source):
                        if self.independent_set[target]:
                            self.independent_set[source] = False
                            self.cardinality -= 1
                            break

    def _is_independent(self):
        """Independence test."""
        for edge in self.graph.iteredges():   # O(E) time
            if (self.independent_set[edge.source] and 
                self.independent_set[edge.target]):
                    return False
        return True

######################################################################
# Stopnie wierzcholkow sa obliczane w malejacym grafie indukowanym.

class LargestLastIndependentSet3:
    """Find a maximal independent set."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        for edge in self.graph.iteredges():
            if edge.source == edge.target:
                raise ValueError("a loop detected")
        self.independent_set = set(self.graph.iternodes())
        self.cardinality = self.graph.v()
        self.source = None

    def run(self, source=None):
        """Executable pseudocode."""
        if source is not None:
            self.source = source
        degree_dict = dict((node, self.graph.degree(node))
            for node in self.graph.iternodes())   # O(V) time
        # Docelowo wszyscy w iset maja stopnie zerowe!
        # To moze byc latwy test zakonczenia petli O(V).
        while not self._is_independent():
            source = max((node for node in self.independent_set
                if node != self.source),
                key=degree_dict.__getitem__)
            self.independent_set.remove(source)
            # Uaktualniamy stopnie sasiadow po usunieciu source.
            for target in self.graph.iteradjacent(source):
                degree_dict[target] -= 1
        self.cardinality = len(self.independent_set)

    def _is_independent(self):
        """Independence test."""
        for edge in self.graph.iteredges():   # O(E) time
            if (edge.source in self.independent_set and
                edge.target in self.independent_set):
                    return False
        return True


# iset to dict.
class LargestLastIndependentSet4:
    """Find a maximal independent set."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        for edge in self.graph.iteredges():
            if edge.source == edge.target:
                raise ValueError("a loop detected")
        self.independent_set = dict((node, True) for node in self.graph.iternodes())
        self.cardinality = self.graph.v()
        self.source = None

    def run(self, source=None):
        """Executable pseudocode."""
        if source is not None:
            self.source = source
        degree_dict = dict((node, self.graph.degree(node))
            for node in self.graph.iternodes())   # O(V) time
        # Docelowo wszyscy w iset maja stopnie zerowe!
        # To moze byc latwy test zakonczenia petli O(V).
        while not self._is_independent():
            # Szukam wsrod wierzcholkow ze zbioru niezaleznego.
            source = max((node for node in self.graph.iternodes()
                if self.independent_set[node] and node != self.source),
                key=degree_dict.__getitem__)
            self.independent_set[source] = False
            self.cardinality -= 1
            # Uaktualniamy stopnie sasiadow po usunieciu source.
            for target in self.graph.iteradjacent(source):
                degree_dict[target] -= 1

    def _is_independent(self):
        """Independence test."""
        for edge in self.graph.iteredges():   # O(E) time
            if (self.independent_set[edge.source] and 
                self.independent_set[edge.target]):
                    return False
        return True


# Korzystamy z kopii grafu.
class LargestLastIndependentSet5:
    """Find a maximal independent set."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        for edge in self.graph.iteredges():
            if edge.source == edge.target:
                raise ValueError("a loop detected")
        self.independent_set = set(self.graph.iternodes())
        self.cardinality = self.graph.v()
        self.source = None

    def run(self, source=None):
        """Executable pseudocode."""
        if source is not None:
            self.source = source   # tego nie usuwamy
        graph_copy = self.graph.copy()
        while not self._is_independent():
            source = max((node for node in self.independent_set
                if node != self.source),
                key=graph_copy.degree)
            self.independent_set.remove(source)
            graph_copy.del_node(source)
        self.cardinality = len(self.independent_set)

    def _is_independent(self):
        """Independence test."""
        for edge in self.graph.iteredges():   # O(E) time
            if (edge.source in self.independent_set and
                edge.target in self.independent_set):
                    return False
        return True


# W kopii grafu usuwam wierzcholki o najwiekszym stopniu
# az nie bedzie krawedzi. Wtedy wszystkie wierzcholki naleza do iset.
# Jest 2 do 4 razy szybciej niz wersja 5.
# Nie dziala dla grafow z macierza sasiedztwa.
class LargestLastIndependentSet6:
    """Find a maximal independent set."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        for edge in self.graph.iteredges():
            if edge.source == edge.target:
                raise ValueError("a loop detected")
        self.independent_set = None
        self.cardinality = 0
        self.source = None

    def run(self, source=None):
        """Executable pseudocode."""
        if source is not None:
            self.source = source   # tego nie usuwamy
        graph_copy = self.graph.copy()
        while graph_copy.e() > 0:
            source = max((node for node in graph_copy.iternodes()
                if node != self.source),
                key=graph_copy.degree)
            graph_copy.del_node(source)   # remove with edges
        self.independent_set = set(graph_copy.iternodes())
        self.cardinality = graph_copy.v()


LargestLastIndependentSet = LargestLastIndependentSet3

# EOF
