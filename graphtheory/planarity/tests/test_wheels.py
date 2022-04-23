#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory
from graphtheory.planarity.wheels import is_wheel, WheelGraph


class TestWheel(unittest.TestCase):

    def setUp(self):
        self.graph_factory = GraphFactory(Graph)

    def test_k4(self):    # complete graph K4 = W4
        G = self.graph_factory.make_complete(n=4, directed=False)
        self.assertTrue(is_wheel(G))
        algorithm = WheelGraph(G)
        algorithm.run()
        self.assertEqual(algorithm.hub, 0)

    def test_wheel_true(self):
        v = 10
        G = Graph(v, False)
        for node in range(v):
            G.add_node(node)
        hub = 0
        for node in range(1, v):
            G.add_edge(Edge(hub, node))
            G.add_edge(Edge(node, node+1 if node < v-1 else 1))
        self.assertTrue(is_wheel(G))
        algorithm = WheelGraph(G)
        algorithm.run()
        self.assertEqual(algorithm.hub, hub)

    def test_is_wheel(self):
        G = self.graph_factory.make_complete(n=3, directed=False)
        self.assertFalse(is_wheel(G))
        self.assertRaises(ValueError, lambda: WheelGraph(G).run())

    def test_wheel_false(self):
        # 0---+   +---5   windmill graph
        # |\   \ /   /|   https://en.wikipedia.org/wiki/Windmill_graph
        # | 1---3---4 |
        # |/   / \   \|
        # 2---+   +---6
        v = 7
        G = Graph(v, False)
        for node in range(v):
            G.add_node(node)
        edges = [
            Edge(0, 1), Edge(1, 2), Edge(0, 2), Edge(4, 5), 
            Edge(5, 6), Edge(4, 6), Edge(0, 3), Edge(1, 3), 
            Edge(2, 3), Edge(3, 5), Edge(3, 4), Edge(3, 6)]
        for edge in edges:
            G.add_edge(edge)
        self.assertFalse(is_wheel(G))
        self.assertRaises(ValueError, lambda: WheelGraph(G).run())

    def test_wheel_false2(self):
        # 1---2   missing Edge(0, 3) or Edge(1, 3)
        # |\ /|
        # | 0 |
        # |/  |
        # 4---3
        v = 5
        G = Graph(v, False)
        for node in range(v):
            G.add_node(node)
        edges = [
            Edge(0, 1), Edge(0, 2), Edge(0, 4), 
            Edge(1, 2), Edge(2, 3), Edge(3, 4), Edge(1, 4)]
        for edge in edges:
            G.add_edge(edge)
        G.add_edge(Edge(2, 4))   # bad edge
        self.assertFalse(is_wheel(G))
        self.assertRaises(ValueError, lambda: WheelGraph(G).run())

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
