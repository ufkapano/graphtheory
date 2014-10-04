#!/usr/bin/python
#
# hopcroftkarp.py
#
# The Hopcroft-Karp algorithm.
# Based on pseudocode from:
# http://en.wikipedia.org/wiki/Hopcroft%E2%80%93Karp_algorithm

from edges import Edge
from Queue import Queue
#from bipartite import BipartiteGraphBFS as Bipartite
from bipartite import BipartiteGraphDFS as Bipartite


class HopcroftKarp:
    """Maximum-cardinality matching using the Hopcroft-Karp algorithm."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.pair = dict((node, None) for node in self.graph.iternodes())
        self.distance = dict()
        self.cardinality = 0
        algorithm = Bipartite(self.graph)
        algorithm.run()
        self.v1 = set()
        self.v2 = set()
        for node in self.graph.iternodes():
            if algorithm.color[node] == 1:
                self.v1.add(node)
            else:
                self.v2.add(node)
        self.Q = Queue()   # for nodes from self.v1

    def run(self):
        """Executable pseudocode."""
        while self._bfs_stage():
            for node in self.v1:
                if self.pair[node] is None and self._dfs_stage(node):
                    self.cardinality = self.cardinality + 1
                    #print self.pair

    def _bfs_stage(self):
        """The BFS stage."""
        for node in self.v1:
            if self.pair[node] is None:
                self.distance[node] = 0
                self.Q.put(node)
            else:
                self.distance[node] = float("inf")
        self.distance[None] = float("inf")
        while not self.Q.empty():
            node = self.Q.get()
            if self.distance[node] < self.distance[None]:
                for target in self.graph.iteradjacent(node):
                    if self.distance[self.pair[target]] == float("inf"):
                        self.distance[self.pair[target]] = self.distance[node] + 1
                        self.Q.put(self.pair[target])
        return self.distance[None] != float("inf")

    def _dfs_stage(self, node):
        """The DFS stage."""
        if node is not None:
            for target in self.graph.iteradjacent(node):
                if self.distance[self.pair[target]] == self.distance[node] + 1:
                    if self._dfs_stage(self.pair[target]):
                        self.pair[target] = node
                        self.pair[node] = target
                        return True
            self.distance[node] = float("inf")
            return False
        return True

# EOF
