#!/usr/bin/env python3

import itertools
import collections
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.traversing.bfs import BFSWithDepthTracker


class ATFreeDominatingSet:
    '''Find a minimum dominating set of AT-free graphs.

    Based on:

    D. Kratsch, Domination and total domination in asteroidal triple-free graphs,
    Discrete Appl. Math. 99 No.1-3, 111-123 (2000).
    '''
    def __init__(self, graph, w=5):
        if graph.is_directed():
            raise ValueError("the graph is directed")
        # Zakladam. ze mamy AT-free graph.
        self.graph = graph
        self.w = w   # 5 for AT-free graphs
        # Na starcie dset to V(G).
        self.dominating_set = set(self.graph.iternodes())   # konwencja
        self.cardinality = self.graph.v()   # konwencja
        self._H = None   # BFS levels, list of sets
        self._max_level = 0   # the maximum BFS level
        self._A = None   # queues (list od dicts)

    def run(self):
        for source in self.graph.iternodes():
            self.find_bfs_levels(source)
            self.init_queue()
            i = 1
            while self._A[i] and i < self._max_level:
                i += 1
                for S1 in self._A[i-1]:
                    # Wchodzimy na poziom H[i].
                    # Probujemy rozne U z poziomu H[i], ale w polaczeniu
                    # z S1 nie mozemy przekroczyc licznosci 'w'.
                    S1, S2, val_S2 = self._A[i-1][S1]
                    for U in self.iter_U(self._H[i], S1):
                        # W S1uU sa wybrane wierzcholki z H[i-2]+H[i-1]+H[i].
                        S1uU = S1.union(U)
                        N_S1uU = self.find_closed_neighborhood(S1uU)
                        if self._H[i-1].issubset(N_S1uU):
                            # Sprawdzone, ze H[i-1] jest zdominowane.
                            R1 = frozenset(S1uU - self._H[i-2])
                            # W R1 zostaja wierzcholki z H[i-1]+H[i]
                            R2 = S2.union(U)   # kandydat na min dset
                            val_R2 = val_S2 + len(U)

                            if R1 not in self._A[i]:   # O(1) time
                                self._A[i][R1] = (R1, R2, val_R2)
                            else:
                                P1, P2, val_P2 = self._A[i][R1]
                                if val_R2 < val_P2:
                                    self._A[i][R1] = (R1, R2, val_R2)
                        # END for U in ...
                    # END for S1 in ...
                # END while ...
            # END for source in ...
            # Przeszlismy przez wszystkie poziomy, badamy max level.
            B1, B2, val_B2 = None, None, float('inf')

            for S1 in self._A[self._max_level]:
                S1, S2, val_S2 = self._A[self._max_level][S1]
                N_S1 = self.find_closed_neighborhood(S1)

                if set(N_S1).issuperset(self._H[self._max_level]) and val_S2 < val_B2:
                    B1, B2, val_B2 = S1, S2, val_S2

            if B2 and val_B2 < self.cardinality:
                self.dominating_set = B2
                self.cardinality = val_B2

    def find_bfs_levels(self, node):
        order = []
        algorithm = BFSWithDepthTracker(self.graph)   # O(n+m) time
        algorithm.run(node, pre_action=lambda pair: order.append(pair))
        self._max_level = max(level for (node, level) in order)   # O(n) time
        self._H = [set() for i in range(self._max_level + 1)]
        for (node, level) in order:
            self._H[level].add(node)

    def init_queue(self):
        # Liczba kolejek zalezy od _max_level, czyli od source
        self._A = [dict() for i in range(self._max_level + 1)]
        # self._A[0] is not used.
        # Initialize self._A[1].
        for r in range(1, self.w + 1):
            # Rozwazamy N[source].
            for S in itertools.combinations(self._H[1].union(self._H[0]), r):
                # 0 < len(S) <= w, S is a tuple.
                # Nie wszystkie zbiory S dominuja H[1]+H[0].
                # Jezeli jest source z H[0], to bedzie zdominowane H[1],
                # bo to jest sasiedztwo source.
                S = frozenset(S)
                self._A[1][S] = (S, S, len(S))

    def iter_U(self, Hi, S):
        for r in range(0, len(Hi) + 1):
            for U in itertools.combinations(Hi, r):
                if len(S.union(U)) <= self.w:
                    yield U

    def find_closed_neighborhood(self, S):
        result = set(S)
        for node in S:
            result.update(self.graph.iteradjacent(node))
        return result

# EOF
