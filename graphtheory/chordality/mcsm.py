#!/usr/bin/env python3

import collections
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.chordality.peotools import is_peo1

try:
    range = xrange
except NameError:   # Python 3
    pass


class MCS_M:
    """Finding PEO of a chordal completion using MCS-M (minimal triangulation).

    According to the theory, the algorithm runs in O(mn) time.
    Our implementation is slower because modified BFS is used
    to find optimal paths.

    Based on

    A. Berry, J.R.S. Blair, P. Heggernes, B.W. Peyton,
    Maximum cardinality search for computing minimal triangulations of graphs, 
    Algorithmica 39, 287-298 (2004).
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph   # this will be chordal completion
        self.H = self.graph.copy()   # O(V+E) time
        self.new_edges = []   # added edges
        self.order = []   # PEO to find for chordal completion
        self.visited_degree = dict((node, 0)
            for node in self.graph.iternodes())   # O(V) time

    def run(self):
        """Executable pseudocode."""
        for step in range(self.graph.v()):
            source = max(self.H.iternodes(),
                key=self.visited_degree.__getitem__) # O(V) time
            self.order.append(source)
            update = self.visit(source)
            # Update visited degree.
            for target in update:
                self.visited_degree[target] += 1
                edge = Edge(source, target)
                if not self.graph.has_edge(edge):
                    self.new_edges.append(edge)   # nie trzeba dodawac do H
            self.H.del_node(source)
        self.order.reverse()   # O(V) time

        # Creating a chordal completion.
        for edge in self.new_edges:
            self.graph.add_edge(edge)
        # PEO is found.
        assert is_peo1(self.graph, self.order)   # O(V+E) time

    def visit(self, node):
        """Processing a vertex."""
        queue = collections.deque()   # zmienna lokalna w metodzie
        parent = dict()   # zmienna lokalna w metodzie
        parent[node] = None   # before queue.append
        queue.append(node)
        # dict for max weights on the path
        D = dict((target, 0) for target in self.H.iternodes())
        S = set()   # nodes to update

        # First loop. After this S is like in MCS.
        for target in self.H.iteradjacent(node):
            queue.append(target)   # zmienna lokalna w metodzie
            S.add(target)   # wszystkich sasiadow source dodaje do S
            parent[target] = node
            D[target] = self.visited_degree[target]

        while len(queue) > 0:
            source = queue.popleft()
            for target in self.H.iteradjacent(source):
                if target == node:
                    continue
                if target not in parent:   # target was not visited
                    parent[target] = source   # before queue.append
                    queue.append(target)
                    if self.visited_degree[target] > D[source]:
                        S.add(target)
                        D[target] = self.visited_degree[target]
                    else:
                        D[target] = D[source]
                    # UWAGA D[target] nie jest mniejszy od visited_degree[target]
                else:   # target was visited with a different path
                    if self.visited_degree[target] > D[source]: # better path
                        S.add(target)
                        D[target] = self.visited_degree[target]
                        # We want to go further using this path.
                        queue.append(target)
                    elif D[target] > D[source]:
                        D[target] = D[source]   # update
                        queue.append(target)
        return S

# EOF
