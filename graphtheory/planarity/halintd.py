#!/usr/bin/env python3

try:
    range = xrange   # range będzie zawsze generatorem
except NameError:   # Py3
    pass

import collections
from graphtheory.structures.edges import Edge
from graphtheory.spanningtrees.prim import PrimMST

class HalinGraphTreeDecomposition:
    """Halin graphs tree decomposition."""

    def __init__(self, graph, outer):
        """The algorithm initialization.
        
        Parameters
        ----------
        graph : an undirected connected graph (Halin graph)
        outer : a set of outer nodes
        """
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.outer = outer   # nodes from the outer face
        self._graph_copy = self.graph.copy()
        self.order = []   # PEO
        self.outer_next = dict()   # lista cykliczna
        self.outer_prev = dict()   # lista cykliczna
        self.parent = dict()
        self.cliques = []   # list of sets
        self.td = None   # tree decomposition

    def run(self):
        """Executable pseudocode."""
        self._find_parent()
        self._find_cycle()
        self._find_peo()
        self._find_td()

    def _find_parent(self):   # O(V) time
        """Find the inner tree (dict) using a modified BFS."""
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
        """Find PEO for a Halin graph."""
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
                # Teraz dla grafu kola wyznaczam kliki.
                # Mamy hub w srodku i current na obwodzie ustalone.
                node = self.outer_next[current]
                while current != self.outer_next[node]:
                    node1 = current
                    node2 = self.outer_next[node]
                    node3 = hub
                    clique = set([node, node1, node2, node3])
                    self.cliques.append(clique)
                    node = self.outer_next[node]
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
                    # Tworze klike z node i sasiadow.
                    node1 = start
                    node2 = self.outer_next[node]
                    node3 = parent_copy[start]   # centrum wachlarza
                    clique = set([node, node1, node2, node3])
                    self.cliques.append(clique)
                    # Teraz moge usunac node.
                    self._graph_copy.del_node(node)
                    self.outer_prev[self.outer_next[node]] = start
                    del self.outer_prev[node]   # usuwam z listy cyklicznej
                    self.outer_next[start] = self.outer_next[node]
                    del self.outer_next[node]   # usuwam z listy cyklicznej
                    node = self.outer_next[start]
                # Teraz zaliczam do PEO centrum wachlarza. TO MOZE BYC ROOT!
                # Chyba popsuje sie parent_copy.
                node = parent_copy[start]
                for new_parent in self._graph_copy.iteradjacent(node):
                    if new_parent not in self.outer_next:   # wewnetrzny wierzcholek
                        break
                if parent_copy[node] is None:   # node is root
                    parent_copy[new_parent] = None    # new root
                self.order.append(node)
                # Tworze klike z node i sasiadow.
                clique = set([node, start, finish, new_parent])
                self.cliques.append(clique)
                # Teraz moge usunac node.
                self._graph_copy.del_node(node)
                # Uzupelniem krawedzie i parent_copy.
                self._graph_copy.add_edge(Edge(start, new_parent))
                self._graph_copy.add_edge(Edge(finish, new_parent))
                if counter > 2:   # moga byc juz polaczone dla malego wachlarza
                    self._graph_copy.add_edge(Edge(start, finish))
                parent_copy[start] = new_parent
                parent_copy[finish] = new_parent

    def _find_td(self):
        """Find a tree decomposition for a Halin graph."""
        H = self.graph.__class__(self.graph.v())   # graf przeciec klik maksymalnych
        bag_dict = dict()
        # Budowanie workow.
        for c in self.cliques:
            bag = tuple(sorted(c))
            bag_dict[bag] = c
            H.add_node(bag)
        # Budowanie krawedzi grafu przeciec klik.
        for bag1 in bag_dict:
            for bag2 in bag_dict:
                if bag1 < bag2:
                    inter = bag_dict[bag1].intersection(bag_dict[bag2])
                    if inter:
                        H.add_edge(Edge(bag1, bag2, -len(inter)))
        algorithm = PrimMST(H)
        algorithm.run()
        algorithm.to_tree()
        self.td = algorithm.mst
        #self.td.show()

# EOF
