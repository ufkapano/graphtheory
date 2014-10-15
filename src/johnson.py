#!/usr/bin/python

from edges import Edge
from bellmanford import BellmanFord
from dijkstra import Dijkstra

class Johnson:
    """The Johnson algorithm for the shortest path problem."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("graph is not directed")
        self.graph = graph

    def run(self):
        """Executable pseudocode."""
        # graph copy
        size = self.graph.v()
        self.new_graph = self.graph.__class__(size + 1, directed=True)
        for node in self.graph.iternodes():   # O(V) time
            self.new_graph.add_node(node)
        for edge in self.graph.iteredges():   # O(E) time
            self.new_graph.add_edge(edge)
        self.new_node = size
        self.new_graph.add_node(self.new_node)
        for node in self.graph.iternodes():   # O(V) time
            self.new_graph.add_edge(Edge(self.new_node, node, 0))
        self.bf = BellmanFord(self.new_graph)
        # If this step detects a negative cycle, the algorithm is terminated.
        self.bf.run(self.new_node)   # O(V*E) time
        # edges are reweighted
        for edge in list(self.new_graph.iteredges()):   # O(E) time
            edge.weight = (edge.weight 
                + self.bf.distance[edge.source] - self.bf.distance[edge.target])
            self.new_graph.del_edge(edge)
            self.new_graph.add_edge(edge)
        # remove new_node with edges
        self.new_graph.del_node(self.new_node)
        # weights are modified!
        self.distance = dict()
        for source in self.graph.iternodes():
            self.distance[source] = dict()
            algorithm = Dijkstra(self.new_graph) # O(V*E*log(V)) total time
            algorithm.run(source)
            for target in self.graph.iternodes():   # O(V**2) total time
                self.distance[source][target] = (algorithm.distance[target]
                - self.bf.distance[source] + self.bf.distance[target])


class JohnsonFaster:
    """The Johnson algorithm for the shortest path problem."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("graph is not directed")
        self.graph = graph
        self.positive_weights = all(edge.weight >= 0
            for edge in self.graph.iteredges())   # O(E) time

    def run(self):
        """Executable pseudocode."""
        if self.positive_weights:
            self.new_graph = self.graph
        else:
            # graph copy
            self.new_graph = self.graph.__class__(self.graph.v()+1, directed=True)
            for node in self.graph.iternodes():   # O(V) time
                self.new_graph.add_node(node)
            for edge in self.graph.iteredges():   # O(E) time
                self.new_graph.add_edge(edge)
            self.new_node = self.graph.v()
            self.new_graph.add_node(self.new_node)
            for node in self.graph.iternodes():   # O(V) time
                self.new_graph.add_edge(Edge(self.new_node, node, 0))
            self.bf = BellmanFord(self.new_graph)
            # If this step detects a negative cycle,
            # the algorithm is terminated.
            self.bf.run(self.new_node)   # O(V*E) time
            # edges are reweighted
            for edge in list(self.new_graph.iteredges()):   # O(E) time
                edge.weight = (edge.weight 
                    + self.bf.distance[edge.source] - self.bf.distance[edge.target])
                self.new_graph.del_edge(edge)
                self.new_graph.add_edge(edge)
            # remove new_node with edges
            self.new_graph.del_node(self.new_node)

        self.distance = dict()
        for source in self.graph.iternodes():
            self.distance[source] = dict()
            algorithm = Dijkstra(self.new_graph) # O(V*E*log(V)) total time
            algorithm.run(source)
            for target in self.graph.iternodes():   # O(V**2) total time
                if self.positive_weights:
                    self.distance[source][target] = algorithm.distance[target]
                else:
                    self.distance[source][target] = (algorithm.distance[target]
                    - self.bf.distance[source] + self.bf.distance[target])

# EOF
