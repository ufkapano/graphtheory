#!/usr/bin/env python3

from graphtheory.structures.powersets import iter_power_set


class ChordalDominatingSet:
    """Find a minimum dominating set for a chordal graph."""

    def __init__(self, graph, tree_decomposition):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.td = tree_decomposition
        self.parent = dict()   # for tree decomposition
        self.dominating_set = set()
        self.cardinality = 0
        import sys
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v() * 2, recursionlimit))

    def run(self, source=None):
        """Executable pseudocode."""
        if source is not None:
            # A single connected component, a single tree.
            self.parent[source] = None   # before _visit
            arg1 = self._visit(source)
            dset = None
            for (white, grey, black) in arg1:
                if len(white) == 0:   # tylko prawidlowe rozwiazania
                    if dset is None:
                        dset = black
                    else:
                        dset = min(dset, black, key=len)
            self.dominating_set.update(dset)
            self.cardinality = len(self.dominating_set)
        else:
            # A forest is possible. NOT FOR TD
            for bag in self.td.iternodes():
                if bag not in self.parent:
                    self.parent[bag] = None   # before _visit
                    arg1 = self._visit(bag)
                    dset = None
                    for (white, grey, black) in arg1:
                        if len(white) == 0:   # tylko prawidlowe rozwiazania
                            if dset is None:
                                dset = black
                            else:
                                dset = min(dset, black, key=len)
                    self.dominating_set.update(dset)
            self.cardinality = len(self.dominating_set)

    def _compose(self, top, arg1, bag, arg2):
        """Compose results."""
        result = []
        separator = set(top) & set(bag)
        introduce = set(top) - separator
        forget = set(bag) - separator
        for (white1, grey1, black1) in arg1:
            # Do kazdego set1 chcemy dolaczyc jak najmniej od dziecka.
            # Mozemy dolaczyc tylko takie rozwiazania, ktore sa zgodne
            # na przecieciu workow.
            white3 = None
            grey3 = None
            black3 = None
            for (white2, grey2, black2) in arg2:
                if (black2 & separator == black1 & separator and
                    len(white2 & forget) == 0):
                    # Jezeli jest zgodnosc przy przecieciu to sprawdzamy.
                    # Nie moga zostac zapomniane wierzcholki niezdominowane.
                    if black3 is None:
                        black3 = black1|black2
                        grey3 = grey1|grey2
                        white3 = (white1 - grey2)|(white2 - grey1)
                    else:
                        b3 = black1|black2
                        g3 = grey1|grey2
                        w3 = (white1 - grey2)|(white2 - grey1)
                        if len(b3) < len(black3):   # mamy lepsze rozwiazanie
                            black3 = b3
                            grey3 = g3
                            white3 = w3
            result.append((white3, grey3, black3))
        return result

    def _visit(self, top):
        """Explore recursively the connected component."""
        # Start from a single node.
        # Tworze liste mozliwych rozwiazan dla bag.
        # To sa wszystkie niepuste podzbiory bag.
        arg1 = []
        for subbag in iter_power_set(top):
            if subbag:
                white = set()
                black = set(subbag)
                grey = set(top) - black
            else:
                white = set(top)
                grey = set()
                black = set()
            arg1.append((white, grey, black))   # kolorowanie
            # Kazdy wierzcholek gdzies musi nalezec.
            assert len(white) + len(grey) + len(black) == len(top)
        # Do zbiorow dominujacych dolaczamy wierzcholki od workow dzieci.
        for bag in self.td.iteradjacent(top):
            if bag not in self.parent:
                self.parent[bag] = top   # before _visit
                arg2 = self._visit(bag)
                arg1 = self._compose(top, arg1, bag, arg2)
        return arg1

# EOF
