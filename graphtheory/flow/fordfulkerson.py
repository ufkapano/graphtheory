#!/usr/bin/env python3

import collections
from graphtheory.structures.edges import Edge


class FordFulkerson:
    """The Ford-Fulkerson algorithm for computing the maximum flow.
    
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
    
    Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C., 2009, 
        Introduction to Algorithms, third edition, The MIT Press, 
        Cambridge, London.
    
    https://en.wikipedia.org/wiki/Ford-Fulkerson_algorithm
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
            min_capacity = self._find_path_dfs()
            if min_capacity > 0:
                self.max_flow += min_capacity
            else:
                break

    def _find_path_dfs(self):
        """Finding augmenting paths in the residual network."""
        parent = dict((node, None) for node in self.residual.iternodes())
        # Capacity of found path to node.
        capacity = {self.source: float("inf")}
        stack = collections.deque()
        stack.append(self.source)
        while len(stack) > 0:
            node = stack.pop()
            for edge in self.residual.iteroutedges(node):
                cap = edge.weight - self.flow[edge.source][edge.target]
                if cap > 0 and parent[edge.target] is None:
                    parent[edge.target] = edge.source
                    capacity[edge.target] = min(capacity[edge.source], cap)
                    if edge.target != self.sink:
                        stack.append(edge.target)
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


class FordFulkersonSparse:
    """The Ford-Fulkerson algorithm for computing the maximum flow.
    
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
    
    Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C., 2009, 
        Introduction to Algorithms, third edition, The MIT Press, 
        Cambridge, London.
    
    https://en.wikipedia.org/wiki/Ford-Fulkerson_algorithm
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
            min_capacity = self._find_path_dfs()
            if min_capacity > 0:
                self.max_flow += min_capacity
            else:
                break

    def _find_path_dfs(self):
        """Finding augmenting paths in the residual network."""
        parent = dict((node, None) for node in self.residual.iternodes())
        # Capacity of found path to node.
        capacity = {self.source: float("inf")}
        stack = collections.deque()
        stack.append(self.source)
        while len(stack) > 0:
            node = stack.pop()
            for edge in self.residual.iteroutedges(node):
                cap = edge.weight - self.flow[edge.source][edge.target]
                if cap > 0 and parent[edge.target] is None:
                    parent[edge.target] = edge.source
                    capacity[edge.target] = min(capacity[edge.source], cap)
                    if edge.target != self.sink:
                        stack.append(edge.target)
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


class FordFulkersonWithEdges:
    """The Ford-Fulkerson algorithm for computing the maximum flow.
    
    Attributes
    ----------
    graph : input directed graph (flow network)
    residual : directed graph (residual network)
    flow : dict with pairs (edge, number)
    mate : dict with pairs (edge, edge)
    source : node
    sink : node
    max_flow : number
    
    Notes
    -----
    Based on:
    
    Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C., 2009, 
        Introduction to Algorithms, third edition, The MIT Press, 
        Cambridge, London.
    
    https://en.wikipedia.org/wiki/Ford-Fulkerson_algorithm
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
        self.mate = dict()   # krawedz przeciwna w residual
        # Initial capacities for the residual network.
        for edge in self.graph.iteredges():
            edge2 = Edge(edge.target, edge.source, 0)
            self.residual.add_edge(edge)   # original capacity
            self.residual.add_edge(edge2)
            self.flow[edge] = 0
            self.flow[edge2] = 0
            self.mate[edge] = edge2
            self.mate[edge2] = edge
        # Initial flow is zero.
        self.max_flow = 0

    def run(self, source, sink):
        """Executable pseudocode."""
        if source == sink:
            raise ValueError("source and sink are the same")
        self.source = source
        self.sink = sink
        while True:
            min_capacity = self._find_path_dfs()
            if min_capacity > 0:
                self.max_flow += min_capacity
            else:
                break

    def _find_path_dfs(self):
        """Finding augmenting paths in the residual network."""
        parent = dict((node, None) for node in self.residual.iternodes())
        # Capacity of found path to node.
        capacity = {self.source: float("inf")}
        stack = collections.deque()
        stack.append(self.source)
        while len(stack) > 0:
            node = stack.pop()
            for edge in self.residual.iteroutedges(node):
                cap = edge.weight - self.flow[edge]
                if cap > 0 and parent[edge.target] is None:
                    parent[edge.target] = self.mate[edge] # from target to source
                    capacity[edge.target] = min(capacity[edge.source], cap)
                    if edge.target != self.sink:
                        stack.append(edge.target)
                    else:
                        # Backtrack search and write flow.
                        target = self.sink
                        while target != self.source:
                            edge = parent[target]
                            edge2 = self.mate[edge]
                            self.flow[edge2] += capacity[self.sink]
                            self.flow[edge] -= capacity[self.sink]
                            target = edge.target
                        return capacity[self.sink]
        return 0


class FordFulkersonRecursive:
    """The Ford-Fulkerson algorithm for computing the maximum flow.
    
    Attributes
    ----------
    graph : input directed graph (flow network)
    residual : directed graph (residual network)
    flow : dict with pairs (edge, number)
    mate : dict with pairs (edge, edge)
    source : node
    sink : node
    max_flow : number
    
    Notes
    -----
    Based on:
    
    Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C., 2009, 
        Introduction to Algorithms, third edition, The MIT Press, 
        Cambridge, London.
    
    https://en.wikipedia.org/wiki/Ford-Fulkerson_algorithm
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
        self.parent = None

    def run(self, source, sink):
        """Executable pseudocode."""
        if source == sink:
            raise ValueError("source and sink are the same")
        self.source = source
        self.sink = sink
        while True:
            # Nowe poszukiwanie sciezki za pomoca DFS.
            self.parent = dict((node, None) for node in self.residual.iternodes())
            min_capacity = self._find_path_dfs(self.source, float("inf"))
            if min_capacity > 0:
                self.max_flow += min_capacity
            else:
                break

    def _find_path_dfs(self, source, start_capacity):
        """Finding augmenting paths in the residual network."""
        if source == self.sink:
            return start_capacity
        for edge in self.residual.iteroutedges(source):
            cap = edge.weight - self.flow[edge.source][edge.target]
            if cap > 0 and self.parent[edge.target] is None:
                # Sprawdzamy, czy nie plynelismy ta krawedzia.
                self.parent[edge.target] = edge.source
                min_capacity = min(start_capacity, cap)
                min_capacity = self._find_path_dfs(edge.target, min_capacity)
                if min_capacity > 0:
                    # Dodajemy przeplyw przy powrocie.
                    self.flow[edge.source][edge.target] += min_capacity
                    self.flow[edge.target][edge.source] -= min_capacity
                    return min_capacity
        return 0


class FordFulkersonRecursiveWithEdges:
    """The Ford-Fulkerson algorithm for computing the maximum flow.
    
    Attributes
    ----------
    graph : input directed graph (flow network)
    residual : directed graph (residual network)
    flow : dict with pairs (edge, number)
    mate : dict with pairs (edge, edge)
    source : node
    sink : node
    max_flow : number
    
    Notes
    -----
    Based on:
    
    Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C., 2009, 
        Introduction to Algorithms, third edition, The MIT Press, 
        Cambridge, London.
    
    https://en.wikipedia.org/wiki/Ford-Fulkerson_algorithm
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
        self.mate = dict()   # krawedz przeciwna w residual
        # Initial capacities for the residual network.
        for edge in self.graph.iteredges():
            edge2 = Edge(edge.target, edge.source, 0)
            self.residual.add_edge(edge)   # original capacity
            self.residual.add_edge(edge2)
            self.flow[edge] = 0
            self.flow[edge2] = 0
            self.mate[edge] = edge2
            self.mate[edge2] = edge
        # Initial flow is zero.
        self.max_flow = 0
        self.parent = None

    def run(self, source, sink):
        """Executable pseudocode."""
        if source == sink:
            raise ValueError("source and sink are the same")
        self.source = source
        self.sink = sink
        while True:
            # Nowe poszukiwanie sciezki za pomoca DFS.
            self.parent = dict((node, None) for node in self.residual.iternodes())
            min_capacity = self._find_path_dfs(self.source, float("inf"))
            if min_capacity > 0:
                self.max_flow += min_capacity
            else:
                break

    def _find_path_dfs(self, source, start_capacity):
        """Finding augmenting paths in the residual network."""
        if source == self.sink:
            return start_capacity
        for edge in self.residual.iteroutedges(source):
            cap = edge.weight - self.flow[edge]
            if cap > 0 and self.parent[edge.target] is None:
                # Sprawdzamy, czy nie plynelismy ta krawedzia.
                self.parent[edge.target] = self.mate[edge]
                min_capacity = min(start_capacity, cap)
                min_capacity = self._find_path_dfs(edge.target, min_capacity)
                if min_capacity > 0:
                    # Dodajemy przeplyw przy powrocie.
                    edge2 = self.mate[edge]
                    self.flow[edge] += min_capacity
                    self.flow[edge2] -= min_capacity
                    return min_capacity
        return 0

# EOF
