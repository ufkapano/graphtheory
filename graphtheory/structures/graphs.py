#!/usr/bin/env python3

import random
import collections
from graphtheory.structures.edges import Edge


class Graph(dict):
    """The class defining a graph.
    
    Nodes can be numbers, strings, or any hashable objects.
    We would like to compare nodes.
    
    An exemplary graph structure:
    {"A": {"B": Edge("A", "B", 1), "C": Edge("A", "C", 2)}, 
    "B": {"C": Edge("B", "C", 3), "D": Edge("B", "D", 4)}, 
    "C": {"D": Edge("C", "D", 5)}, 
    "D": {"C": Edge("D", "C", 6)}, 
    "E": {"C": Edge("E", "C", 7)}, 
    "F": {}}
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
        # Structures defining a topological graph.
        self.edge_next = None
        self.edge_prev = None
        self.face2edge = None
        self.edge2face = None

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

    def f(self):
        """Return the number of faces (for planar graphs)."""
        if not self.edge_next:
            raise ValueError("run planarity test first")
        return self.e() + 2 - self.v()   # Euler's formula

    def iterfaces(self):
        """Generate all faces on demand (for planar graphs)."""
        if not self.edge_next:
            raise ValueError("planar embedding not calculated")
        used = set()
        for edge in self.edge_next:
            if edge in used:
                continue
            used.add(edge)
            face = [edge]
            edge = self.edge_next[~edge]
            while edge not in used:
                used.add(edge)
                face.append(edge)
                edge = self.edge_next[~edge]
            yield face

    def iterface(self, start_edge):
        """Generate edges from the same face on demand (for planar graphs)."""
        if not self.edge_next:
            raise ValueError("planar embedding not calculated")
        edge = start_edge
        while True:
            yield edge
            edge = self.edge_next[~edge]
            if edge == start_edge:
                break

    def add_node(self, node):
        """Add a node to the graph."""
        if node not in self:
            self[node] = dict()

    def has_node(self, node):
        """Test if a node exists."""
        return node in self

    def del_node(self, node):
        """Remove a node from the graph (with edges)."""
        # The dictionary changes size during iteration.
        for edge in list(self.iterinedges(node)):
            self.del_edge(edge)
        if self.is_directed():
            for edge in list(self.iteroutedges(node)):
                self.del_edge(edge)
        del self[node]

    def add_edge(self, edge):
        """Add an edge to the graph (missing nodes are created)."""
        if edge.source == edge.target:
            raise ValueError("loops are forbidden")
        self.add_node(edge.source)
        self.add_node(edge.target)
        if edge.target not in self[edge.source]:
            self[edge.source][edge.target] = edge
        else:
            raise ValueError("parallel edges are forbidden")
        if not self.is_directed():
            if edge.source not in self[edge.target]:
                self[edge.target][edge.source] = ~edge
            else:
                raise ValueError("parallel edges are forbidden")

    def del_edge(self, edge):
        """Remove an edge from the graph."""
        try:   # checking Edge interface
            source, target = edge.source, edge.target
        except AttributeError:
            source, target = edge   # tuple or list
        del self[source][target]
        if not self.is_directed():
            del self[target][source]

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
            return self[source][target].weight
        else:
            return 0

    def iternodes(self):
        """Generate all nodes from the graph on demand."""
        return iter(self)

    def iteradjacent(self, source):
        """Generate the adjacent nodes from the graph on demand."""
        return iter(self[source])

    def iteroutedges(self, source):
        """Generate the outedges from the graph on demand."""
        for target in self[source]:
            yield self[source][target]

    def iterinedges(self, source):
        """Generate the inedges from the graph on demand."""
        if self.is_directed():   # O(V) time
            for target in self.iternodes():
                if source in self[target]:
                    yield self[target][source]
        else:
            for target in self[source]:
                yield self[target][source]

    def iteredges(self):
        """Generate all edges from the graph on demand."""
        for source in self.iternodes():
            for target in self[source]:
                if self.is_directed() or source < target:
                    yield self[source][target]

    def iteredges_connected(self, start_edge):
        """Generate all connected edges from the graph on demand.
        
        Used for ConnectedSequentialEdgeColoring.
        """
        if self.is_directed():
            raise ValueError("the graph is directed")
        if not self.has_edge(start_edge):
            raise ValueError("edge not in the graph")
        if start_edge.source > start_edge.target:
            start_edge = ~start_edge
        # Modified BFS starts from here, before while.
        used = set()   # for yielded edges
        parent = dict()   # for BFS tree
        parent[start_edge.source] = None
        parent[start_edge.target] = start_edge.source
        queue = collections.deque()
        queue.append(start_edge.source)
        queue.append(start_edge.target)
        used.add(start_edge)
        yield start_edge
        while len(queue) > 0:   # BFS continued
            source = queue.popleft()
            for edge in self.iteroutedges(source):
                if edge.target not in parent:
                    parent[edge.target] = source   # before Q.append
                    queue.append(edge.target)
                if edge.source > edge.target:
                    edge = ~edge
                if edge not in used:   # start_edge will be detected
                    used.add(edge)
                    yield edge

    def show(self):
        """The graph presentation."""
        L = []
        for source in self.iternodes():
            L.append("{} : ".format(source))
            for edge in self.iteroutedges(source):
                if edge.weight == 1:
                    L.append("{} ".format(edge.target))
                else:
                    L.append("{}({}) ".format(edge.target, edge.weight))
            L.append("\n")
        print("".join(L))

    def copy(self):
        """Return the graph copy."""
        new_graph = self.__class__(n=self.n, directed=self.directed)
        for node in self.iternodes():
            new_graph[node] = dict(self[node])
        # Structures defining a topological graph.
        if self.edge_next:
            new_graph.edge_next = dict(self.edge_next)
        if self.edge_prev:
            new_graph.edge_prev = dict(self.edge_prev)
        if self.face2edge:
            new_graph.face2edge = dict(self.face2edge)
        if self.edge2face:
            new_graph.edge2face = dict(self.edge2face)
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
                if source != target:   # no loops
                    edge = Edge(source, target)
                    if not self.has_edge(edge) and not new_graph.has_edge(edge):
                        new_graph.add_edge(edge)
        return new_graph

    def subgraph(self, nodes):
        """Return the induced subgraph."""
        node_set = set(nodes)
        if any(not self.has_node(node) for node in node_set):
            raise ValueError("nodes not from the graph")
        new_graph = self.__class__(n=len(node_set), directed=self.directed)
        for node in node_set:
            new_graph.add_node(node)
        for edge in self.iteredges():
            if (edge.source in node_set) and (edge.target in node_set):
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
        for node in self.iternodes():   # comparing neighbors
            if self[node] != other[node]:   # different dicts
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
