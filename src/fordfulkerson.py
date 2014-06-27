#!/usr/bin/python
#
# fordfulkerson.py
#
# The Ford-Fulkerson algorithm.

from edges import Edge
from Queue import LifoQueue


class FordFulkerson:
    """The Ford-Fulkerson algorithm."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("graph is not directed")
        self.graph = graph
        # residual network
        self.residual = graph.__class__(graph.v(), directed=True)
        for node in self.graph.iternodes():
            self.residual.add_node(node)
        # initial capacities for the residual network
        for edge in self.graph.iteredges():
            self.residual.add_edge(edge) # original capacity
            self.residual.add_edge(Edge(edge.target, edge.source, 0))
        # legal flow
        self.flow = dict()
        for source in self.graph.iternodes():
            self.flow[source] = dict()
            for target in self.graph.iternodes():
                self.flow[source][target] = 0
        # initial flow is zero
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
            #print "new path, min_capacity", min_capacity
            # backtrack search and write flow
            target = self.sink
            #print target
            while target != self.source:
                node = parent[target]
                self.flow[node][target] = self.flow[node][target] + min_capacity
                self.flow[target][node] = self.flow[target][node] - min_capacity
                target = node
                #print target

    def find_path(self): # use DFS
        """Finding augmenting paths in the residual network."""
        parent = dict((node, None) for node in self.residual.iternodes())
        # capacity of found path to node
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
    """The Ford-Fulkerson algorithm."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("graph is not directed")
        self.graph = graph
        # residual network
        self.residual = graph.__class__(graph.v(), directed=True)
        for node in self.graph.iternodes():
            self.residual.add_node(node)
        # initial capacities for the residual network
        for edge in self.graph.iteredges():
            self.residual.add_edge(edge) # original capacity
            self.residual.add_edge(Edge(edge.target, edge.source, 0))
        # legal flow
        self.flow = dict()
        for node in self.graph.iternodes():
            self.flow[node] = dict()
        # initial flow is zero
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
            #print "new path, min_capacity", min_capacity
            # backtrack search and write flow
            target = self.sink
            #print target
            while target != self.source:
                node = parent[target]
                self.flow[node][target] = self.flow[node].get(target, 0) + min_capacity
                self.flow[target][node] = self.flow[target].get(node, 0) - min_capacity
                target = node
                #print target

    def find_path(self): # use DFS
        """Finding augmenting paths in the residual network."""
        parent = dict((node, None) for node in self.residual.iternodes())
        # capacity of found path to node
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

# EOF
