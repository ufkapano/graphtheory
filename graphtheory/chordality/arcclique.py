#!/usr/bin/env python3

from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.bipartiteness.bipartiteiset import BipartiteIndependentSet


class GavrilMaximumClique:
    """Finding a maximum clique for circular-arc graphs (Gavril, 1974)."""

    def __init__(self, reprB):
        """The algorithm initialization."""
        # Przedzialy w reprB moga byc w dowolnej kolejnosci.
        self.reprB = reprB
        self.n = len(reprB)   # the number of arcs
        self.maximum_clique = set()
        self.event2arc = {}   # pairs (event, arc), O(n) memory
        for (arc, (head, tail)) in enumerate(self.reprB):
            self.event2arc[head] = arc
            self.event2arc[tail] = arc

    def run(self):   # O(n^2) time
        """Executable pseudocode."""
        for i in range(self.n):   # O(n)
            # Tworze lista etykiet lukow podgrafu posortowana.
            M_i_arcs = self.find_X_Y(i)  # O(n)
            M_i_model = [self.reprB[arc] for arc in M_i_arcs]   # lista par zdarzen podgrafu
            M_i = self.make_abstract_arc_subgraph(M_i_model)
            M_i_complement = M_i.complement()   # O(n^2)
            algorithm = BipartiteIndependentSet(M_i_complement)
            algorithm.run()
            clique_i = algorithm.independent_set
            self.maximum_clique = max(self.maximum_clique, clique_i, key=len)

    def find_X_Y(self, idx):   # O(n)
        X_Y = []   # nie musimy rozdzielac X i Y
        head_curr, tail_curr = self.reprB[idx]

        # all arcs that contain head_curr should be in X
        # all arcs that contain tail_curr, but are not in X, should be in Y
        for arc in range(self.n):   # O(n)
            head, tail = self.reprB[arc]
            if arc == idx:
                X_Y.append(arc)   # do zbioru X
            elif (head < head_curr < tail or
                head_curr < tail < head or
                tail < head < head_curr):
                X_Y.append(arc)   # zbior X
            elif (head < tail_curr < tail or
                tail_curr < tail < head or
                tail < head < tail_curr):
                X_Y.append(arc)   # zbior Y
        return X_Y   # arcs posortowane

    def make_abstract_arc_subgraph(self, pairs):
        # Nie jest potrzebna postac kanoniczna.
        # pairs to pewien podzbior (lista) par z reprB.
        # Wynikowy podgraf uzywa etykiet z pelnego reprB.
        graph = Graph()
        active = set()
    
        # Tworze zbior zdarzen zawartych w pairs.
        events = {event for pair in pairs for event in pair}
    
        # Pierwsza petla 'for' nie uwzglednia zawinietych lukow.
        for event in range(2*self.n):
            if event not in events:
                continue
            curr_arc = self.event2arc[event]   # etykieta luku
            head, tail = self.reprB[curr_arc]   # mamy zapisane konce
            if event == head:   # dodajemy nowy luk, jestesmy w head
                graph.add_node(curr_arc)
                for arc in active:
                    graph.add_edge(Edge(curr_arc, arc))
                active.add(curr_arc)
            else:   # event == tail
                active.discard(curr_arc)   # tu gubimy wsteczne luki
    
        # W tym momencie zbior 'active' zawiera tylko wsteczne krawedzie.
        #print("active po pierwszym for ...")
        #print(active)
        for event in range(2*self.n):
            if event not in events:
                continue
            curr_arc = self.event2arc[event]   # etykieta luku
            head, tail = self.reprB[curr_arc]   # mamy zapisane konce
            if event == head:   # zaczyna sie nowy luk
                if head < tail:   # czyli jest zwykly luk
                    for arc in active:   # sprawdzamy wsteczne luki
                        head_backward, tail_backward = self.reprB[arc]
                        if tail < head_backward:
                            # nie bylo przeciecia w pierwszej petli for
                            graph.add_edge(Edge(curr_arc, arc))
            else:   # event == tail
                active.discard(curr_arc)   # tu zwykle luki tez porzucamy
            if len(active) == 0:
                break   # dalej nie siegaja wsteczne krawedzie
        return graph
