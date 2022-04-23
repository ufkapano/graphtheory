#!/usr/bin/env python3

import sys
import random
#from graphtheory.dominatingsets.dsetus import UnorderedSequentialDominatingSet as DominatingSet
#from graphtheory.dominatingsets.dsetrs import RandomSequentialDominatingSet as DominatingSet
from graphtheory.dominatingsets.dsetlf import LargestFirstDominatingSet as DominatingSet

class HybridDominatingSet:
    """Find a minimum dominating set using a hybrid algorithm."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        algorithm = DominatingSet(graph)
        algorithm.run()
        self.dominating_set = algorithm.dominating_set
        self._tmp_set = set()
        self.cardinality = len(self.dominating_set)
        self.node_list = list(self.graph.iternodes())
        #random.shuffle(self.node_list)
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(self.graph.v()*2, recursionlimit))

    def run(self):
        """Executable pseudocode."""
        # Musimy sprawdzic wszystkie mozliwosci, aby znalezc min dset.
        self._try_node(0)
        self.cardinality = len(self.dominating_set)

    def _try_node(self, k):
        """Try to add node_list[k] to dset."""
        node = self.node_list[k]
        # Jezeli self._tmp_set ma juz tyle nodes co self.dominating_set,
        # to nie ma sensu isc glebiej.
        if len(self._tmp_set) >= len(self.dominating_set):
            return
        # Najpierw sprawdzam mozliwosc, ze nalezy do dset.
        self._tmp_set.add(node)
        if k < self.graph.v() - 1:
            self._try_node(k+1)
        else:
            if len(self._tmp_set) < len(self.dominating_set) and self._is_dset():
                self.dominating_set = set(self._tmp_set)
        self._tmp_set.remove(node)
        # Teraz sprawdzam mozliwosc, ze nie nalezy do dset.
        if k < self.graph.v() - 1:
            self._try_node(k+1)
        else:
            if len(self._tmp_set) < len(self.dominating_set) and self._is_dset():
                self.dominating_set = set(self._tmp_set)

    def _is_dset(self):
        """Test if _tmp_set is dset in O(V+E) time."""
        for source in self.graph.iternodes():
            if source in self._tmp_set:
                continue
            covered = False
            for target in self.graph.iteradjacent(source):
                if target in self._tmp_set:
                    covered = True
                    break
            if not covered:
                return False
        return True

# EOF
