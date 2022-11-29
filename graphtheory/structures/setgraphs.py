#!/usr/bin/env python3

import random
from graphtheory.structures.edges import Edge


class Graph(dict):
    """The class defining an unweighted graph (edge weights are ignored).
    
    Nodes can be numbers, strings, or any hashable objects.
    We would like to compare nodes.
    
    Internal structure of an exemplary directed graph:
    {"A": set(["B", "C"]), 
    "B": set(["C", "D"]), 
    "C": set(["D"]), 
    "D": set(["C"]), 
    "E": set(["C"]), 
    "F": set()}
    """

    def __init__(self, n=0, directed=False):
        """Load up a Graph instance.
        
        Parameters
        ----------
        n : int (positive; not used, for compatibility only)
        directed : bool, optional (default=False)
        """
        self.n = n
        self.directed = directed

    def is_directed(self):
        """Test if the graph is directed."""
        return self.directed

    def v(self):
        """Return the number of nodes (the graph order)."""
        return len(self)

    def e(self):
        """Return the number of edges in O(V) time."""
        edges = sum(len(self[node]) for node in self)
        return (edges if self.is_directed() else edges // 2)

    def add_node(self, node):
        """Add a node to the graph."""
        if node not in self:
            self[node] = set()

    def has_node(self, node):
        """Test if a node exists."""
        return node in self

    def del_node(self, node):
        """Remove a node from the graph (with edges)."""
        for source in self:
            self[source].discard(node)
        del self[node]

    def add_edge(self, edge):
        """Add an edge to the graph (missing nodes are created)."""
        if edge.source == edge.target:
            raise ValueError("loops are forbidden")
        self.add_node(edge.source)
        self.add_node(edge.target)
        if edge.target not in self[edge.source]:
            self[edge.source].add(edge.target)
        else:
            raise ValueError("parallel edges are forbidden")
        if not self.is_directed():
            if edge.source not in self[edge.target]:
                self[edge.target].add(edge.source)
            else:
                raise ValueError("parallel edges are forbidden")

    def del_edge(self, edge):
        """Remove an edge from the graph."""
        try:   # checking Edge interface
            source, target = edge.source, edge.target
        except AttributeError:
            source, target = edge   # tuple or list
        self[source].remove(target)
        if not self.is_directed():
            self[target].remove(source)

    def has_edge(self, edge):
        """Test if an edge exists (the weight is not checked)."""
        try:   # checking Edge interface
            source, target = edge.source, edge.target
        except AttributeError:
            source, target = edge   # tuple or list
        return source in self and target in self[source]

    def weight(self, edge):
        """Return the edge weight or zero."""
        try:   # checking Edge interface
            source, target = edge.source, edge.target
        except AttributeError:
            source, target = edge   # tuple or list
        if source in self and target in self[source]:
            return 1
        else:
            return 0

    def iternodes(self):
        """Generate the nodes from the graph on demand."""
        return iter(self)

    def iteradjacent(self, source):
        """Generate the adjacent nodes from the graph on demand."""
        return iter(self[source])

    def iteroutedges(self, source):
        """Generate the outedges from the graph on demand."""
        for target in self[source]:
            yield Edge(source, target)

    def iterinedges(self, source):
        """Generate the inedges from the graph on demand."""
        if self.is_directed():   # O(V) time
            for target in self.iternodes():
                if source in self[target]:
                    yield Edge(target, source)
        else:
            for target in self[source]:
                yield Edge(target, source)

    def iteredges(self):
        """Generate the edges from the graph on demand."""
        for source in self.iternodes():
            for target in self[source]:
                if self.is_directed() or source < target:
                    yield Edge(source, target)

    def show(self):
        """The graph presentation."""
        L = []
        for source in self.iternodes():
            L.append("{} : ".format(source))
            for target in self.iteradjacent(source):
                L.append("{} ".format(target))
            L.append("\n")
        print("".join(L))

    def copy(self):
        """Return the graph copy."""
        new_graph = self.__class__(n=self.n, directed=self.directed)
        for node in self.iternodes():
            new_graph[node] = set(self[node])
        return new_graph

    def transpose(self):
        """Return the transpose of the graph."""
        new_graph = self.__class__(n=self.n, directed=self.directed)
        for node in self.iternodes():
            new_graph.add_node(node)
        for edge in self.iteredges():
            new_graph.add_edge(~edge)
        return new_graph

    def complement(self):
        """Return the complement of the graph."""
        new_graph = self.__class__(n=self.n, directed=self.directed)
        for node in self.iternodes():
            new_graph.add_node(node)
        for source in self.iternodes():
            for target in self.iternodes():
                if source != target:
                    edge = Edge(source, target)
                    if not self.has_edge(edge) and not new_graph.has_edge(edge):
                        new_graph.add_edge(edge)
        return new_graph

    def degree(self, source):
        """Return the degree of the node in the undirected graph."""
        if self.is_directed():
            raise ValueError("the graph is directed")
        return len(self[source])

    def outdegree(self, source):
        """Return the outdegree of the node."""
        return len(self[source])

    def indegree(self, source):
        """Return the indegree of the node."""
        if self.is_directed():   # O(V) time
            counter = 0
            for target in self.iternodes():
                if source in self[target]:
                    counter += 1
            return counter
        else:                   # O(1) time
            return len(self[source])

    def __eq__(self, other):
        """Test if the graphs are equal."""
        if self.is_directed() is not other.is_directed():
            return False
        if set(self) != set(other):   # checking nodes
            return False
        for node in self.iternodes():   # checking neighbors
            if self[node] != other[node]:   # comparing sets
                return False
        return True

    def __ne__(self, other):
        """Test if the graphs are not equal."""
        return not self == other

    def add_graph(self, other):
        """Add a graph to this graph (the current graph is modified)."""
        if self.is_directed() is not other.is_directed():
            raise ValueError("directed vs undirected")
        for node in other.iternodes():
            self.add_node(node)
        for edge in other.iteredges():
            self.add_edge(edge)

# EOF
