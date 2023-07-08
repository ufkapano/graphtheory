#!/usr/bin/env python3

try:
    integer_types = (int, long)
    range = xrange
except NameError:   # Python 3
    integer_types = (int,)


class TreeCenter:
    """Finding the center of a single tree in O(n) time."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        if self.graph.is_directed():
            raise ValueError("the graph is directed")
        self.tree_center = []   # one or two nodes
        self.tree_radius = 0

    def run(self):
        """Executable pseudocode."""
        # Wyznaczam stopnie wierzcholkow drzewa.
        degree_dict = dict((node, self.graph.degree(node))
            for node in self.graph.iternodes())   # O(n) time
        # Identyfikujemy wierzcholki stopnia 1.
        # Wstawiamy je do kolejki.
        Q = [None] * self.graph.v()
        qstart = 0  # pierwszy do pobrania
        qend = 0   # pierwszy wolny
        for node in self.graph.iternodes():
            if degree_dict[node] == 1:
                Q[qend] = node
                qend += 1
        # Teraz etapami odrywamy wierzcholki od drzewa.
        # Czyli usuwamy krawedzie.
        while True:
            if qend == self.graph.v():   # one or two nodes left
                for i in range(qstart, qend):
                    self.tree_center.append(Q[i])
                if len(self.tree_center) == 2:
                    self.tree_radius += 1
                break
            elif qstart == qend:
                raise ValueError("cycle detected")
            for step in range(qend-qstart):
                source = Q[qstart]
                qstart += 1
                degree_dict[source] -= 1
                for target in self.graph.iteradjacent(source):
                    if degree_dict[target] > 0:   # is in the tree?
                        degree_dict[target] -= 1
                    if degree_dict[target] == 1:   # new leaf
                        Q[qend] = target
                        qend += 1
            self.tree_radius += 1

# EOF
