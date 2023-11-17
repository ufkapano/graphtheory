#!/usr/bin/env python3

try:
    range = xrange   # range będzie zawsze generatorem
except NameError:   # Py3
    pass

import collections
from graphtheory.structures.edges import Edge


class HalinGraphPEO:
    """Halin graphs PEO detection."""

    def __init__(self, graph, outer):
        """The algorithm initialization.
        
        Parameters
        ----------
        graph : undirected graph
        outer : a set of outer nodes
        """
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.outer = outer   # nodes from the outer face
        self._graph_copy = self.graph.copy()
        self.order = []           # PEO
        self.outer_next = dict()   # cyclic list
        self.outer_prev = dict()   # cyclic list
        self.parent = dict()

    def run(self):
        """Executable pseudocode."""
        self._find_parent()
        self._find_cycle()
        self._find_peo()

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
        Q.append(node)
        while len(Q) > 0:
            source = Q.popleft()
            for target in self.graph.iteradjacent(source):
                if target not in self.parent:
                    self.parent[target] = source   # before Q.put
                    if target not in self.outer: # nie wychodzimy poza outer
                        Q.append(target)

    def _find_cycle(self):
        """Order nodes from the outer cycle."""
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

    def _find_peo(self):
        """Find PEO for a Halin graph (chordal completion)."""
        # Czasem obiegamy cykl zewnetrzny wiecej niz jeden raz.
        parent_copy = self.parent.copy()   # zmienia sie przy usuwaniu centrum wachlarza
        # wierzcholek poczatkowy, bedziemy szli wzdluz cyklu zewnetrznego.
        current = self.outer.pop()   # pobieramy dowolny
        self.outer.add(current)   # przywracamy
        while True:
            if self._graph_copy.v() == 1 + len(self.outer_next):   # wheel
                for node in self._graph_copy.iternodes():
                    if node in self.outer_next:
                        self.order.append(node)
                    else:
                        hub = node
                self.order.append(hub)
                assert parent_copy[hub] == None   # hub is root
                break
            else:
                # Jak nie ma kola, to sa co najmniej dwa wachlarze.
                # Szukam poczatku wachlarza.
                start = self.outer_next[current]
                while parent_copy[start] == parent_copy[current]:
                    start = self.outer_next[start]
                # Szukam konca wachlarza.
                finish = start   # moze byc tylko jedna galazka, nie wachlarz
                counter = 1   # obliczam szerokosc wachlarza (liczba wierzcholkow na brzegu)
                while parent_copy[self.outer_next[finish]] == parent_copy[start]:
                    finish = self.outer_next[finish]
                    counter += 1
                current = finish   # ustawienie dla nastepnej petli while True
                # Upewniam sie, ze to wachlarz.
                if self._graph_copy.degree(parent_copy[start]) != (counter + 1):
                    continue   # to nie jest wachlarz, przeskakujemy
                # Dodaje wierzcholki do PEO.
                node = self.outer_next[start]
                while node != finish:
                    self.order.append(node)
                    self._graph_copy.del_node(node)
                    self.outer_prev[self.outer_next[node]] = start
                    del self.outer_prev[node]   # usuwam z listy cyklicznej
                    self.outer_next[start] = self.outer_next[node]
                    del self.outer_next[node]   # usuwam z listy cyklicznej
                    node = self.outer_next[start]
                # Teraz zaliczam do PEO centrum wachlarza. TO MOZE BYC ROOT!
                # Chyba popsuje sie parent_copy.
                node = parent_copy[start]
                assert self._graph_copy.degree(node) == 3
                for new_parent in self._graph_copy.iteradjacent(node):
                    if new_parent not in self.outer_next:   # wewnetrzny wierzcholek
                        break
                if parent_copy[node] is None:   # node is root
                    parent_copy[new_parent] = None    # new root
                self.order.append(node)
                self._graph_copy.del_node(node)
                # Uzupelniem krawedzie i parent_copy.
                self._graph_copy.add_edge(Edge(start, new_parent))
                self._graph_copy.add_edge(Edge(finish, new_parent))
                if counter > 2:   # moga byc juz polaczone dla malego wachlarza
                    self._graph_copy.add_edge(Edge(start, finish))
                parent_copy[start] = new_parent
                parent_copy[finish] = new_parent
                assert self._graph_copy.degree(start) == 3
                assert self._graph_copy.degree(finish) == 3

# EOF
