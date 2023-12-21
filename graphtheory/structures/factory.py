#!/usr/bin/env python3

try:
    integer_types = (int, long)
    range = xrange
except NameError:   # Python 3
    integer_types = (int,)

import random
from graphtheory.structures.edges import Edge


class GraphFactory:
    """The class for graph generators."""

    def __init__(self, graph_class):
        """Get a graph class."""
        self.cls = graph_class

    def make_complete(self, n=1, directed=False):
        """Create a weighted complete graph."""
        graph = self.cls(n, directed)
        weights = list(range(1, 1 + n * (n-1) // 2))   # different weights
        random.shuffle(weights)
        for node in range(n):
            graph.add_node(node)
        for source in range(n):
            for target in range(source + 1, n):   # no loops
                if random.random() > 0.5:   # random direction
                    graph.add_edge(Edge(source, target, weights.pop()))
                else:
                    graph.add_edge(Edge(target, source, weights.pop()))
        return graph

    def make_cyclic(self, n=1, directed=False):
        """Create a weighted cyclic graph."""
        if n < 3:
            raise ValueError("number of nodes must be greater than 2")
        graph = self.cls(n, directed)
        weights = list(range(1, 1 + n))   # different weights
        random.shuffle(weights)
        for node in range(n):
            graph.add_node(node)
        for i in range(n):
            graph.add_edge(Edge(i, (i+1) % n, weights.pop()))
        return graph

    def make_sparse(self, n=1, directed=False, m=0):
        """Create a weighted sparse graph."""
        if m >= n*(n-1) // 2:
            raise ValueError("too mamy edges")
        graph = self.cls(n, directed)
        weights = list(range(1, 1 + m))   # different weights
        random.shuffle(weights)
        for node in range(n):
            graph.add_node(node)
        nodes = list(range(n))
        n_edges = 0
        while n_edges < m:
            source, target = random.sample(nodes, 2)
            if not graph.has_edge(Edge(source, target)):
                graph.add_edge(Edge(source, target, weights.pop()))
                n_edges += 1
        return graph

    def make_tree(self, n=1, directed=False):
        """Create a weighted tree graph."""
        graph = self.cls(n, directed)
        weights = list(range(1, n))   # different weights
        random.shuffle(weights)
        for node in range(n):
            graph.add_node(node)
        nodes = [0]
        for node in range(1, n):
            parent = random.sample(nodes, 1)[0]
            nodes.append(node)
            graph.add_edge(Edge(parent, node, weights.pop()))
        return graph

    def make_connected(self, n=1, directed=False, m=0):
        """Create a weighted connected graph."""
        if m < n - 1 or m >= n * (n - 1) // 2:
            raise ValueError("bad number of edges for the connected graph")
        graph = self.cls(n, directed)
        weights = list(range(1, m + 1))   # different weights
        random.shuffle(weights)
        for node in range(n):
            graph.add_node(node)
        nodes = [0]
        # make a tree
        for node in range(1, n):
            parent = random.sample(nodes, 1)[0]
            nodes.append(node)
            graph.add_edge(Edge(parent, node, weights.pop()))
        # the rest of edges
        n_edges = n - 1
        while n_edges < m:
            source, target = random.sample(nodes, 2)
            if not graph.has_edge(Edge(source, target)):
                graph.add_edge(Edge(source, target, weights.pop()))
                n_edges += 1
        return graph

    def make_random(self, n=1, directed=False, edge_probability=0.5):
        """Create a weighted random graph."""
        graph = self.cls(n, directed)
        weights = list(range(1, 1 + n * (n-1) // 2))   # different weights
        random.shuffle(weights)
        for node in range(n):
            graph.add_node(node)
        for source in range(n):
            for target in range(source + 1, n):   # no loops
                if random.random() > edge_probability:
                    continue
                if random.random() > 0.5:   # random direction
                    graph.add_edge(Edge(source, target, weights.pop()))
                else:
                    graph.add_edge(Edge(target, source, weights.pop()))
        return graph

    def make_bipartite(self, n1=1, n2=1, directed=False, edge_probability=0.5):
        """Create a weighted random bipartite graph."""
        graph = self.cls(n1 + n2, directed)
        weights = list(range(1, n1 * n2 + 1))   # different weights
        random.shuffle(weights)
        for node in range(n1 + n2):
            graph.add_node(node)
        for source in range(n1):
            for target in range(n1, n1 + n2):   # no loops
                if random.random() > edge_probability:
                    continue
                if random.random() > 0.5:   # random direction
                    graph.add_edge(Edge(source, target, weights.pop()))
                else:
                    graph.add_edge(Edge(target, source, weights.pop()))
        return graph

# |     |     |            |
# 2s--(2s+1)-(2s+2)-...--(3s-1)
# |     |     |            |
# s---(s+1)-(s+2)---...--(2s-1)
# |     |     |            |
# 0-----1-----2-----...--(s-1)

    def make_grid(self, size=3):
        """Create a weighted grid graph with boundary
            |V|= size * size, |E| = 2 * size * (size-1).
        """
        if size < 3:
            raise ValueError("size too small")
        n = size * size
        graph = self.cls(n, directed=False)
        weights = list(range(1, 1 + 2 * size * (size-1)))   # different weights
        random.shuffle(weights)
        for node in range(n):
            graph.add_node(node)
        for node in range(n):
            row = node // size
            col = node % size
            if col != size-1:
                graph.add_edge(Edge(node, node + 1, weights.pop()))  # line ---
            if row != size-1:
                graph.add_edge(Edge(node, node + size, weights.pop()))  # line |
        return graph

#   |     |     |
# --2s--(2s+1)-(2s+2)--
#   |     |     |
# --s---(s+1)-(s+2)--
#   |     |     |
# --0-----1-----2---
#   |     |     |

    def make_grid_periodic(self, size=3):
        """Create a weighted grid graph with periodic boundary conditions.
        |V| = size * size, |E| = 2 * |V|.
        """
        if size < 3:
            raise ValueError("size too small")
        n = size * size
        graph = self.cls(n, directed=False)
        weights = list(range(1, 1 + 2 * n))   # different weights
        random.shuffle(weights)
        for node in range(n):
            graph.add_node(node)
        for node in range(n):
            row = node // size
            col = node % size
            graph.add_edge(Edge(node, row * size + (col + 1) % size, weights.pop())) # line ---
            graph.add_edge(Edge(node, ((row + 1) % size) * size + col, weights.pop())) # line |
        return graph

# |  /  |  /  |  /     /  |
# 2s--(2s+1)-(2s+2)-...-(3s-1)
# |  /  |  /  |  /     /  |
# s---(s+1)-(s+2)--...--(2s-1)
# |  /  |  /  |  /     /  |
# 0-----1-----2---...---(s-1)

    def make_triangle(self, size=3):
        """Create a weighted triangle graph with boundary,
        |V| = size * size, |E| = 2 * size * (size-1) + (size-1) * (size-1).
        """
        if size < 3:
            raise ValueError("size too small")
        n = size * size
        graph = self.cls(n, directed=False)
        weights = list(range(1, 1 + 3*size*size -4*size + 1))   # different weights
        random.shuffle(weights)
        for node in range(n):
            graph.add_node(node)
        for node in range(n):
            row = node // size
            col = node % size
            if col != size-1:
                graph.add_edge(Edge(node, node + 1, weights.pop()))  # line ---
            if row != size-1:
                graph.add_edge(Edge(node, node + size, weights.pop()))  # line |
            if col != size-1 and row != size-1:
                graph.add_edge(Edge(node, node + 1 + size, weights.pop())) # line /
        return graph

#   |  /  |  /  | /
# --2s--(2s+1)-(2s+2)--
# / |  /  |  /  | /
# --s---(s+1)-(s+2)--
# / |  /  |  /  | /
# --0-----1-----2---
# / |  /  |  /  |

    def make_triangle_periodic(self, size=3):
        """Create a weighted triangle network with periodic boundary 
        conditions. |V| = size * size, |E| = 3 * |V|.
        """
        if size < 3:
            raise ValueError("size too small")
        n = size * size
        graph = self.cls(n, directed=False)
        weights = list(range(1, 1 + 3 * n))   # different weights
        random.shuffle(weights)
        for node in range(n):
            graph.add_node(node)
        for node in range(n):
            row = node // size
            col = node % size
            graph.add_edge(Edge(node, row * size + (col + 1) % size, weights.pop())) # line ---
            graph.add_edge(Edge(node, ((row + 1) % size) * size + col, weights.pop())) # line |
            graph.add_edge(Edge(node, ((row + 1) % size) * size + (col + 1) % size, weights.pop())) # line /
        return graph

# 1--3--5--...--(2s-1)
# |  |  |         |
# 0--2--4--...--(2s-2)

    def make_ladder(self, size=3):
        """Create a weighted ladder with boundary.
        |V| = 2 * size, |E| = 3*size - 2.
        """
        if size < 3:
            raise ValueError("size too small")
        n = 2 * size
        graph = self.cls(n, directed=False)
        weights = list(range(1, 1 + 3 * size - 2))   # different weights
        random.shuffle(weights)
        for node in range(n):
            graph.add_node(node)
        for i in range(size):
            node = 2 * i
            graph.add_edge(Edge(node, node + 1, weights.pop())) # line |
            if i != size-1:
                graph.add_edge(Edge(node, (node + 2) % n, weights.pop())) # line ---
                graph.add_edge(Edge(node + 1, (node + 3) % n, weights.pop())) # line ---
        return graph

# --1--3--5--...--(2s-1)-
#   |  |  |         |
# --0--2--4--...--(2s-2)---

    def make_prism(self, size=3):
        """Create a weighted prism graph or a circular ladder graph.
        |V| = 2 * size, |E| = 3 * size.
        
         Weisstein, Eric W. "Prism Graph." From MathWorld--A Wolfram Web Resource. 
         http://mathworld.wolfram.com/PrismGraph.html 
        """
        if size < 3:
            raise ValueError("size too small")
        n = 2 * size
        graph = self.cls(n, directed=False)
        weights = list(range(1, 1 + 3 * size))   # different weights
        random.shuffle(weights)
        for node in range(n):
            graph.add_node(node)
        for i in range(size):
            node = 2 * i
            graph.add_edge(Edge(node, node + 1, weights.pop())) # line |
            graph.add_edge(Edge(node, (node + 2) % n, weights.pop())) # line ---
            graph.add_edge(Edge(node + 1, (node + 3) % n, weights.pop())) # line ---
        return graph

    make_ladder_periodic = make_prism

    def make_antiprism(self, size=3):
        """Create a weighted antiprism graph, |V| = 2 * size, |E| = 4 * size.
        
        Weisstein, Eric W. "Antiprism Graph." From MathWorld--A Wolfram Web Resource. 
        http://mathworld.wolfram.com/AntiprismGraph.html 
        """
        if size < 3:
            raise ValueError("size too small")
        n = 2 * size
        graph = self.cls(n, directed=False)
        weights = list(range(1, 1 + 4 * size))   # different weights
        random.shuffle(weights)
        for node in range(n):
            graph.add_node(node)
        for node in range(n):
            graph.add_edge(Edge(node, (node + 1) % n, weights.pop())) # line /
            graph.add_edge(Edge(node, (node + 2) % n, weights.pop())) # line ---
        return graph

    def make_flow_network(self, n=1):
        """Create a flow network."""
        graph = self.cls(n, True)
        for node in range(n):
            graph.add_node(node)
        node_list = list(range(1, n))
        source = 0
        sink = n - 1
        used = dict((node, False) for node in range(n))
        used[source] = True
        # create paths from source to sink
        while any(used[node] == False for node in used):
            random.shuffle(node_list)
            start = source
            for target in node_list:
                edge = Edge(start, target, random.randint(1, n))
                if not (graph.has_edge(edge) or graph.has_edge(~edge)):
                    graph.add_edge(edge)
                    used[target] = True
                if target == sink:
                    break
                else:
                    start = target
        # all nodes are on paths; new edges can be added
        return graph

# 0-----------------(n-1)       n is even
# |\                / |  outer nodes set(range(0,n,2)) | set([n-1])
# | 1--3--5-...-(n-3) |
# |/   |  |         \ |
# 2----4--6-...----(n-2)

    def make_necklace(self, n=4, directed=False):
        """Create a weighted necklace graph, |V| = 2*k, |E| = 3*k.
        The set of outer nodes is set(range(0,n,2)) | set([n-1]).
        """
        if n < 4:
            raise ValueError("number of nodes must be greater than 3")
        if n % 2:
            raise ValueError("number of nodes must be even")
        # It is a cubic graph.
        graph = self.cls(n, directed)
        k = n // 2
        weights = list(range(1, 1 + 3 * k))
        random.shuffle(weights)
        for node in range(n):
            graph.add_node(node)
        graph.add_edge(Edge(0, 1, weights.pop()))
        graph.add_edge(Edge(0, 2, weights.pop()))
        graph.add_edge(Edge(0, n-1, weights.pop()))
        graph.add_edge(Edge(n-2, n-1, weights.pop()))
        graph.add_edge(Edge(n-3, n-1, weights.pop()))
        for i in range(1, n-3):
            graph.add_edge(Edge(i, i+2, weights.pop())) # ---
        for i in range(1, n-1, 2):
            graph.add_edge(Edge(i, i+1, weights.pop())) # |
        return graph

    def make_wheel(self, n=4, directed=False):
        """Create a weighted wheel graph. The hub is equal to 0."""
        if n < 4:
            raise ValueError("number of nodes must be greater than 3")
        graph = self.cls(n, directed)
        weights = list(range(1, 1 + 2 * n - 2))
        random.shuffle(weights)
        for node in range(n):
            graph.add_node(node)
        hub = 0
        for i in range(1, n):
            graph.add_edge(Edge(hub, i, weights.pop()))
            graph.add_edge(Edge(i, i+1 if (i < n-1) else 1, weights.pop()))
        return graph

    def make_fake_wheel(self, n=7, directed=False):
        """Create a weighted fake wheel graph."""
        # Similar to a windmill graph,
        # http://mathworld.wolfram.com/WindmillGraph.html
        if n < 7:
            raise ValueError("number of nodes must be greater than 6")
        graph = self.make_wheel(n, directed)
        # Remowe Edge(3, 4, weight1) and Edge(1, n-1, weight2).
        # Add Edge(3, 1, weight1) and Edge(4, n-1, weight2).
        # Old weights are reused.
        for edge in graph.iteroutedges(3):
            if edge.target == 4:
                edge1 = edge
                break
        for edge in graph.iteroutedges(n-1):
            if edge.target == 1:
                edge2 = edge
                break
        graph.del_edge(edge1)
        graph.del_edge(edge2)
        graph.add_edge(Edge(3, 1, edge1.weight))
        graph.add_edge(Edge(n-1, 4, edge2.weight))
        #graph.show()
        return graph

# EOF
