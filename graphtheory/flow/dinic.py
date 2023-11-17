#!/usr/bin/env python3

import collections
from graphtheory.structures.edges import Edge


class Dinic:
    """The Dinic's algorithm for computing the maximum flow.
    
    Attributes
    ----------
    graph : input directed graph (flow network)
    residual : directed graph (residual network)
    flow : dict-of-dict
    source : node
    sink : node
    max_flow : number
    level : dict with node levels
    
    Notes
    -----
    Based on:
    
    https://en.wikipedia.org/wiki/Dinic's_algorithm
    
    http://www.geeksforgeeks.org/dinics-algorithm-maximum-flow/
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("the graph is not directed")
        self.graph = graph
        self.residual = self.graph.__class__(self.graph.v(), directed=True)
        for node in self.graph.iternodes():
            self.residual.add_node(node)
        # Initial capacities for the residual network.
        for edge in self.graph.iteredges():
            self.residual.add_edge(edge)   # original capacity
            self.residual.add_edge(Edge(edge.target, edge.source, 0))
        # Legal flow.
        self.flow = dict()
        for source in self.graph.iternodes():
            self.flow[source] = dict()
            for target in self.graph.iternodes():
                self.flow[source][target] = 0
        # Initial flow is zero.
        self.max_flow = 0
        # Levels of nodes.
        self.level = None

    def run(self, source, sink):
        """Executable pseudocode."""
        if source == sink:
            raise ValueError("source and sink are the same")
        self.source = source
        self.sink = sink
        while self._bfs():
            while True:
                min_capacity = self._dfs(self.source, float("inf"))
                if min_capacity > 0:
                    self.max_flow += min_capacity
                else:
                    break

    def _bfs(self):
        """Find if more flow can be sent from source to sink.
        Assign levels to nodes."""
        # Wyzerowanie poziomow wierzcholkow.
        self.level = dict((node, None) for node in self.residual.iternodes())
        # BFS rozpoczynamy w self.source.
        self.level[self.source] = 0
        Q = collections.deque()
        Q.append(self.source)
        while len(Q) > 0:   # BFS loop
            node = Q.popleft()
            for edge in self.residual.iteroutedges(node):
                # Rozpoznajemy wierzcholki nieodwiedzone po tym,
                # ze nie maja ustawionego parametru level.
                cap = edge.weight - self.flow[edge.source][edge.target]
                if self.level[edge.target] is None and cap > 0:
                    self.level[edge.target] = self.level[edge.source] + 1
                    Q.append(edge.target)
        return self.level[self.sink] is not None

    def _dfs(self, node, start_capacity):
        """A DFS based function to send flow after BFS has figured out
        that there is a possible flow. Levels were constructed during BFS."""
        if node == self.sink:
            return start_capacity
        for edge in self.residual.iteroutedges(node):
            cap = edge.weight - self.flow[edge.source][edge.target]
            if (self.level[edge.target] == self.level[edge.source] + 1) and cap > 0:
                min_capacity = min(start_capacity, cap)
                min_capacity = self._dfs(edge.target, min_capacity)
                if min_capacity > 0:
                    # Zapisujemy przeplyw przy wychodzeniu z rekurencji.
                    self.flow[edge.source][edge.target] += min_capacity
                    self.flow[edge.target][edge.source] -= min_capacity
                    return min_capacity
        return 0


class DinicSparse:
    """The Dinic's algorithm for computing the maximum flow.
    
    Attributes
    ----------
    graph : input directed graph (flow network)
    residual : directed graph (residual network)
    flow : dict-of-dict
    source : node
    sink : node
    max_flow : number
    level : dict with node levels
    
    Notes
    -----
    Based on:
    
    https://en.wikipedia.org/wiki/Dinic's_algorithm
    
    http://www.geeksforgeeks.org/dinics-algorithm-maximum-flow/
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("the graph is not directed")
        self.graph = graph
        self.residual = self.graph.__class__(self.graph.v(), directed=True)
        for node in self.graph.iternodes():
            self.residual.add_node(node)
        # Legal flow.
        self.flow = dict()
        for source in self.graph.iternodes():
            self.flow[source] = dict()
        # Initial capacities for the residual network.
        for edge in self.graph.iteredges():
            self.residual.add_edge(edge)   # original capacity
            self.residual.add_edge(Edge(edge.target, edge.source, 0))
            self.flow[edge.source][edge.target] = 0
            self.flow[edge.target][edge.source] = 0
        # Initial flow is zero.
        self.max_flow = 0
        # Levels of nodes.
        self.level = None

    def run(self, source, sink):
        """Executable pseudocode."""
        if source == sink:
            raise ValueError("source and sink are the same")
        self.source = source
        self.sink = sink
        while self._bfs():
            while True:
                min_capacity = self._dfs(self.source, float("inf"))
                if min_capacity > 0:
                    self.max_flow += min_capacity
                else:
                    break

    def _bfs(self):
        """Find if more flow can be sent from source to sink.
        Assign levels to nodes."""
        # Wyzerowanie poziomow wierzcholkow.
        self.level = dict((node, None) for node in self.residual.iternodes())
        self.level[self.source] = 0
        Q = collections.deque()
        Q.append(self.source)
        while len(Q) > 0:   # BFS loop
            node = Q.popleft()
            for edge in self.residual.iteroutedges(node):
                # Rozpoznajemy wierzcholki nieodwiedzone po tym,
                # ze nie maja ustawionego parametru level.
                cap = edge.weight - self.flow[edge.source][edge.target]
                if self.level[edge.target] is None and cap > 0:
                    self.level[edge.target] = self.level[edge.source] + 1
                    Q.append(edge.target)
        return self.level[self.sink] is not None

    def _dfs(self, node, start_capacity):
        """A DFS based function to send flow after BFS has figured out
        that there is a possible flow. Levels were constructed during BFS."""
        if node == self.sink:
            return start_capacity
        for edge in self.residual.iteroutedges(node):
            cap = edge.weight - self.flow[edge.source][edge.target]
            if (self.level[edge.target] == self.level[edge.source] + 1) and cap > 0:
                min_capacity = min(start_capacity, cap)
                min_capacity = self._dfs(edge.target, min_capacity)
                if min_capacity > 0:
                    # Zapisujemy przeplyw przy wychodzeniu z rekurencji.
                    self.flow[edge.source][edge.target] += min_capacity
                    self.flow[edge.target][edge.source] -= min_capacity
                    return min_capacity
        return 0

# EOF
