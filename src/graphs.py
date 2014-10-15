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

import random
from edges import Edge


class Graph(dict):
    """The class defining a graph."""

    def __init__(self, n=0, directed=False):
        """Load up a Graph instance."""
        self.n = n              # compatibility
        self.directed = directed  # bool

    def is_directed(self):
        """Test if the graph is directed."""
        return self.directed

    def v(self):
        """Return the number of nodes (the graph order)."""
        return len(self)

    def e(self):
        """Return the number of edges in O(V) time."""
        edges = sum(len(self[node]) for node in self)
        return (edges if self.is_directed() else edges / 2)

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
        if edge.source == edge.target:
            raise ValueError("loops are forbidden")
        self.add_node(edge.source)
        self.add_node(edge.target)
        if edge.target not in self[edge.source]:
            self[edge.source][edge.target] = edge.weight
        else:
            raise ValueError("parallel edges are forbidden")
        if not self.is_directed():
            if edge.source not in self[edge.target]:
                self[edge.target][edge.source] = edge.weight
            else:
                raise ValueError("parallel edges are forbidden")

    def del_edge(self, edge):
        """Remove an edge from the graph."""
        del self[edge.source][edge.target]
        if not self.is_directed():
            del self[edge.target][edge.source]

    def has_edge(self, edge):
        """Test if an edge exists (the weight is not checked)."""
        return edge.source in self and edge.target in self[edge.source]

    def weight(self, edge):
        """Return the edge weight or zero."""
        if edge.source in self and edge.target in self[edge.source]:
            return self[edge.source][edge.target]
        else:
            return 0

    def iternodes(self):
        """Generate the nodes from the graph on demand."""
        return self.iterkeys()

    def iteradjacent(self, source):
        """Generate the adjacent nodes from the graph on demand."""
        return self[source].iterkeys()

    def iteroutedges(self, source):
        """Generate the outedges from the graph on demand."""
        for target in self[source]:
            yield Edge(source, target, self[source][target])

    def iterinedges(self, source):
        """Generate the inedges from the graph on demand."""
        if self.is_directed():   # O(V) time
            for (target, sources_dict) in self.iteritems():
                if source in sources_dict:
                    yield Edge(target, source, sources_dict[source])
        else:
            for target in self[source]:
                yield Edge(target, source, self[target][source])

    def iteredges(self):
        """Generate the edges from the graph on demand."""
        for source in self.iternodes():
            for target in self[source]:
                if self.is_directed() or source < target:
                    yield Edge(source, target, self[source][target])

    def show(self):
        """The graph presentation."""
        for source in self.iternodes():
            print source, ":",
            for edge in self.iteroutedges(source):
                print "%s(%s)" % (edge.target, edge.weight),
            print

    def copy(self):
        """Return the graph copy."""
        new_graph = Graph(n=self.n, directed=self.directed)
        for node in self.iternodes():
            new_graph[node] = dict(self[node])
        return new_graph

    def transpose(self):
        """Return the transpose of the graph."""
        new_graph = Graph(n=self.n, directed=self.directed)
        for node in self.iternodes():
            new_graph.add_node(node)
        for edge in self.iteredges():
            new_graph.add_edge(~edge)
        return new_graph

    def degree(self, node):
        """Return the degree of the node in the undirected graph."""
        if self.is_directed():
            raise ValueError("the graph is directed")
        return len(self[node])

    def outdegree(self, node):
        """Return the outdegree of the node."""
        return len(self[node])

    def indegree(self, node):
        """Return the indegree of the node."""
        if self.is_directed():   # O(V) time
            counter = 0
            for sources_dict in self.itervalues():
                if node in sources_dict:
                    counter = counter + 1
            return counter
        else:                   # O(1) time
            return len(self[node])

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
        if self.is_directed() is not other.is_directed():
            raise ValueError("directed vs undirected")
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
