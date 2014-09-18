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
        self.dist = dict()
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
        while self.bfs_stage():
            for node in self.v1:
                if self.pair[node] is None and self.dfs_stage(node):
                    self.cardinality = self.cardinality + 1
                    #print self.pair

    def bfs_stage(self):
        """The BFS stage."""
        for node in self.v1:
            if self.pair[node] is None:
                self.dist[node] = 0
                self.Q.put(node)
            else:
                self.dist[node] = float("inf")
        self.dist[None] = float("inf")
        while not self.Q.empty():
            node = self.Q.get()
            if self.dist[node] < self.dist[None]:
                for target in self.graph.iteradjacent(node):
                    if self.dist[self.pair[target]] == float("inf"):
                        self.dist[self.pair[target]] = self.dist[node] + 1
                        self.Q.put(self.pair[target])
        return self.dist[None] != float("inf")

    def dfs_stage(self, node):
        """The DFS stage."""
        if node is not None:
            for target in self.graph.iteradjacent(node):
                if self.dist[self.pair[target]] == self.dist[node] + 1:
                    if self.dfs_stage(self.pair[target]):
                        self.pair[target] = node
                        self.pair[node] = target
                        return True
            self.dist[node] = float("inf")
            return False
        return True

# EOF
