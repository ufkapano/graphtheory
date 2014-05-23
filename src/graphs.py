#!/usr/bin/python
#
# graphs.py
#
# Nodes can be numbers, string, or any hashable objects.
# We would like also to compare nodes.
#
# {"A":{"B":1,"C":2}, 
# "B":{"C":3,"D":4}, 
# "C":{"D":5}, 
# "D":{"C":6}, 
# "E":{"C":7}, 
# "F":{}}

from edges import Edge
import random


class Graph(dict):
    """The class defining a graph."""

    def __init__(self, n=0, directed=False):
        """Loads up a Graph instance."""
        self.n = n              # compatibility
        self.directed = directed  # bool

    def v(self):
        """Returns the number of nodes (the graph order)."""
        return len(self)

    def e(self):
        """Returns the number of edges in O(V) time."""
        edges = sum(len(self[node]) for node in self)
        return (edges if self.is_directed() else edges / 2)

    def is_directed(self):
        """Test if the graph is directed."""
        return self.directed

    def add_node(self, node):
        """Add a node to the graph."""
        if node not in self:
            self[node] = dict()

    def has_node(self, node):
        """Test if a node exists."""
        return node in self

    def del_node(self, node):
        """Remove a node from the graph (with edges)."""
        # dictionary changes size during iteration.
        for edge in list(self.iterinedges(node)):
            self.del_edge(edge)
        if self.is_directed():
            for edge in list(self.iteroutedges(node)):
                self.del_edge(edge)
        del self[node]

    def add_edge(self, edge):
        """Add an edge to the graph (missing nodes are created)."""
        self.add_node(edge.source)
        self.add_node(edge.target)
        if edge.target not in self[edge.source]:
            self[edge.source][edge.target] = edge.weight
        if not self.is_directed():
            if edge.source not in self[edge.target]:
                self[edge.target][edge.source] = edge.weight

    def del_edge(self, edge):
        """Remove an edge from the graph."""
        del self[edge.source][edge.target]
        if not self.is_directed():
            del self[edge.target][edge.source]

    def has_edge(self, edge):
        """Test if an edge exists (the weight is not checked)."""
        return edge.source in self and edge.target in self[edge.source]

    def weight(self, edge):
        """Returns the edge weight or zero."""
        if edge.source in self and edge.target in self[edge.source]:
            return self[edge.source][edge.target]
        else:
            return 0

    def iternodes(self):
        """Generates nodes from the graph on demand."""
        return self.iterkeys()

    def iteradjacent(self, source):
        """Generates adjacent nodes from the graph on demand."""
        return self[source].iterkeys()

    def iteroutedges(self, source):
        """Generates outedges from the graph on demand."""
        for target in self[source]:
            yield Edge(source, target, self[source][target])

    def iterinedges(self, source):
        """Generates inedges from the graph on demand."""
        if self.is_directed():   # O(V) time
            for (target, sources_dict) in self.iteritems():
                if source in sources_dict:
                    yield Edge(target, source, sources_dict[source])
        else:
            for target in self[source]:
                yield Edge(target, source, self[target][source])

    def iteredges(self):
        """Generates edges from the graph on demand."""
        for source in self.iternodes():
            for target in self[source]:
                if self.is_directed() or source < target:
                    yield Edge(source, target, self[source][target])

    def show(self):
        """Graph presentation."""
        for source in self.iternodes():
            print source, ":",
            for target in self.iteradjacent(source):
                print "%s(%s)" % (target, self[source][target]),
            print

    def __eq__(self, other):
        """Test if the graphs are equal."""
        if self.is_directed() is not other.is_directed():
            #print "directed and undirected graphs"
            return False
        if self.v() != other.v():
            #print "|V1| != |V2|"
            return False
        for node in self.iternodes():   # O(V) time
            if not other.has_node(node):
                #print "V1 != V2"
                return False
        if self.e() != other.e():   # inefficient, O(E) time
            #print "|E1| != |E2|"
            return False
        for edge in self.iteredges():   # O(E) time
            if not other.has_edge(edge):
                #print "E1 != E2"
                return False
            if edge.weight != other.weight(edge):
                return False
        return True

    def __ne__(self, other):
        """Test if the graphs are not equal."""
        return not self == other

    def add_graph(self, other):
        """Add a graph to this graph (the current graph is modified)."""
        for node in other.iternodes():
            self.add_node(node)
        for edge in other.iteredges():
            self.add_edge(edge)

    @classmethod
    def make_complete(cls, n=1, directed=False):
        """Creates the complete graph."""
        graph = cls(n, directed)
        weights = range(1, 1 + n * (n-1)/2)
        random.shuffle(weights)
        for node in xrange(n):
            graph.add_node(node)
        for source in xrange(n):
            for target in xrange(source + 1, n):   # no loops
                if random.random() > 0.5:   # random direction
                    graph.add_edge(Edge(source, target, weights.pop()))
                else:
                    graph.add_edge(Edge(target, source, weights.pop()))
        return graph

    @classmethod
    def make_sparse(cls, n=1, directed=False, m=0):
        """Creates the sparse graph."""
        if m >= n*(n-1)/2:
            raise ValueError("too mamy edges")
        graph = cls(n, directed)
        weights = range(1, 1 + m)
        random.shuffle(weights)
        for node in xrange(n):
            graph.add_node(node)
        nodes = range(n)
        n_edges = 0
        while n_edges < m:
            source, target = random.sample(nodes, 2)
            if not graph.has_edge(Edge(source, target)):
                graph.add_edge(Edge(source, target, weights.pop()))
                n_edges = n_edges + 1
        return graph

    @classmethod
    def make_connected(cls, n=1, directed=False, m=0):
        """Creates the sparse graph."""
        if m < n - 1 or m >= n * (n - 1)/2:
            raise ValueError("bad number of edges for the connected graph")
        graph = cls(n, directed)
        weights = range(1, m + 1)
        random.shuffle(weights)
        for node in xrange(n):
            graph.add_node(node)
        nodes = set([0])
        # make a tree
        for node in xrange(1, n):
            parent = random.sample(nodes, 1)[0]
            nodes.add(node)
            graph.add_edge(Edge(parent, node, weights.pop()))
        # the rest of edges
        n_edges = n - 1
        while n_edges < m:
            source, target = random.sample(nodes, 2)
            if not graph.has_edge(Edge(source, target)):
                graph.add_edge(Edge(source, target, weights.pop()))
                n_edges = n_edges + 1
        return graph

    @classmethod
    def make_tree(cls, n=1, directed=False):
        """Creates the tree graph."""
        graph = cls(n, directed)
        weights = range(1, n)
        random.shuffle(weights)
        for node in xrange(n):
            graph.add_node(node)
        nodes = set([0])
        for node in xrange(1, n):
            parent = random.sample(nodes, 1)[0]
            nodes.add(node)
            graph.add_edge(Edge(parent, node, weights.pop()))
        return graph

    @classmethod
    def make_random(cls, n=1, directed=False, edge_probability=0.5):
        """Creates the tree graph."""
        graph = cls(n, directed)
        weights = range(1, 1 + n * (n-1)/2)
        random.shuffle(weights)
        for node in xrange(n):
            graph.add_node(node)
        for source in xrange(n):
            for target in xrange(source + 1, n):   # no loops
                if random.random() > edge_probability:
                    continue
                if random.random() > 0.5:   # random direction
                    graph.add_edge(Edge(source, target, weights.pop()))
                else:
                    graph.add_edge(Edge(target, source, weights.pop()))
        return graph

    @classmethod
    def make_grid(cls, size=3):
        """Creates the grid graph with periodic boundary conditions.
        |V| = size * size, |E| = 2 * |V|.
        """
        if size < 3:
            raise ValueError("size too small")
        n = size * size
        graph = cls(n, directed=False)
        weights = range(1, 1 + 2 * n)
        random.shuffle(weights)
        for node in xrange(n):
            graph.add_node(node)
        for node in range(n):
            row = node / size
            col = node % size
            graph.add_edge(Edge(node, row * size + (col + 1) % size, weights.pop())) # line ---
            graph.add_edge(Edge(node, ((row + 1) % size) * size + col, weights.pop())) # line |
        return graph

# EOF
