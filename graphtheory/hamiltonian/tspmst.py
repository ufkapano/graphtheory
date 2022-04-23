#!/usr/bin/env python3

try:
    integer_types = (int, long)
    range = xrange
except NameError:   # Python 3
    integer_types = (int,)

from graphtheory.spanningtrees.prim import PrimMatrixMSTWithEdges
from graphtheory.traversing.dfs import SimpleDFS


class PrimTSPWithEdges:
    """The minimum spanning tree algorithm for Metric TSP.
    
    Attributes
    ----------
    graph : input weighted complete graph
    hamiltonian_cycle : list of edges
    source : starting node
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.hamiltonian_cycle = list()
        self.source = None

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:
            source = next(self.graph.iternodes())
        self.source = source
        algorithm = PrimMatrixMSTWithEdges(self.graph)   # O(V**2) time
        algorithm.run(self.source)
        self.mst = algorithm.to_tree()
        # Obchodzenie MST w kolejnosci preorder z uzyciem DFS.
        # Hamiltonian cycle as a list of nodes.
        order = list()
        algorithm = SimpleDFS(self.mst)   # O(V) time
        algorithm.run(self.source, pre_action=lambda node: order.append(node))
        order.append(self.source)   # close cycle, length V+1
        # Finding edges for the Hamiltonian cycle, O(V**2) time.
        for i in range(self.graph.v()):
            source = order[i]
            target = order[i+1]
            for edge in self.graph.iteroutedges(source):
                if edge.target == target:
                    self.hamiltonian_cycle.append(edge)
                    break


class PrimTSPWithGraph:
    """The minimum spanning tree algorithm for Metric TSP.
    
    Attributes
    ----------
    graph : input weighted complete graph
    hamiltonian_cycle : cycle graph
    source : starting node
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.hamiltonian_cycle = self.graph.__class__(self.graph.v())
        for node in self.graph.iternodes():
            self.hamiltonian_cycle.add_node(node)
        self.source = None

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:
            source = next(self.graph.iternodes())
        self.source = source
        algorithm = PrimMatrixMSTWithEdges(self.graph)   # O(V**2) time
        algorithm.run(self.source)
        self.mst = algorithm.to_tree()
        # Obchodzenie MST w kolejnosci preorder z uzyciem DFS.
        # Hamiltonian cycle as a list of nodes.
        order = list()
        algorithm = SimpleDFS(self.mst)   # O(V) time
        algorithm.run(self.source, pre_action=lambda node: order.append(node))
        order.append(self.source)   # close cycle, length V+1
        # Finding edges for the Hamiltonian cycle, O(V**2) time.
        for i in range(self.graph.v()):
            source = order[i]
            target = order[i+1]
            for edge in self.graph.iteroutedges(source):
                if edge.target == target:
                    self.hamiltonian_cycle.add_edge(edge)
                    break

# EOF
