#!/usr/bin/env python3

class ChordalNodeCover:
    """Find a minimum node cover for a chordal graph."""

    def __init__(self, graph, tree_decomposition):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.td = tree_decomposition
        self.parent = dict()   # for tree decomposition
        self.node_cover = set()
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
            self.node_cover.update(min(arg1, key=len))
            self.cardinality = len(self.node_cover)
        else:
            # A forest is possible. NOT FOR TD
            for bag in self.td.iternodes():
                if bag not in self.parent:
                    self.parent[bag] = None   # before _visit
                    arg1 = self._visit(bag)
                    self.node_cover.update(min(arg1, key=len))
            self.cardinality = len(self.node_cover)

    def _compose(self, top, arg1, bag, arg2):
        """Compose results."""
        result = []
        separator = set(top) & set(bag)
        for set1 in arg1:
            # Do kazdego set1 chcemy dolaczyc jak najmniej od dziecka.
            # Mozemy dolaczyc tylko takie rozwiazania, ktore sa zgodne
            # na przecieciu workow.
            set3 = None   # set1 poszerzony o set2
            for set2 in arg2:
                #if set2 & set(top) == set1 & set(bag):
                if set2 & separator == set1 & separator:
                    # Jezeli jest zgodnosc przy przecieciu to sprawdzamy.
                    if set3 is None:
                        set3 = set1|set2
                    else:
                        set3 = min(set3, set1|set2, key=len)
            result.append(set3)
        return result

    def _visit(self, top):
        """Explore recursively the connected component."""
        # Start from a single node.
        # Tworze liste mozliwych rozwiazan dla bag.
        # To sa zbiory bez jednego wierzcholka plus caly top.
        arg1 = []
        for node in top:
            arg1.append(set(x for x in top if x != node))
        arg1.append(set(top))
        # Do pokryc dolaczamy wierzcholki od workow dzieci.
        for bag in self.td.iteradjacent(top):
            if bag not in self.parent:
                self.parent[bag] = top   # before _visit
                arg2 = self._visit(bag)
                arg1 = self._compose(top, arg1, bag, arg2)
        return arg1

# EOF
