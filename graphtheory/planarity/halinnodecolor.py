#!/usr/bin/env python3

try:
    range = xrange   # range będzie zawsze generatorem
except NameError:   # Py3
    pass

import collections
from graphtheory.structures.edges import Edge


class HalinNodeColoring:
    """Halin graphs node coloring."""

    def __init__(self, graph, outer):
        """The algorithm initialization.
        
        Parameters
        ----------
        graph : undirected graph
        outer : a set of outer nodes
        color : dict with nodes (values are colors)
        """
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.outer = outer   # nodes from the outer face
        self.color = dict((node, None) for node in self.graph.iternodes())
        self.outer_next = dict()   # lista cykliczna
        self.outer_prev = dict()   # lista cykliczna
        self.parent = dict()   # inner tree

    def run(self):
        """Executable pseudocode."""
        self._find_parent()   # tree coloring
        self._find_cycle()
        self._cycle_coloring()

    def _find_parent(self):   # O(V) time
        """Find the inner tree (dict) using modified BFS."""
        # Robimy BFS z wierzcholka wewnetrznego.
        for source in self.graph.iternodes():
            if source not in self.outer:
                self._visit(source)
                break

    def _visit(self, node):
        """Explore the connected component."""
        Q = collections.deque()
        self.parent[node] = None   # before Q.put
        self.color[node] = 0   # before Q.put
        Q.append(node)
        while len(Q) > 0:
            source = Q.popleft()
            for target in self.graph.iteradjacent(source):
                #if target not in self.parent:
                if self.color[target] is None:
                    self.parent[target] = source   # before Q.put
                    self.color[target] = (self.color[source] + 1) % 2  # before Q.put
                    if target not in self.outer: # nie wychodzimy poza outer
                        Q.append(target)

    def _find_cycle(self):
        """Order nodes from the outer cycle."""
        # Tutaj nie korzystam z drzewa parent!
        # Ustalam dwa pierwsze wierzcholki z cyklu zewnetrzego.
        node1 = self.outer.pop()   # pobieramy dowolny
        self.outer.add(node1)   # przywracamy
        for node2 in self.graph.iteradjacent(node1):
            if node2 in self.outer:
                break   # mamy drugi na brzegu
        # Poczatek budowy listy cyklicznej podwojnie powiazanej.
        self.outer_next[node1] = node2
        self.outer_prev[node1] = node2
        self.outer_next[node2] = node1
        self.outer_prev[node2] = node1
        # Dodawanie kolejnych wierzcholkow do listy cyklicznej.
        for step in range(len(self.outer)-2):
            for node3 in self.graph.iteradjacent(node2):
                if node3 in self.outer:
                    if node3 == self.outer_prev[node2]:
                        continue   # stad przyszlismy
                    else:
                        node4 = node3   # nastepny do dodania
            self.outer_next[node4] = node1
            self.outer_prev[node4] = node2
            self.outer_prev[node1] = node4
            self.outer_next[node2] = node4
            node2 = node4

    def _cycle_coloring(self):
        """Node coloring of the outer cycle."""
        # Drzewo juz jest pokolorowane.
        node1 = self.outer.pop()   # pobieramy dowolny
        self.outer.add(node1)   # przywracamy
        # Jakie kolory sa na cyklu zewnetrznym?
        outer_color_set = set(self.color[node] for node in self.outer)
        # CASE 1. Even cycle.
        if len(self.outer) % 2 == 0:
            current = node1
            for i in range(len(self.outer)):
                if i % 2 == 1:
                    self.color[current] = 2
                current = self.outer_next[current]
        # CASE 2. Wheel graph with odd cycle.
        # Caly cykl ma kolor 1, hub ma kolor 0.
        elif self.graph.v() == len(self.outer) + 1:
            assert len(self.outer) % 2 == 1
            # Testing colors.
            for node in self.graph.iternodes():
                if node in self.outer:
                    assert self.color[node] == 1
                else:
                    assert self.color[node] == 0
            current = node1
            self.color[current] = 3
            current = self.outer_next[current]
            for i in range(1, len(self.outer)):
                if i % 2 == 1:
                    self.color[current] = 2
                current = self.outer_next[current]
        # CASE 3. Odd cycle with two colors.
        elif len(outer_color_set) == 2:
            # Szukam w cyklu sasiadow z kolorami 0 i 1.
            assert len(self.outer) % 2 == 1
            current = node1
            while True:
                if self.color[current] != self.color[self.outer_prev[current]]:
                    current = self.outer_next[current]
                    break
                current = self.outer_next[current]
            for i in range(len(self.outer)-2):
                if i % 2 == 0:
                    self.color[current] = 2
                current = self.outer_next[current]
        # CASE 4. Odd cycle with one color.
        else:
            assert len(self.outer) % 2 == 1
            c1 = outer_color_set.pop()   # cycle color (0 or 1)
            c2 = (c1 + 1) % 2
            c3 = 2
            # Szukam nieparzystego wachlarza lub pseudowachlarza.
            # Szukam poczatku (pseudo)wachlarza.
            current = node1
            while True:
                start = self.outer_next[current]
                while self.parent[start] == self.parent[current]:
                    start = self.outer_next[start]
                # Szukam konca (pseudo)wachlarza.
                finish = start   # moze byc tylko jedna galazka, nie wachlarz
                counter = 1   # obliczam szerokosc wachlarza (liczba wierzcholkow na brzegu)
                while self.parent[self.outer_next[finish]] == self.parent[start]:
                    finish = self.outer_next[finish]
                    counter += 1
                current = finish   # ustawienie dla nastepnej petli while True
                # Sprawdzam czy nieparzysty (pseudo)wachlarz.
                if counter % 2 == 0:
                    #print "even (pseudo)fan"
                    continue
                else:
                    #print "odd (pseudo)fan"
                    break
            # Upewniam sie, ze to wachlarz.
            #if self.graph.degree(self.parent[start]) != (counter + 1):
            #    print "pseudofan detected"
            #else:
            #    print "fan detected"
            # Przekolorowanie wachlarza [c2, c1, ..., c1, c2].
            self.color[self.parent[start]] = c3
            for i in range(counter):
                if i % 2 == 0:
                    self.color[start] = c2
                else:
                    self.color[start] = c1
                start = self.outer_next[start]
            # Przekolorowanie poza wachlarzem [c1, (c3|c2)].
            assert (len(self.outer)-counter) % 2 == 0
            for i in range(len(self.outer)-counter):
                if i % 2 == 1: # co drugi przekolorujemy
                    if self.color[self.parent[start]] == c2:
                        self.color[start] = c3
                    else:
                        self.color[start] = c2
                start = self.outer_next[start]

# EOF
