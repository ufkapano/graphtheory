#!/usr/bin/python

from graphtheory.spanningtrees.prim import PrimMatrixMSTWithEdges
from graphtheory.traversing.dfs import SimpleDFS


class PrimTSPWithEdges:
    """The minimum spanning tree algorithm for Metric TSP.
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.hamiltonian_cycle = list()

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:
            source = self.graph.iternodes().next()
        self.source = source
        algorithm = PrimMatrixMSTWithEdges(self.graph)   # O(V**2) time
        algorithm.run(self.source)
        self.mst = algorithm.to_tree()
        #self.mst.show()
        # Obchodzenie MST w kolejnosci preorder z uzyciem DFS.
        # Cykl Hamiltona jako lista wierzcholkow.
        order = list()
        algorithm = SimpleDFS(self.mst)   # O(V) time
        algorithm.run(self.source, pre_action=lambda node: order.append(node))
        order.append(self.source)   # zamykam cykl, teraz dlugosc V+1
        # Szukam krawedzi realizujacych cykl Hamiltona, O(V**2) time.
        for i in xrange(self.graph.v()):
            source = order[i]
            target = order[i+1]
            for edge in self.graph.iteroutedges(source):
                if edge.target == target:
                    self.hamiltonian_cycle.append(edge)
                    break


class PrimTSPWithGraph:
    """The minimum spanning tree algorithm for Metric TSP.
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.hamiltonian_cycle = self.graph.__class__(self.graph.v())
        for node in self.graph.iternodes():
            self.hamiltonian_cycle.add_node(node)

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:
            source = self.graph.iternodes().next()
        self.source = source
        algorithm = PrimMatrixMSTWithEdges(self.graph)   # O(V**2) time
        algorithm.run(self.source)
        self.mst = algorithm.to_tree()
        #self.mst.show()
        # Obchodzenie MST w kolejnosci preorder z uzyciem DFS.
        # Cykl Hamiltona jako lista wierzcholkow.
        order = list()
        algorithm = SimpleDFS(self.mst)   # O(V) time
        algorithm.run(self.source, pre_action=lambda node: order.append(node))
        order.append(self.source)   # zamykam cykl, teraz dlugosc V+1
        # Szukam krawedzi realizujacych cykl Hamiltona, O(V**2) time.
        for i in xrange(self.graph.v()):
            source = order[i]
            target = order[i+1]
            for edge in self.graph.iteroutedges(source):
                if edge.target == target:
                    self.hamiltonian_cycle.add_edge(edge)
                    break

# EOF
