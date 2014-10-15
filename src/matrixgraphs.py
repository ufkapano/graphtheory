#!/usr/bin/python
#
# matrixgraphs.py
#
# Nodes are int from 0 to n-1.

import copy
import random
from edges import Edge


class Graph:
    """The class defining a graph."""

    def __init__(self, n, directed=False):
        """Load up a Graph instance."""
        self.n = n
        self.directed = directed  # bool
        self.data = [[0] * self.n for node in xrange(self.n)]

    def is_directed(self):
        """Test if the graph is directed."""
        return self.directed

    def v(self):
        """Return the number of nodes (the graph order)."""
        return self.n

    def e(self):
        """Return the number of edges in O(V**2) time."""
        counter = 0
        for source in xrange(self.n):
            for target in xrange(self.n):
                if self.data[source][target] != 0:
                    counter = counter + 1
        return (counter if self.directed else counter / 2)

    def add_node(self, node):
        """Add a node to the graph."""
        if not isinstance(node, (int, long)):
            raise ValueError("node is not int or long")
        if node >= self.n or node < 0:
            raise ValueError("node out of range")

    def has_node(self, node):
        """Test if a node exists."""
        if not isinstance(node, (int, long)):
            raise ValueError("node is not int or long")
        if 0 <= node < self.n:
            return True
        else:
            return False

    def del_node(self, source):
        """Remove a node from the graph with edges.
        In fact, the node become isolated. It takes O(V) time."""
        for target in xrange(self.n):
            self.data[source][target] = 0
            self.data[target][source] = 0

    def add_edge(self, edge):
        """Add an edge to the graph."""
        if edge.source == edge.target:
            raise ValueError("loops are forbidden")
        self.add_node(edge.source)
        self.add_node(edge.target)
        if self.data[edge.source][edge.target] == 0:
            self.data[edge.source][edge.target] = edge.weight
        else:
            raise ValueError("parallel edges are forbidden")
        if not self.directed:
            if self.data[edge.target][edge.source] == 0:
                self.data[edge.target][edge.source] = edge.weight
            else:
                raise ValueError("parallel edges are forbidden")

    def del_edge(self, edge):
        """Remove an edge from the graph."""
        self.data[edge.source][edge.target] = 0
        if not self.directed:
            self.data[edge.target][edge.source] = 0

    def has_edge(self, edge):
        """Test if an edge exists (the weight is not checked)."""
        return self.data[edge.source][edge.target] != 0

    def weight(self, edge):
        """Return the edge weight or zero."""
        return self.data[edge.source][edge.target]

    def iternodes(self):
        """Generate the nodes from the graph on demand."""
        return iter(xrange(self.n))

    def iteradjacent(self, source):
        """Generate the adjacent nodes from the graph on demand."""
        for target in xrange(self.n):   # O(V) time
            if self.data[source][target] != 0:
                yield target

    def iteroutedges(self, source):   # O(V) time
        """Generate the outedges from the graph on demand."""
        for target in xrange(self.n):
            if self.data[source][target] != 0:
                yield Edge(source, target, self.data[source][target])

    def iterinedges(self, source):   # O(V) time
        """Generate the inedges from the graph on demand."""
        for target in xrange(self.n):
            if self.data[target][source] != 0:
                yield Edge(target, source, self.data[target][source])

    def iteredges(self):   # O(V**2) time
        """Generate the edges from the graph on demand."""
        for source in xrange(self.n):
            for target in xrange(self.n):
                if self.data[source][target] != 0 and (
                    self.directed or source < target):
                    yield Edge(source, target, self.data[source][target])

    def show(self):
        """The graph presentation."""
        for source in xrange(self.n):
            print source, ":",
            for target in self.iteradjacent(source):
                print "%s(%s)" % (target, self.data[source][target]),
            print

    def copy(self):
        """Return the graph copy in O(V**2) time."""
        new_graph = Graph(n=self.n, directed=self.directed)
        for source in xrange(self.n):
            for target in xrange(self.n):
                new_graph.data[source][target] = self.data[source][target]
        return new_graph

    def transpose(self):
        """Return the transpose of the graph in O(V**2) time."""
        new_graph = Graph(n=self.n, directed=self.directed)
        for source in xrange(self.n):
            for target in xrange(self.n):
                new_graph.data[source][target] = self.data[target][source]
        return new_graph

    def degree(self, source):
        """Return the degree of the node in the undirected graph."""
        if self.is_directed():
            raise ValueError("the graph is directed")
        counter = 0
        for target in xrange(self.n):
            if self.data[source][target] != 0:
                counter = counter + 1
        return counter

    def outdegree(self, source):
        """Return the outdegree of the node."""
        counter = 0
        for target in xrange(self.n):
            if self.data[source][target] != 0:
                counter = counter + 1
        return counter

    def indegree(self, source):
        """Return the indegree of the node."""
        counter = 0
        for target in xrange(self.n):
            if self.data[target][source] != 0:
                counter = counter + 1
        return counter

    def __eq__(self, other):
        """Test if the graphs are equal."""
        if self.is_directed() is not other.is_directed():
            return False
        if self.v() != other.v():
            return False
        for source in xrange(self.n):   # time O(V**2)
            for target in xrange(self.n):
                if self.data[source][target] != other.data[source][target]:
                    return False
        return True

    def __ne__(self, other):
        """Test if the graphs are not equal."""
        return not self == other

    def add_graph(self, other):
        """Add a graph to this graph (the current graph is modified)."""
        if self.is_directed() is not other.is_directed():
            raise ValueError("directed vs undirected")
        if self.v() != other.v():
            raise ValueError("different numbers of nodes")
        for node in other.iternodes():
            self.add_node(node)
        for edge in other.iteredges():
            self.add_edge(edge)

    @classmethod
    def make_complete(cls, n=1, directed=False):
        """Create the complete graph."""
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
        """Create a sparse graph."""
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
        """Create a connected graph."""
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
        """Create a tree graph."""
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
        """Create a random graph."""
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

#   |     |     |
# --2s--(2s+1)-(2s+2)--
#   |     |     |
# --s---(s+1)-(s+2)--
#   |     |     |
# --0-----1-----2---
#   |     |     |

    @classmethod
    def make_grid(cls, size=3):
        """Create the grid graph with periodic boundary conditions.
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

#   |  /  |  /  | /
# --2s--(2s+1)-(2s+2)--
# / |  /  |  /  | /
# --s---(s+1)-(s+2)--
# / |  /  |  /  | /
# --0-----1-----2---
# / |  /  |  /  |

    @classmethod
    def make_triangle(cls, size=3):
        """Create the triangle network with periodic boundary conditions.
        |V| = size * size, |E| = 3 * |V|.
        """
        if size < 3:
            raise ValueError("size too small")
        n = size * size
        graph = cls(n, directed=False)
        weights = range(1, 1 + 3 * n)
        random.shuffle(weights)
        for node in xrange(n):
            graph.add_node(node)
        for node in range(n):
            row = node / size
            col = node % size
            graph.add_edge(Edge(node, row * size + (col + 1) % size, weights.pop())) # line ---
            graph.add_edge(Edge(node, ((row + 1) % size) * size + col, weights.pop())) # line |
            graph.add_edge(Edge(node, ((row + 1) % size) * size + (col + 1) % size, weights.pop())) # line /
        return graph

# --1--3--5--...--(2s+1)-
#   |  |  |         |
# --0--2--4--...--(2s)---

    @classmethod
    def make_ladder(cls, size=3):
        """Create the ladder with periodic boundary conditions.
        |V| = 2 * size, |E| = 3 * size.
        """
        if size < 3:
            raise ValueError("size too small")
        n = 2 * size
        graph = cls(n, directed=False)
        weights = range(1, 1 + 3 * size)
        random.shuffle(weights)
        for node in xrange(n):
            graph.add_node(node)
        for i in xrange(size):
            node = 2 * i
            graph.add_edge(Edge(node, node + 1, weights.pop())) # line |
            graph.add_edge(Edge(node, (node + 2) % n, weights.pop())) # line ---
            graph.add_edge(Edge(node + 1, (node + 3) % n, weights.pop())) # line ---
        return graph

    @classmethod
    def make_flow_network(cls, n=1):
        """Create a flow network."""
        graph = cls(n, True)
        for node in xrange(n):
            graph.add_node(node)
        node_list = range(1, n)
        source = 0
        sink = n - 1
        used = dict((node, False) for node in xrange(n))
        used[source] = True
        # create paths from source to sink
        while any(used[node] == False for node in used):
            random.shuffle(node_list)
            start = source
            for target in node_list:
                edge = Edge(start, target, random.randint(1, n))
                if not (graph.has_edge(edge) or graph.has_edge(Edge(target, start))):
                    graph.add_edge(edge)
                    used[target] = True
                if target == sink:
                    break
                else:
                    start = target
        # all nodes are on paths; new edges can be added
        return graph

# EOF
