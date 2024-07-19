#!/usr/bin/env python3

import itertools
from graphtheory.structures.edges import Edge
from graphtheory.permutations.permtools import perm_is_connected
from graphtheory.permutations.permtools import make_abstract_perm_graph
from graphtheory.permutations.permtools import make_bipartite_perm
from graphtheory.chordality.peotools import find_peo_mcs
from graphtheory.chordality.peotools import is_peo1, is_peo2

class PermGraphPEO:
    """Finding a chordal completion for permutation graphs in O(n^4) time."""

    def __init__(self, perm):
        """The algorithm initialization."""
        self.perm = perm
        self.n = len(self.perm)
        if not perm_is_connected(self.perm):   # O(n) time
            raise ValueError("perm is not connected")
        self.graph = make_abstract_perm_graph(self.perm)
        self.new_edges = []
        self.order = None

    def run(self):
        """Executable pseudocode."""
        self.order = find_peo_mcs(self.graph)
        if is_peo1(self.graph, self.order):   # pomijamy chordal graphs
            #print("perm graph is chordal")
            return

        cycle2chord = dict()
        chord2cycle = dict()
        # Szukam 4 liczb tworzacych indukowany graf C_4.
        for (i,j,k,r) in itertools.combinations(range(self.n), 4):
            if self.perm[k] < self.perm[r] < self.perm[i] < self.perm[j]:
                cycle = (self.perm[i], self.perm[k], self.perm[j], self.perm[r])
                chord1 = Edge(self.perm[i], self.perm[j])
                chord2 = Edge(self.perm[k], self.perm[r])
                cycle2chord[cycle] = {chord1, chord2}
                if chord1 in chord2cycle:
                    chord2cycle[chord1].add(cycle)
                else:
                    chord2cycle[chord1] = {cycle}
                if chord2 in chord2cycle:
                    chord2cycle[chord2].add(cycle)
                else:
                    chord2cycle[chord2] = {cycle}

        # Chce pobierac cieciwy pokrywajace najwiecej cykli.
        # key: ile cykli pokrywa cieciwa
        # value: lista cieciw
        n_cycles = len(cycle2chord)
        bucket = list(set() for chord in range(n_cycles+1))
        for chord in chord2cycle:
            bucket[len(chord2cycle[chord])].add(chord)

        maxi = n_cycles
        while True:   # w jednym kroku mozna usunac kilka cykli
            while not bucket[maxi]:   # szukamy niepustego bukietu
                maxi -= 1
            chord1 = bucket[maxi].pop()   # pobieramy cieciwe
            bucket[maxi].add(chord1)   # przywracam dla wygody
            self.new_edges.append(chord1)
            # usuwamy pokryte cykle
            for cycle in tuple(chord2cycle[chord1]):   # kopia, pokryte cykle
                for chord2 in cycle2chord[cycle]:
                    k = len(chord2cycle[chord2])   # szukam bucket
                    chord2cycle[chord2].remove(cycle)
                    bucket[k].remove(chord2)
                    bucket[k-1].add(chord2)
                del cycle2chord[cycle]
            del chord2cycle[chord1]
            if not cycle2chord:
                #print("chord2cycle", chord2cycle)
                assert all(len(chord2cycle[chord]) == 0 for chord in chord2cycle)
                break
        # Creating a chordal completion.
        for edge in self.new_edges:
            self.graph.add_edge(edge)
        self.order = find_peo_mcs(self.graph)
        assert is_peo1(self.graph, self.order)

# EOF
