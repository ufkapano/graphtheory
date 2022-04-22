#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.algorithms.topsort import TopologicalSortQueue
from graphtheory.algorithms.topsort import TopologicalSortDFS
from graphtheory.algorithms.topsort import TopologicalSortSet
from graphtheory.algorithms.topsort import TopologicalSortList


class TestTopologicalSorting(unittest.TestCase):

    def setUp(self):
        #  Knuth s.273 t.1
        self.N = 10           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = range(self.N)
        self.edges = [
            Edge(9, 2), Edge(3, 7), Edge(7, 5), Edge(5, 8), Edge(8, 6), 
            Edge(4, 6), Edge(1, 3), Edge(7, 4), Edge(9, 5), Edge(2, 8)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_topsort_queue(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = TopologicalSortQueue(self.G)
        algorithm.run()
        idx = dict((node, i) for (i, node) in enumerate(algorithm.sorted_nodes))
        for edge in self.edges:
            self.assertTrue(idx[edge.source] < idx[edge.target])

    def test_topsort_dfs(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = TopologicalSortDFS(self.G)
        algorithm.run()
        idx = dict((node, i) for (i, node) in enumerate(algorithm.sorted_nodes))
        for edge in self.edges:
            self.assertTrue(idx[edge.source] < idx[edge.target])

    def test_topsort_set(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = TopologicalSortSet(self.G)
        algorithm.run()
        idx = dict((node, i) for (i, node) in enumerate(algorithm.sorted_nodes))
        for edge in self.edges:
            self.assertTrue(idx[edge.source] < idx[edge.target])

    def test_topsort_list(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = TopologicalSortList(self.G)
        algorithm.run()
        idx = dict((node, i) for (i, node) in enumerate(algorithm.sorted_nodes))
        for edge in self.edges:
            self.assertTrue(idx[edge.source] < idx[edge.target])

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
