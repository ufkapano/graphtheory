#!/usr/bin/python

from Queue import LifoQueue
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
        self.source = source
        self.sink = sink
        while True:
            min_capacity, parent = self.find_path()
            if min_capacity == 0:
                break
            self.max_flow = self.max_flow + min_capacity
            # Backtrack search and write flow.
            target = self.sink
            while target != self.source:
                node = parent[target]
                self.flow[node][target] = self.flow[node][target] + min_capacity
                self.flow[target][node] = self.flow[target][node] - min_capacity
                target = node

    def find_path(self):   # use DFS
        """Finding augmenting paths in the residual network."""
        parent = dict((node, None) for node in self.residual.iternodes())
        # Capacity of found path to node.
        capacity = {self.source: float("inf")}
        Q = LifoQueue()
        Q.put(self.source)
        while not Q.empty():
            node = Q.get()
            for edge in self.residual.iteroutedges(node):
                cap = edge.weight - self.flow[edge.source][edge.target]
                if cap > 0 and parent[edge.target] is None:
                    parent[edge.target] = edge.source
                    capacity[edge.target] = min(capacity[edge.source], cap)
                    if edge.target != self.sink:
                        Q.put(edge.target)
                    else:
                        return capacity[self.sink], parent
        return 0, parent


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
        # Initial capacities for the residual network.
        for edge in self.graph.iteredges():
            self.residual.add_edge(edge)   # original capacity
            self.residual.add_edge(Edge(edge.target, edge.source, 0))
        # Legal flow.
        self.flow = dict()
        for node in self.graph.iternodes():
            self.flow[node] = dict()
        # Initial flow is zero.
        self.max_flow = 0

    def run(self, source, sink):
        """Executable pseudocode."""
        self.source = source
        self.sink = sink
        while True:
            min_capacity, parent = self.find_path()
            if min_capacity == 0:
                break
            self.max_flow = self.max_flow + min_capacity
            # Backtrack search and write flow.
            target = self.sink
            while target != self.source:
                node = parent[target]
                self.flow[node][target] = self.flow[node].get(target, 0) + min_capacity
                self.flow[target][node] = self.flow[target].get(node, 0) - min_capacity
                target = node

    def find_path(self):   # use DFS
        """Finding augmenting paths in the residual network."""
        parent = dict((node, None) for node in self.residual.iternodes())
        # Capacity of found path to node.
        capacity = {self.source: float("inf")}
        Q = LifoQueue()
        Q.put(self.source)
        while not Q.empty():
            node = Q.get()
            for edge in self.residual.iteroutedges(node):
                cap = edge.weight - self.flow[edge.source].get(edge.target,0)
                if cap > 0 and parent[edge.target] is None:
                    parent[edge.target] = edge.source
                    capacity[edge.target] = min(capacity[edge.source], cap)
                    if edge.target != self.sink:
                        Q.put(edge.target)
                    else:
                        return capacity[self.sink], parent
        return 0, parent


class FordFulkersonWithEdges:
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
        self.source = source
        self.sink = sink
        while True:
            min_capacity, parent = self.find_path()
            if min_capacity == 0:
                break
            self.max_flow = self.max_flow + min_capacity
            # Backtrack search and write flow.
            target = self.sink
            while target != self.source:
                edge = parent[target]
                edge2 = self.mate[edge]
                self.flow[edge2] = self.flow[edge2] + min_capacity
                self.flow[edge] = self.flow[edge] - min_capacity
                target = edge.target

    def find_path(self):   # use DFS
        """Finding augmenting paths in the residual network."""
        parent = dict((node, None) for node in self.residual.iternodes())
        # Capacity of found path to node.
        capacity = {self.source: float("inf")}
        Q = LifoQueue()
        Q.put(self.source)
        while not Q.empty():
            node = Q.get()
            for edge in self.residual.iteroutedges(node):
                cap = edge.weight - self.flow[edge]
                if cap > 0 and parent[edge.target] is None:
                    parent[edge.target] = self.mate[edge] # from target to source
                    capacity[edge.target] = min(capacity[edge.source], cap)
                    if edge.target != self.sink:
                        Q.put(edge.target)
                    else:
                        return capacity[self.sink], parent
        return 0, parent

# EOF
