#!/usr/bin/python

import random
from edges import Edge


class GraphFactory:
    """The class for graph generators."""

    def __init__(self, graph_class):
        """Get an empty graph (directed or undirected)."""
        self.cls = graph_class

    def make_complete(self, n=1, directed=False):
        """Create the complete graph."""
        graph = self.cls(n, directed)
        weights = range(1, 1 + n * (n-1)/2)   # different weights
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

    def make_cyclic(self, n=1, directed=False):
        """Create the cyclic graph."""
        graph = self.cls(n, directed)
        for node in xrange(n):
            graph.add_node(node)
        for i in xrange(n):
            graph.add_edge(Edge(i, (i+1) % n))
        return graph

    def make_sparse(self, n=1, directed=False, m=0):
        """Create a sparse graph."""
        if m >= n*(n-1)/2:
            raise ValueError("too mamy edges")
        graph = self.cls(n, directed)
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

    def make_tree(self, n=1, directed=False):
        """Create a tree graph."""
        graph = self.cls(n, directed)
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

    def make_connected(self, n=1, directed=False, m=0):
        """Create a connected graph."""
        if m < n - 1 or m >= n * (n - 1)/2:
            raise ValueError("bad number of edges for the connected graph")
        graph = self.cls(n, directed)
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

    def make_random(self, n=1, directed=False, edge_probability=0.5):
        """Create a random graph."""
        graph = self.cls(n, directed)
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

    def make_grid(self, size=3):
        """Create the grid graph with periodic boundary conditions.
        |V| = size * size, |E| = 2 * |V|.
        """
        if size < 3:
            raise ValueError("size too small")
        n = size * size
        graph = self.cls(n, directed=False)
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

    def make_triangle(self, size=3):
        """Create the triangle network with periodic boundary conditions.
        |V| = size * size, |E| = 3 * |V|.
        """
        if size < 3:
            raise ValueError("size too small")
        n = size * size
        graph = self.cls(n, directed=False)
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

    def make_ladder(self, size=3):
        """Create the ladder with periodic boundary conditions.
        |V| = 2 * size, |E| = 3 * size.
        """
        if size < 3:
            raise ValueError("size too small")
        n = 2 * size
        graph = self.cls(n, directed=False)
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

    def make_flow_network(self, n=1):
        """Create a flow network."""
        graph = self.cls(n, True)
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
