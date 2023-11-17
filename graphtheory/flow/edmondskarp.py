#!/usr/bin/env python3

import collections
from graphtheory.structures.edges import Edge


class EdmondsKarp:
    """The Edmonds-Karp algorithm for computing the maximum flow.
    
    Attributes
    ----------
    graph : input directed graph (flow network)
    residual : directed graph (residual network)
    flow : dict-of-dict
    source : node
    sink : node
    max_flow : number
    
    Notes
    -----
    Based on:
    
    https://en.wikipedia.org/wiki/Edmonds-Karp_algorithm
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

    def run(self, source, sink):
        """Executable pseudocode."""
        if source == sink:
            raise ValueError("source and sink are the same")
        self.source = source
        self.sink = sink
        while True:
            min_capacity = self._find_path_bfs()
            if min_capacity > 0:
                self.max_flow += min_capacity
            else:
                break

    def _find_path_bfs(self):
        """Finding augmenting paths in the residual network."""
        parent = dict((node, None) for node in self.residual.iternodes())
        # Capacity of found path to node.
        capacity = {self.source: float("inf")}
        Q = collections.deque()
        Q.append(self.source)
        while len(Q) > 0:
            node = Q.popleft()
            for edge in self.residual.iteroutedges(node):
                cap = edge.weight - self.flow[edge.source][edge.target]
                if cap > 0 and parent[edge.target] is None:
                    parent[edge.target] = edge.source
                    capacity[edge.target] = min(capacity[edge.source], cap)
                    if edge.target != self.sink:
                        Q.append(edge.target)
                    else:
                        # Backtrack search and write flow.
                        target = self.sink
                        while target != self.source:
                            node = parent[target]
                            self.flow[node][target] += capacity[self.sink]
                            self.flow[target][node] -= capacity[self.sink]
                            target = node
                        return capacity[self.sink]
        return 0


class EdmondsKarpSparse:
    """The Edmonds-Karp algorithm for computing the maximum flow.
    
    Attributes
    ----------
    graph : input directed graph (flow network)
    residual : directed graph (residual network)
    flow : dict-of-dict
    source : node
    sink : node
    max_flow : number
    
    Notes
    -----
    Based on:
    
    https://en.wikipedia.org/wiki/Edmonds-Karp_algorithm
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
        for node in self.graph.iternodes():
            self.flow[node] = dict()
        # Initial capacities for the residual network.
        for edge in self.graph.iteredges():
            self.residual.add_edge(edge)   # original capacity
            self.residual.add_edge(Edge(edge.target, edge.source, 0))
            self.flow[edge.source][edge.target] = 0
            self.flow[edge.target][edge.source] = 0
        # Initial flow is zero.
        self.max_flow = 0

    def run(self, source, sink):
        """Executable pseudocode."""
        if source == sink:
            raise ValueError("source and sink are the same")
        self.source = source
        self.sink = sink
        while True:
            min_capacity = self._find_path_bfs()
            if min_capacity > 0:
                self.max_flow += min_capacity
            else:
                break

    def _find_path_bfs(self):
        """Finding augmenting paths in the residual network."""
        parent = dict((node, None) for node in self.residual.iternodes())
        # Capacity of found path to node.
        capacity = {self.source: float("inf")}
        Q = collections.deque()
        Q.append(self.source)
        while len(Q) > 0:
            node = Q.popleft()
            for edge in self.residual.iteroutedges(node):
                cap = edge.weight - self.flow[edge.source][edge.target]
                if cap > 0 and parent[edge.target] is None:
                    parent[edge.target] = edge.source
                    capacity[edge.target] = min(capacity[edge.source], cap)
                    if edge.target != self.sink:
                        Q.append(edge.target)
                    else:
                        # Backtrack search and write flow.
                        target = self.sink
                        while target != self.source:
                            node = parent[target]
                            self.flow[node][target] += capacity[self.sink]
                            self.flow[target][node] -= capacity[self.sink]
                            target = node
                        return capacity[self.sink]
        return 0

# EOF
