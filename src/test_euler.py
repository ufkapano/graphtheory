#!/usr/bin/python

import unittest
from edges import Edge
from graphs import Graph
from euler import EulerianCycleDFS

# 0 --- 1     2
# |     |   / |
# |     |  /  |
# |     | /   |
# 3 --- 4 --- 5

class TestEulerianCycle(unittest.TestCase):

    def setUp(self):
        self.N = 6           # number of nodes
        self.G = Graph(self.N, directed=False)
        self.nodes = [0, 1, 2, 3, 4, 5]
        self.edges = [Edge(0, 1), Edge(0, 3), Edge(1, 4),
            Edge(3, 4), Edge(4, 2), Edge(4, 5), Edge(2, 5)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_euler_dfs(self):
        algorithm = EulerianCycleDFS(self.G)
        algorithm.run(0)
        expected_cycle = [0, 1, 4, 2, 5, 4, 3]
        self.assertEqual(len(algorithm.eulerian_cycle), len(self.edges))
        self.assertEqual(algorithm.eulerian_cycle, expected_cycle)

    def test_eulerian(self):
        self.G.add_edge(Edge(1, 2))
        self.assertRaises(ValueError, EulerianCycleDFS, self.G)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
