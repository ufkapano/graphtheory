#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.seriesparallel.spnodes import Node
from graphtheory.seriesparallel.spcover import SPGraphNodeCover
from graphtheory.seriesparallel.spcover import SPTreeNodeCover

# 0      s=0, t=1
# | \
# 1---2
# | \
# 3   4

class TestNodeCover(unittest.TestCase):

    def setUp(self):
        self.N = 5
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [Edge(0, 1), Edge(0, 2), Edge(1, 2),
            Edge(1, 3), Edge(1, 4)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()
        node1 = Node(0, 1, "edge")
        node2 = Node(0, 2, "edge")
        node3 = Node(2, 1, "edge")
        node4 = Node(1, 3, "edge")
        node5 = Node(1, 4, "edge")
        node6 = Node(0, 1, "series", node2, node3)
        node7 = Node(0, 1, "parallel", node1, node6)
        node8 = Node(0, 1, "jackknife", node7, node4)
        node9 = Node(0, 1, "jackknife", node8, node5)
        self.root = node9

    def test_spgraph_node_cover(self):
        algorithm = SPGraphNodeCover(self.G, self.root)
        algorithm.run()
        expected1 = set([0, 1])
        expected2 = set([1, 2])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.node_cover, expected2)
        # Testing cover.
        for edge in self.G.iteredges():
            self.assertTrue(edge.source in algorithm.node_cover
                         or edge.target in algorithm.node_cover)

    def test_sptree_node_cover(self):
        algorithm = SPTreeNodeCover(self.root)
        algorithm.run()
        expected1 = set([0, 1])
        expected2 = set([1, 2])
        self.assertEqual(algorithm.cardinality, len(expected1))
        self.assertEqual(algorithm.node_cover, expected2)
        # Testing cover.
        for edge in self.G.iteredges():
            self.assertTrue(edge.source in algorithm.node_cover
                         or edge.target in algorithm.node_cover)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
