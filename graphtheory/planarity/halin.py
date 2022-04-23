#!/usr/bin/env python3

from graphtheory.structures.edges import Edge


class HalinGraph:
    """Halin graphs detection.
    
    Attributes
    ----------
    graph : input graph
    outer : set of nodes from the outer face
    
    Notes
    -----
    Based on:
    
    https://en.wikipedia.org/wiki/Halin_graph
    
    http://www.ics.uci.edu/~eppstein/PADS/
    """

    def __init__(self, graph):
        """The algorithm initialization.
        
        Parameters
        ----------
        graph : undirected graph
        """
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self._graph_copy = self.graph.copy()
        self.outer = set()
        self.degree3 = set(node for node in self.graph.iternodes()
            if self.graph.degree(node) == 3)   # active nodes with degree 3
        self._calls = []

    def run(self):
        """Executable pseudocode."""
        while self.degree3:
            node = self.degree3.pop()
            if (self._graph_copy.has_node(node) and
                self._graph_copy.v() > 4 and
                self._graph_copy.degree(node) == 3):
                    # Decode set of neighbors.
                    a, b, c = tuple(self._graph_copy.iteradjacent(node))
                    self._reduce(a, node, b)
                    self._reduce(a, node, c)
                    self._reduce(b, node, c)
        if not self.is_outer_k4():
            raise ValueError("not a Halin graph")
        self._reconstruct_cycle()

    def other_neighbor(self, a, b, c):
        """Return a neighbor of b which is not included in the triangle."""
        # Using a dict.
        #neighbors = set(self._graph_copy.iteradjacent(b))
        #neighbors.remove(a)
        #neighbors.remove(c)
        # Using a list.
        neighbors = list(node for node in self._graph_copy.iteradjacent(b)
            if node != a and node != c)
        return neighbors.pop()

    def _reduce(self, a, b, c):
        """Try reduce for node b in the middle."""
        for node in (a, b, c):   # probably this check can be skipped
            if (not self._graph_copy.has_node(node) or 
                self._graph_copy.degree(node) != 3):
                    return
        if self._graph_copy.has_edge(Edge(a, c)):
            self._reduce_triangle(a, b, c)
        else:
            self._reduce_path(a, b, c)

    def _reduce_triangle(self, a, b, c):
        """Collapse nodes from a triangle with distinct neighbors."""
        Na = self.other_neighbor(b, a, c)
        Nb = self.other_neighbor(a, b, c)
        Nc = self.other_neighbor(a, c, b)
        if Na == Nb or Nb == Nc or Na == Nc:
            return   # need to have three distinct neighbors
        # BEGIN HALIN
        if a in self.outer and b in self.outer and c in self.outer:
            return   # can't collapse when all three are outer
        # If node belongs to the outer face, mark its neighbor as outer.
        for node, neighbor in [(a, Na), (b, Nb), (c, Nc)]:
            if node in self.outer:
                self.outer.add(neighbor)
        # Add also the collapsed node to the outer set.
        new_node = "{0}_{1}_{2}".format(a, b, c)
        self.outer.add(new_node)
        self._calls.append(("triangle", a, b, c, Na, Nb, Nc, new_node))
        # END HALIN
        # Make the change!
        self._graph_copy.del_node(a)
        self._graph_copy.del_node(b)
        self._graph_copy.del_node(c)
        self._graph_copy.add_edge(Edge(Na, new_node))
        self._graph_copy.add_edge(Edge(Nb, new_node))
        self._graph_copy.add_edge(Edge(Nc, new_node))
        # Update the active nodes.
        for node in (new_node, Na, Nb, Nc):
            if self._graph_copy.degree(node) == 3:
                self.degree3.add(node)

    def _reduce_path(self, a, b, c):
        """Degree-three vertices from a path with one shared neighbor 
        contracted to a two-vertex path."""
        neighbors = (set(self._graph_copy.iteradjacent(a)) & 
                     set(self._graph_copy.iteradjacent(b)) & 
                     set(self._graph_copy.iteradjacent(c)))
        if len(neighbors) != 1:
            return
        Nb = neighbors.pop()
        # BEGIN HALIN
        if Nb in self.outer:
            return        # as we can't shorten path with outer apex
        # Jezeli pod koniec bedzie kolo W_5, to latwo zaznaczyc ktory
        # wierzcholek nie jest outer.
        # Ale czy grafy kubiczne beda dobrze rozpoznawane?
        if self._graph_copy.v() == 5:
            self.outer.update(node for node in self._graph_copy.iternodes()
                if node != Nb)
        else:
            self.outer.update((a, c))   # mark remaining nodes as outer
        self._calls.append(("path", a, b, c, Nb))
        # END HALIN
        # Make the change!
        self._graph_copy.del_node(b)   # remove b with edges
        self._graph_copy.add_edge(Edge(a, c))
        # Update the active nodes.
        if self._graph_copy.degree(Nb) == 3:
            self.degree3.add(Nb)

    def _reconstruct_cycle(self):
        """Recursively reconstruct the leaf cycle of Halin graph."""
        self._calls.reverse()
        # Augment outer to include all outer vertices.
        # Teraz sprawdzam, czy jakis wierzcholek nie jest zaznaczony
        # jako zewnetrzny i jesli nie to moze byc wewnetrznym.
        # Nie wiem czy tu nie ma za duzo swobody wyboru.
        # Trzeba to przetestowac z duzymi grafami Halina.
        for node in self._graph_copy.iternodes():
            if node not in self.outer:
                for source in self._graph_copy.iternodes():
                    if node != source:
                        self.outer.add(source)
                break
        for items in self._calls:
            name, arguments = items[0], items[1:]
            if name == "triangle":
                self._undo_triangle(*arguments)
            elif name == "path":
                self._undo_path(*arguments)
        # Remove nodes from reduction.
        self.outer = self.outer & set(self.graph.iternodes())

    def _undo_triangle(self, a, b, c, Na, Nb, Nc, x):
        """Undo a triangle reduction."""
        nout = 0
        for node, neighbor in [(a, Na), (b, Nb), (c, Nc)]:
            if neighbor in self.outer:
                self.outer.add(node)
                nout += 1
        if nout != 2:
            raise ValueError("problem with triangle")

    def _undo_path(self, a, b, c, neighbor):
        """Undo a path reduction."""
        if neighbor in self.outer:
            raise ValueError("neighbor in outer")
        self.outer.update((a, b, c))

    def is_k4(self):
        """Check if the graph is K4."""
        if self._graph_copy.v() != 4:
            return False
        return all(self._graph_copy.degree(node) == 3
            for node in self._graph_copy.iternodes())

    def is_outer_k4(self):
        """Have we reduced to a K4 with a non-outer node?"""
        if not self.is_k4():
            return False
        return any(node not in self.outer
            for node in self._graph_copy.iternodes())

# EOF
