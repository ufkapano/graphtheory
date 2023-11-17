#!/usr/bin/env python3

import collections
# no recursion
from graphtheory.bipartiteness.bipartite import BipartiteGraphBFS as Bipartite
# with recursion
#from graphtheory.bipartiteness.bipartite import BipartiteGraphDFS as Bipartite


class HopcroftKarpSet:
    """Maximum-cardinality matching using the Hopcroft-Karp algorithm.
    
    Attributes
    ----------
    graph : input bipartite graph
    mate : dict with nodes (values are nodes or None)
    distance : dict with nodes
    cardinality : number
    v1 : first set of nodes
    v2 : second set of nodes
    Q : queue, private
    
    Notes
    -----
    Based on pseudocode from:
    
    http://en.wikipedia.org/wiki/Hopcroft-Karp_algorithm
    """

    def __init__(self, graph):
        """The algorithm initialization.
        
        Parameters
        ----------
        graph : undirected graph
        """
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.mate = dict((node, None) for node in self.graph.iternodes())
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
        self.Q = collections.deque()   # for nodes from self.v1

    def run(self):
        """Executable pseudocode."""
        while self._bfs_stage():
            for node in self.v1:
                if self.mate[node] is None and self._dfs_stage(node):
                    self.cardinality += 1
                    #print self.mate

    def _bfs_stage(self):
        """The BFS stage."""
        for node in self.v1:
            if self.mate[node] is None:
                self.distance[node] = 0
                self.Q.append(node)
            else:
                self.distance[node] = float("inf")
        self.distance[None] = float("inf")
        while len(self.Q) > 0:
            node = self.Q.popleft()
            if self.distance[node] < self.distance[None]:
                for target in self.graph.iteradjacent(node):
                    if self.distance[self.mate[target]] == float("inf"):
                        self.distance[self.mate[target]] = self.distance[node] + 1
                        self.Q.append(self.mate[target])
        return self.distance[None] != float("inf")

    def _dfs_stage(self, node):
        """The DFS stage."""
        if node is not None:
            for target in self.graph.iteradjacent(node):
                if self.distance[self.mate[target]] == self.distance[node] + 1:
                    if self._dfs_stage(self.mate[target]):
                        self.mate[target] = node
                        self.mate[node] = target
                        return True
            self.distance[node] = float("inf")
            return False
        return True


class HopcroftKarpList:
    """Maximum-cardinality matching using the Hopcroft-Karp algorithm.
    
    Attributes
    ----------
    graph : input bipartite graph
    mate : dict with nodes (values are nodes or None)
    distance : dict with nodes
    cardinality : number
    v1 : first set of nodes
    v2 : second set of nodes
    Q : queue, private
    
    Notes
    -----
    Based on pseudocode from:
    
    http://en.wikipedia.org/wiki/Hopcroft-Karp_algorithm
    """

    def __init__(self, graph):
        """The algorithm initialization.
        
        Parameters
        ----------
        graph : undirected graph
        """
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.mate = dict((node, None) for node in self.graph.iternodes())
        self.distance = dict()
        self.cardinality = 0
        algorithm = Bipartite(self.graph)
        algorithm.run()
        self.v1 = list()
        self.v2 = list()
        for node in self.graph.iternodes():
            if algorithm.color[node] == 1:
                self.v1.append(node)
            else:
                self.v2.append(node)
        self.Q = collections.deque()   # for nodes from self.v1

    def run(self):
        """Executable pseudocode."""
        while self._bfs_stage():
            for node in self.v1:
                if self.mate[node] is None and self._dfs_stage(node):
                    self.cardinality += 1
                    #print self.mate

    def _bfs_stage(self):
        """The BFS stage."""
        for node in self.v1:
            if self.mate[node] is None:
                self.distance[node] = 0
                self.Q.append(node)
            else:
                self.distance[node] = float("inf")
        self.distance[None] = float("inf")
        while len(self.Q) > 0:
            node = self.Q.popleft()
            if self.distance[node] < self.distance[None]:
                for target in self.graph.iteradjacent(node):
                    if self.distance[self.mate[target]] == float("inf"):
                        self.distance[self.mate[target]] = self.distance[node] + 1
                        self.Q.append(self.mate[target])
        return self.distance[None] != float("inf")

    def _dfs_stage(self, node):
        """The DFS stage."""
        if node is not None:
            for target in self.graph.iteradjacent(node):
                if self.distance[self.mate[target]] == self.distance[node] + 1:
                    if self._dfs_stage(self.mate[target]):
                        self.mate[target] = node
                        self.mate[node] = target
                        return True
            self.distance[node] = float("inf")
            return False
        return True

# EOF
