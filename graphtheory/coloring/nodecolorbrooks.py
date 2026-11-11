#!/usr/bin/env python3

try:
    range = xrange   # range będzie zawsze generatorem
except NameError:   # Py3
    pass

import itertools
import collections
from graphtheory.structures.edges import Edge
from graphtheory.connectivity.connected import is_connected


class BrooksNodeColoring:
    """Find a node coloring based on Brooks' theorem in O(n^2) time.
    The implementation finds Delta-coloring in two cases:
    (1) for connected graphs which are not Delta-regular,
    (2) for Delta-regular 3-connected graphs.
    
    Attributes
    ----------
    graph : input undirected graph or multigraph
    color : dict with nodes (values are colors)
    order : list of nodes (order of coloring)
    parent : dict (BFS tree)
    
    Notes
    -----
    Colors are 0, 1, 2, ...
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        if not is_connected(graph):
            raise ValueError("the graph is not connected")
        self.graph = graph
        self.color = dict((node, None) for node in self.graph.iternodes())
        self.order = list()
        self.parent = dict()
        self.m = 0   # graph.e() is slow
        for edge in self.graph.iteredges():   # O(m) time
            self.m += 1
            if edge.source == edge.target:
                raise ValueError("a loop detected")
        if 2 * self.m == self.graph.v() * (self.graph.v() - 1):
            raise ValueError("complete graph detected")
        self._color_list = [False] * self.graph.v()

    def run(self):
        """Executable pseudocode."""
        Delta = max(self.graph.degree(node) for node in self.graph.iternodes())
        if Delta < 3:
            raise ValueError("trivial case with Delta less then three")
        source = min(self.graph.iternodes(), key=self.graph.degree) # O(n) time
        if self.graph.degree(source) < Delta:
            # Wystarczy zrobic BFS zaczynajac od source.
            # Tutaj wystarczy, gdy graf jest spojny.
            # Ustalam kolejnosc kolorowania wierzcholkow za pomoca BFS.
            self._visit(source)   # BFS in O(n+m) time
        else:
            # Delta-regular graph.
            # Zakladam, ze graf jest 3-connected. Chodzi o to, aby 
            # po usunieciu neighbor1 i neighbor2 graf dalej byl spojny.
            # Wybieram wierzcholek o najwiekszym stopniu, O(n) time.
            #source = max(self.graph.iternodes(), key=self.graph.degree)
            #source = self.graph.iternodes().next()
            for nodes in itertools.combinations(
                self.graph.iteradjacent(source), 2):   # O(Delta^2) time
                    neighbor1, neighbor2 = nodes
                    if not self.graph.has_edge(Edge(neighbor1, neighbor2)):
                        break
            #print ( "path {} {} {}".format(neighbor1, source, neighbor2) )
            # Mark two neighbors of source as visited.
            self.parent[neighbor1] = source
            self.parent[neighbor2] = source
            self._visit(source)   # modified BFS in O(n+m) time
            self.order.append(neighbor1)   # second colored, color 0
            self.order.append(neighbor2)   # first colored, color 0
        # Mozemy kolorowac zachlannie wg znalezionej kolejnosci.
        # Sprawdzenie czy wszedzie doszedl BFS.
        assert len(self.order) == self.graph.v(), "problems with a Delta-regular graph"
        self.order.reverse()   # kolejnosc odwrotna! O(n) time
        for source in self.order:   # O(n+m) time
            self._greedy_color(source)

    def _visit(self, node):
        """Explore the connected component with BFS."""
        Q = collections.deque()
        self.parent[node] = None   # before Q.append
        Q.append(node)
        self.order.append(node)   # pre_action
        while len(Q) > 0:
            source = Q.popleft()
            for target in self.graph.iteradjacent(source):
                if target not in self.parent:
                    self.parent[target] = source   # before Q.append
                    Q.append(target)
                    self.order.append(target)   # pre_action

    def _greedy_color(self, source):
        """Give node the smallest possible color."""
        for target in self.graph.iteradjacent(source):
            if self.color[target] is not None:
                self._color_list[self.color[target]] = True
        for c in range(self.graph.v()):   # check colors
            if not self._color_list[c]:
                self.color[source] = c
                break
        for target in self.graph.iteradjacent(source):
            if self.color[target] is not None:
                self._color_list[self.color[target]] = False
        return c

# EOF
