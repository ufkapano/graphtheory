#!/usr/bin/python

import sys
from graphtheory.seriesparallel.spnodes import btree_count_iter


class SPGraphDominatingSet:
    """Find a minimum dominating set for sp-graphs."""

    def __init__(self, graph, root):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph       # series-parallel graph
        self.root = root         # binary sp-tree
        self.dominating_set = set()
        self.cardinality = 0
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v() * 2, recursionlimit))

    def run(self):
        """Executable pseudocode."""
        arg2 = self._visit(self.root)
        r00, r01, r02, r10, r11, r12, r20, r21, r22 = arg2
        self.dominating_set.update(min(r11, r12, r21, r22, key=len))
        self.cardinality = len(self.dominating_set)

    def _compose_series(self, arg1, arg2):
        """Compose results for series operation."""
        r00a, r01a, r02a, r10a, r11a, r12a, r20a, r21a, r22a = arg1
        r00b, r01b, r02b, r10b, r11b, r12b, r20b, r21b, r22b = arg2
        r00 = min(r00a|r10b, r01a|r00b, r01a|r10b, r02a|r20b, key=len)
        r01 = min(r00a|r11b, r01a|r01b, r01a|r11b, r02a|r21b, key=len)
        r02 = min(r00a|r12b, r01a|r02b, r01a|r12b, r02a|r22b, key=len)
        r10 = min(r10a|r10b, r11a|r00b, r11a|r10b, r12a|r20b, key=len)
        r11 = min(r10a|r11b, r11a|r01b, r11a|r11b, r12a|r21b, key=len)
        r12 = min(r10a|r12b, r11a|r02b, r11a|r12b, r12a|r22b, key=len)
        r20 = min(r20a|r10b, r21a|r00b, r21a|r10b, r22a|r20b, key=len)
        r21 = min(r20a|r11b, r21a|r01b, r21a|r11b, r22a|r21b, key=len)
        r22 = min(r20a|r12b, r21a|r02b, r21a|r12b, r22a|r22b, key=len)
        # Powtarzajace sie wierzcholki same wypadna w zbiorach.
        return (r00, r01, r02, r10, r11, r12, r20, r21, r22)

    def _compose_parallel(self, arg1, arg2):
        """Compose results for parallel operation."""
        r00a, r01a, r02a, r10a, r11a, r12a, r20a, r21a, r22a = arg1
        r00b, r01b, r02b, r10b, r11b, r12b, r20b, r21b, r22b = arg2
        r00 = r00a|r00b
        r01 = min(r01a|r01b, r00a|r01b, r01a|r00b, key=len)
        r02 = r02a|r02b
        r10 = min(r10a|r10b, r00a|r10b, r10a|r00b, key=len)
        r11 = min(r11a|r11b, r11a|r10b, r11a|r01b,
                  r01a|r11b, r10a|r11b, r11a|r00b,
                  r01a|r10b, r10a|r01b, r00a|r11b, key=len)
        r12 = min(r12a|r12b, r12a|r02b, r02a|r12b, key=len)
        r20 = r20a|r20b
        r21 = min(r21a|r21b, r21a|r20b, r20a|r21b, key=len)
        r22 = r22a|r22b
        # Powtarzajace sie wierzcholki same wypadna w zbiorach.
        return (r00, r01, r02, r10, r11, r12, r20, r21, r22)

    def _compose_jackknife(self, arg1, arg2):
        """Compose results for jackknife operation."""
        r00a, r01a, r02a, r10a, r11a, r12a, r20a, r21a, r22a = arg1
        r00b, r01b, r02b, r10b, r11b, r12b, r20b, r21b, r22b = arg2
        r00 = min(r00a|r01b, r00a|r02b, key=len)
        r01 = min(r00a|r11b, r00a|r12b, 
                  r01a|r01b, r01a|r02b, 
                  r01a|r11b, r01a|r12b, key=len)
        r02 = min(r02a|r21b, r02a|r22b, key=len)
        r10 = min(r10a|r01b, r10a|r02b, key=len)
        r11 = min(r10a|r11b, r10a|r12b, 
                  r11a|r11b, r11a|r12b, 
                  r11a|r01b, r11a|r02b, key=len)
        r12 = min(r12a|r21b, r12a|r22b, key=len)
        r20 = min(r20a|r01b, r20a|r02b, key=len)
        r21 = min(r20a|r11b, r20a|r12b, 
                  r21a|r11b, r21a|r12b, 
                  r21a|r01b, r21a|r02b, key=len)
        r22 = min(r22a|r21b, r22a|r22b, key=len)
        # Powtarzajace sie wierzcholki same wypadna w zbiorach.
        return (r00, r01, r02, r10, r11, r12, r20, r21, r22)

    def _visit(self, node):
        """Traversing postorder."""
        if node.type == "edge":
            # r01 faktycznie jest niepoprawne (to jest r22),
            # r02 faktycznie jest niepoprawne (to jest r22),
            # r10 faktycznie jest niepoprawne (to jest r22),
            # r11 faktycznie jest niepoprawne (to jest r22),
            # r20 faktycznie jest niepoprawne (to jest r22),
            # ale takie przyjecie upraszcza przetwarzanie..
            # Kolejnosc (r00, r01, r02, r10, r11, r12, r20, r21, r22).
            return (set(),
                    set([node.source, node.target]),
                    set([node.source, node.target]),
                    set([node.source, node.target]),
                    set([node.source, node.target]),
                    set([node.target]),
                    set([node.source, node.target]),
                    set([node.source]),
                    set([node.source, node.target]))
        arg1 = self._visit(node.left)
        arg2 = self._visit(node.right)
        if node.type == "series":
            return self._compose_series(arg1, arg2)
        elif node.type == "parallel":
            return self._compose_parallel(arg1, arg2)
        elif node.type == "jackknife":
            return self._compose_jackknife(arg1, arg2)
        else:
            raise ValueError("bad node type")


class SPTreeDominatingSet:
    """Find a minimum dominating set for sp-trees."""

    def __init__(self, root):
        """The algorithm initialization."""
        self.root = root         # binary sp-tree
        self.dominating_set = set()
        self.cardinality = 0
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(btree_count_iter(self.root), recursionlimit))

    def run(self):
        """Executable pseudocode."""
        arg2 = self._visit(self.root)
        r00, r01, r02, r10, r11, r12, r20, r21, r22 = arg2
        self.dominating_set.update(min(r11, r12, r21, r22, key=len))
        self.cardinality = len(self.dominating_set)

    def _compose_series(self, arg1, arg2):
        """Compose results for series operation."""
        r00a, r01a, r02a, r10a, r11a, r12a, r20a, r21a, r22a = arg1
        r00b, r01b, r02b, r10b, r11b, r12b, r20b, r21b, r22b = arg2
        r00 = min(r00a|r10b, r01a|r00b, r01a|r10b, r02a|r20b, key=len)
        r01 = min(r00a|r11b, r01a|r01b, r01a|r11b, r02a|r21b, key=len)
        r02 = min(r00a|r12b, r01a|r02b, r01a|r12b, r02a|r22b, key=len)
        r10 = min(r10a|r10b, r11a|r00b, r11a|r10b, r12a|r20b, key=len)
        r11 = min(r10a|r11b, r11a|r01b, r11a|r11b, r12a|r21b, key=len)
        r12 = min(r10a|r12b, r11a|r02b, r11a|r12b, r12a|r22b, key=len)
        r20 = min(r20a|r10b, r21a|r00b, r21a|r10b, r22a|r20b, key=len)
        r21 = min(r20a|r11b, r21a|r01b, r21a|r11b, r22a|r21b, key=len)
        r22 = min(r20a|r12b, r21a|r02b, r21a|r12b, r22a|r22b, key=len)
        # Powtarzajace sie wierzcholki same wypadna w zbiorach.
        return (r00, r01, r02, r10, r11, r12, r20, r21, r22)

    def _compose_parallel(self, arg1, arg2):
        """Compose results for parallel operation."""
        r00a, r01a, r02a, r10a, r11a, r12a, r20a, r21a, r22a = arg1
        r00b, r01b, r02b, r10b, r11b, r12b, r20b, r21b, r22b = arg2
        r00 = r00a|r00b
        r01 = min(r01a|r01b, r00a|r01b, r01a|r00b, key=len)
        r02 = r02a|r02b
        r10 = min(r10a|r10b, r00a|r10b, r10a|r00b, key=len)
        r11 = min(r11a|r11b, r11a|r10b, r11a|r01b,
                  r01a|r11b, r10a|r11b, r11a|r00b,
                  r01a|r10b, r10a|r01b, r00a|r11b, key=len)
        r12 = min(r12a|r12b, r12a|r02b, r02a|r12b, key=len)
        r20 = r20a|r20b
        r21 = min(r21a|r21b, r21a|r20b, r20a|r21b, key=len)
        r22 = r22a|r22b
        # Powtarzajace sie wierzcholki same wypadna w zbiorach.
        return (r00, r01, r02, r10, r11, r12, r20, r21, r22)

    def _compose_jackknife(self, arg1, arg2):
        """Compose results for jackknife operation."""
        r00a, r01a, r02a, r10a, r11a, r12a, r20a, r21a, r22a = arg1
        r00b, r01b, r02b, r10b, r11b, r12b, r20b, r21b, r22b = arg2
        r00 = min(r00a|r01b, r00a|r02b, key=len)
        r01 = min(r00a|r11b, r00a|r12b, 
                  r01a|r01b, r01a|r02b, 
                  r01a|r11b, r01a|r12b, key=len)
        r02 = min(r02a|r21b, r02a|r22b, key=len)
        r10 = min(r10a|r01b, r10a|r02b, key=len)
        r11 = min(r10a|r11b, r10a|r12b, 
                  r11a|r11b, r11a|r12b, 
                  r11a|r01b, r11a|r02b, key=len)
        r12 = min(r12a|r21b, r12a|r22b, key=len)
        r20 = min(r20a|r01b, r20a|r02b, key=len)
        r21 = min(r20a|r11b, r20a|r12b, 
                  r21a|r11b, r21a|r12b, 
                  r21a|r01b, r21a|r02b, key=len)
        r22 = min(r22a|r21b, r22a|r22b, key=len)
        # Powtarzajace sie wierzcholki same wypadna w zbiorach.
        return (r00, r01, r02, r10, r11, r12, r20, r21, r22)

    def _visit(self, node):
        """Traversing postorder."""
        if node.type == "edge":
            # r01 faktycznie jest niepoprawne (to jest r22),
            # r02 faktycznie jest niepoprawne (to jest r22),
            # r10 faktycznie jest niepoprawne (to jest r22),
            # r11 faktycznie jest niepoprawne (to jest r22),
            # r20 faktycznie jest niepoprawne (to jest r22),
            # ale takie przyjecie upraszcza przetwarzanie..
            # Kolejnosc (r00, r01, r02, r10, r11, r12, r20, r21, r22).
            return (set(),
                    set([node.source, node.target]),
                    set([node.source, node.target]),
                    set([node.source, node.target]),
                    set([node.source, node.target]),
                    set([node.target]),
                    set([node.source, node.target]),
                    set([node.source]),
                    set([node.source, node.target]))
        arg1 = self._visit(node.left)
        arg2 = self._visit(node.right)
        if node.type == "series":
            return self._compose_series(arg1, arg2)
        elif node.type == "parallel":
            return self._compose_parallel(arg1, arg2)
        elif node.type == "jackknife":
            return self._compose_jackknife(arg1, arg2)
        else:
            raise ValueError("bad node type")

# EOF
