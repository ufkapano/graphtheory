#!/usr/bin/python

import sys
from graphtheory.seriesparallel.spnodes import btree_count_iter


class SPGraphNodeCover:
    """Find a minimum cardinality node cover for sp-graphs."""

    def __init__(self, graph, root):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph       # series-parallel graph
        self.root = root         # binary sp-tree
        self.node_cover = set()
        self.cardinality = 0
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v() * 2, recursionlimit))

    def run(self):
        """Executable pseudocode."""
        arg2 = self._visit(self.root)
        self.node_cover.update(min(arg2, key=len))
        self.cardinality = len(self.node_cover)

    def _compose_series(self, arg1, arg2):
        """Compose results for series operation."""
        r00a, r01a, r10a, r11a = arg1
        r00b, r01b, r10b, r11b = arg2
        r00 = min(r00a|r00b, r01a|r10b, key=len)
        r01 = min(r00a|r01b, r01a|r11b, key=len)
        r10 = min(r10a|r00b, r11a|r10b, key=len)
        r11 = min(r10a|r01b, r11a|r11b, key=len)
        # Powtarzajace sie wierzcholki same wypadna w zbiorach.
        return (r00, r01, r10, r11)

    def _compose_parallel(self, arg1, arg2):
        """Compose results for parallel operation."""
        r00a, r01a, r10a, r11a = arg1
        r00b, r01b, r10b, r11b = arg2
        r00 = r00a|r00b
        r01 = r01a|r01b
        r10 = r10a|r10b
        r11 = r11a|r11b
        # Powtarzajace sie wierzcholki same wypadna w zbiorach.
        return (r00, r01, r10, r11)

    def _compose_jackknife(self, arg1, arg2):
        """Compose results for jackknife operation."""
        r00a, r01a, r10a, r11a = arg1
        r00b, r01b, r10b, r11b = arg2
        r00 = min(r00a|r00b, r00a|r01b, key=len)
        r01 = min(r01a|r10b, r01a|r11b, key=len)
        r10 = min(r10a|r00b, r10a|r01b, key=len)
        r11 = min(r11a|r10b, r11a|r11b, key=len)
        # Powtarzajace sie wierzcholki same wypadna w zbiorach.
        return (r00, r01, r10, r11)

    def _visit(self, node):
        """Traversing postorder."""
        if node.type == "edge":
            # r00 faktycznie jest niepoprawne (to jest r11),
            # ale takie przyjecie upraszcza przetwarzanie..
            # Kolejnosc (r00, r01, r10, r11).
            return (set([node.source, node.target]),
                    set([node.target]), 
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


class SPTreeNodeCover:
    """Find a minimum cardinality node cover for sp-trees."""

    def __init__(self, root):
        """The algorithm initialization."""
        self.root = root         # binary sp-tree
        self.node_cover = set()
        self.cardinality = 0
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(btree_count_iter(self.root), recursionlimit))

    def run(self):
        """Executable pseudocode."""
        arg2 = self._visit(self.root)
        self.node_cover.update(min(arg2, key=len))
        self.cardinality = len(self.node_cover)

    def _compose_series(self, arg1, arg2):
        """Compose results for series operation."""
        r00a, r01a, r10a, r11a = arg1
        r00b, r01b, r10b, r11b = arg2
        r00 = min(r00a|r00b, r01a|r10b, key=len)
        r01 = min(r00a|r01b, r01a|r11b, key=len)
        r10 = min(r10a|r00b, r11a|r10b, key=len)
        r11 = min(r10a|r01b, r11a|r11b, key=len)
        # Powtarzajace sie wierzcholki same wypadna w zbiorach.
        return (r00, r01, r10, r11)

    def _compose_parallel(self, arg1, arg2):
        """Compose results for parallel operation."""
        r00a, r01a, r10a, r11a = arg1
        r00b, r01b, r10b, r11b = arg2
        r00 = r00a|r00b
        r01 = r01a|r01b
        r10 = r10a|r10b
        r11 = r11a|r11b
        # Powtarzajace sie wierzcholki same wypadna w zbiorach.
        return (r00, r01, r10, r11)

    def _compose_jackknife(self, arg1, arg2):
        """Compose results for jackknife operation."""
        r00a, r01a, r10a, r11a = arg1
        r00b, r01b, r10b, r11b = arg2
        r00 = min(r00a|r00b, r00a|r01b, key=len)
        r01 = min(r01a|r10b, r01a|r11b, key=len)
        r10 = min(r10a|r00b, r10a|r01b, key=len)
        r11 = min(r11a|r10b, r11a|r11b, key=len)
        # Powtarzajace sie wierzcholki same wypadna w zbiorach.
        return (r00, r01, r10, r11)

    def _visit(self, node):
        """Traversing postorder."""
        if node.type == "edge":
            # r00 faktycznie jest niepoprawne (to jest r11),
            # ale takie przyjecie upraszcza przetwarzanie..
            # Kolejnosc (r00, r01, r10, r11).
            return (set([node.source, node.target]),
                    set([node.target]), 
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
