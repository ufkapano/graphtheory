#!/usr/bin/env python3

try:
    from Queue import PriorityQueue
except ImportError:   # Python 3
    from queue import PriorityQueue

from graphtheory.structures.edges import Edge
from graphtheory.flow.fordfulkerson import FordFulkersonSparse
# no recursion
from graphtheory.bipartiteness.bipartite import BipartiteGraphBFS as Bipartite
# with recursion
#from graphtheory.bipartiteness.bipartite import BipartiteGraphDFS as Bipartite


class MatchingFordFulkersonSet:
    """Maximum-cardinality matching using the Ford-Fulkerson method.
    
    Attributes
    ----------
    graph : input bipartite graph
    mate : dict with nodes (values are nodes or None)
    cardinality : number
    v1 : first set of nodes
    v2 : second set of nodes
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
        self.mate = dict((node, None) for node in self.graph.iternodes())
        self.cardinality = 0
        algorithm = Bipartite(self.graph)
        algorithm.run()
        self.v1 = set()
        self.v2 = set()
        for node in self.graph.iternodes():   # O(V) time
            if algorithm.color[node] == 1:
                self.v1.add(node)
            else:
                self.v2.add(node)

    def run(self):
        """Executable pseudocode."""
        size = self.graph.v()
        # Create flow network.
        network = self.graph.__class__(size + 2, directed=True)
        self.source = size
        self.sink = size + 1
        network.add_node(self.source)
        network.add_node(self.sink)
        for node in self.graph.iternodes():   # O(V) time
            network.add_node(node)
        for node in self.v1:   # edges from source to V1
            network.add_edge(Edge(self.source, node))
        for edge in self.graph.iteredges():   # edges from V1 to V2
            if edge.source in self.v1:   # weights are 1
                network.add_edge(Edge(edge.source, edge.target))
            else:
                network.add_edge(Edge(edge.target, edge.source))
        for node in self.v2:   # edges from V2 to sink
            network.add_edge(Edge(node, self.sink))
        algorithm = FordFulkersonSparse(network)
        algorithm.run(self.source, self.sink)   # O(V*E) time
        for source in self.v1:
            for target in self.v2:
                if algorithm.flow[source].get(target, 0) == 1:
                    self.mate[source] = target
                    self.mate[target] = source
        self.cardinality = algorithm.max_flow


class MatchingFordFulkersonList:
    """Maximum-cardinality matching using the Ford-Fulkerson method.
    
    Attributes
    ----------
    graph : input bipartite graph
    mate : dict with nodes (values are nodes or None)
    cardinality : number
    v1 : first set of nodes
    v2 : second set of nodes
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
        self.mate = dict((node, None) for node in self.graph.iternodes())
        self.cardinality = 0
        algorithm = Bipartite(self.graph)
        algorithm.run()
        self.v1 = list()
        self.v2 = list()
        for node in self.graph.iternodes():   # O(V) time
            if algorithm.color[node] == 1:
                self.v1.append(node)
            else:
                self.v2.append(node)

    def run(self):
        """Executable pseudocode."""
        size = self.graph.v()
        # Create flow network.
        network = self.graph.__class__(size + 2, directed=True)
        self.source = size
        self.sink = size + 1
        network.add_node(self.source)
        network.add_node(self.sink)
        for node in self.graph.iternodes():   # O(V) time
            network.add_node(node)
        for node in self.v1:   # edges from source to V1
            network.add_edge(Edge(self.source, node))
        for edge in self.graph.iteredges():   # edges from V1 to V2
            if edge.source in self.v1:   # weights are 1
                network.add_edge(Edge(edge.source, edge.target))
            else:
                network.add_edge(Edge(edge.target, edge.source))
        for node in self.v2:   # edges from V2 to sink
            network.add_edge(Edge(node, self.sink))
        algorithm = FordFulkersonSparse(network)
        algorithm.run(self.source, self.sink)   # O(V*E) time
        for source in self.v1:
            for target in self.v2:
                if algorithm.flow[source].get(target, 0) == 1:
                    self.mate[source] = target
                    self.mate[target] = source
        self.cardinality = algorithm.max_flow


class MatchingFordFulkersonColor:
    """Maximum-cardinality matching using the Ford-Fulkerson method.
    
    Attributes
    ----------
    graph : input bipartite graph
    mate : dict with nodes (values are nodes or None)
    cardinality : number
    color : dict with nodes (values are colors)
    """
    # Sets are not used.

    def __init__(self, graph):
        """The algorithm initialization.
        
        Parameters
        ----------
        graph : undirected graph
        """
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.mate = dict((node, None) for node in self.graph.iternodes())
        self.cardinality = 0
        algorithm = Bipartite(self.graph)
        algorithm.run()
        self.color = algorithm.color

    def run(self):
        """Executable pseudocode."""
        size = self.graph.v()
        # Create flow network.
        network = self.graph.__class__(size + 2, directed=True)
        self.source = size
        self.sink = size + 1
        network.add_node(self.source)
        network.add_node(self.sink)
        for node in self.graph.iternodes():   # O(V) time
            network.add_node(node)
            if self.color[node] == 1:   # edges from source to V1
                network.add_edge(Edge(self.source, node))
            else:   # edges from V2 to sink
                network.add_edge(Edge(node, self.sink))
        for edge in self.graph.iteredges():   # edges from V1 to V2
            if self.color[edge.source] == 1:   # weights are 1
                network.add_edge(Edge(edge.source, edge.target))
            else:
                network.add_edge(Edge(edge.target, edge.source))
        algorithm = FordFulkersonSparse(network)
        algorithm.run(self.source, self.sink)   # O(V*E) time
        for source in self.graph.iternodes():   # O(V^2) time
            for target in self.graph.iternodes():
                if (self.color[source] == 1 and self.color[target] != 1
                    and algorithm.flow[source].get(target, 0) == 1):
                        self.mate[source] = target
                        self.mate[target] = source
        self.cardinality = algorithm.max_flow

# EOF
