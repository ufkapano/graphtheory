#!/usr/bin/python
#
# johnson.py
#
# The Johnson algorithm.

import copy
from edges import Edge
from bellmanford import BellmanFord
from dijkstra import Dijkstra

class Johnson:
    """The Johnson algorithm for the shortest path problem."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("graph is not directed")
        # graph copy
        self.graph = graph.__class__(graph.v()+1, directed=True)
        self.old_nodes = list(graph.iternodes())
        for node in self.old_nodes:
            self.graph.add_node(node)
        for edge in graph.iteredges():
            self.graph.add_edge(edge)
        self.new_node = graph.v()
        self.graph.add_node(self.new_node)
        for node in self.old_nodes:
            self.graph.add_edge(Edge(self.new_node, node, 0))

    def run(self):
        """Executable pseudocode."""
        self.bf = BellmanFord(self.graph)
        self.bf.run(self.new_node)
        # edges are reweighted
        for edge in list(self.graph.iteredges()):
            edge.weight = (edge.weight 
                + self.bf.dist[edge.source] - self.bf.dist[edge.target])
            self.graph.del_edge(edge)
            self.graph.add_edge(edge)
        # remove new_node with edges
        self.graph.del_node(self.new_node)
        # weights are modified!
        self.dist = dict()
        for source in self.old_nodes:
            self.dist[source] = dict()
            alg = Dijkstra(self.graph)
            alg.run(source)
            for target in self.old_nodes:
                self.dist[source][target] = (alg.dist[target]
                - self.bf.dist[source] + self.bf.dist[target])

# EOF
