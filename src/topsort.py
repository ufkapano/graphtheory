#!/usr/bin/python
#
# topsort.py
#
# Topological sorting of nodes from a dag.

from edges import Edge
from graphs import Graph
from dfs import DFSWithRecursion

class TopologicalSort:

    def __init__(self, graph):
        self.graph = graph
        self.dfs = DFSWithRecursion(graph)
        self.sorted_nodes = []

    def run(self):
        self.dfs.run(post_action=lambda node: self.sorted_nodes.append(node))
        self.sorted_nodes.reverse()

# EOF
