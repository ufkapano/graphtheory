#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.eulerian.euler import EulerianCycleDFS
from graphtheory.eulerian.euler import EulerianCycleDFSWithEdges

# 0 --- 1     2
# |     |   / |
# |     |  /  |
# |     | /   |
# 3 --- 4 --- 5

class TestEulerianCycleUndirected(unittest.TestCase):

    def setUp(self):
        self.N = 6           # number of nodes
        self.G = Graph(self.N, directed=False)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 1), Edge(0, 3), Edge(1, 4), Edge(3, 4), Edge(4, 2), 
            Edge(4, 5), Edge(2, 5)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_euler_dfs(self):
        algorithm = EulerianCycleDFS(self.G)
        algorithm.run(0)
        expected_cycle = [0, 1, 4, 2, 5, 4, 3, 0]
        self.assertEqual(len(algorithm.eulerian_cycle), len(self.edges) + 1)
        self.assertEqual(algorithm.eulerian_cycle, expected_cycle)

    def test_euler_dfs_with_edges(self):
        algorithm = EulerianCycleDFSWithEdges(self.G)
        algorithm.run(0)
        #expected_cycle = [0, 1, 4, 2, 5, 4, 3, 0]
        expected_cycle = [
            Edge(0, 1), Edge(1, 4), Edge(4, 2), Edge(2, 5), Edge(5, 4), 
            Edge(4, 3), Edge(3, 0)]
        self.assertEqual(len(algorithm.eulerian_cycle), len(self.edges))
        self.assertEqual(algorithm.eulerian_cycle, expected_cycle)

    def test_eulerian(self):
        self.G.add_edge(Edge(1, 2))
        self.assertRaises(ValueError, EulerianCycleDFS, self.G)
        self.assertRaises(ValueError, EulerianCycleDFSWithEdges, self.G)

    def tearDown(self): pass

# 0 --- 1     2 --- 3
#   \   |     |   /
#    \  |     |  /
#     \ |     | /
#       4 --- 5
#       |   /
#       |  /
#       | /
#       6

class TestEulerianCycleUndirected2(unittest.TestCase):

    def setUp(self):
        self.N = 7           # number of nodes
        self.G = Graph(self.N, directed=False)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 1), Edge(0, 4), Edge(1, 4), Edge(2, 3), Edge(2, 5), 
            Edge(3, 5), Edge(4, 5), Edge(4, 6), Edge(5, 6)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_euler_dfs(self):
        algorithm = EulerianCycleDFS(self.G)
        algorithm.run(6)
        expected_cycle = [6, 4, 0, 1, 4, 5, 2, 3, 5, 6]
        self.assertEqual(len(algorithm.eulerian_cycle), len(self.edges) + 1)
        self.assertEqual(algorithm.eulerian_cycle, expected_cycle)

    def test_euler_dfs_with_edges(self):
        algorithm = EulerianCycleDFSWithEdges(self.G)
        algorithm.run(6)
        #expected_cycle = [6, 4, 0, 1, 4, 5, 2, 3, 5, 6]
        expected_cycle = [
            Edge(6, 4), Edge(4, 0), Edge(0, 1), Edge(1, 4),
            Edge(4, 5), Edge(5, 2), Edge(2, 3), Edge(3, 5), Edge(5, 6)]
        self.assertEqual(len(algorithm.eulerian_cycle), len(self.edges))
        self.assertEqual(algorithm.eulerian_cycle, expected_cycle)

    def test_eulerian(self):
        self.G.add_edge(Edge(1, 2))
        self.assertRaises(ValueError, EulerianCycleDFS, self.G)
        self.assertRaises(ValueError, EulerianCycleDFSWithEdges, self.G)

    def tearDown(self): pass

# 0 --o 1     2
# o     |   / o
# |     |  /  |
# |     o o   |
# 3 o-- 4 --o 5

class TestEulerianCycleDirected(unittest.TestCase):

    def setUp(self):
        self.N = 6           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 1), Edge(3, 0), Edge(1, 4), Edge(4, 3), Edge(2, 4), 
            Edge(4, 5), Edge(5, 2)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_euler_dfs(self):
        algorithm = EulerianCycleDFS(self.G)
        algorithm.run(0)
        expected_cycle = [0, 1, 4, 5, 2, 4, 3, 0]
        self.assertEqual(len(algorithm.eulerian_cycle), len(self.edges) + 1)
        self.assertEqual(algorithm.eulerian_cycle, expected_cycle)

    def test_euler_dfs_with_edges(self):
        algorithm = EulerianCycleDFSWithEdges(self.G)
        algorithm.run(0)
        #expected_cycle = [0, 1, 4, 5, 2, 4, 3, 0]
        expected_cycle = [
            Edge(0, 1), Edge(1, 4), Edge(4, 5), Edge(5, 2), Edge(2, 4), 
            Edge(4, 3), Edge(3, 0)]
        self.assertEqual(len(algorithm.eulerian_cycle), len(self.edges))
        self.assertEqual(algorithm.eulerian_cycle, expected_cycle)

    def test_eulerian(self):
        self.G.add_edge(Edge(1, 2))
        self.assertRaises(ValueError, EulerianCycleDFS, self.G)
        self.assertRaises(ValueError, EulerianCycleDFSWithEdges, self.G)

    def tearDown(self): pass

# 0 --o 1     2 --o 3
#   o   |     o   /
#    \  |     |  /
#     \ o     | o
#       4 --o 5
#       o   /
#       |  /
#       | o
#       6

class TestEulerianCycleDirected2(unittest.TestCase):

    def setUp(self):
        self.N = 7           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 1), Edge(4, 0), Edge(1, 4), Edge(2, 3), Edge(5, 2), 
            Edge(3, 5), Edge(4, 5), Edge(6, 4), Edge(5, 6)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_euler_dfs(self):
        algorithm = EulerianCycleDFS(self.G)
        algorithm.run(6)
        expected_cycle = [6, 4, 0, 1, 4, 5, 2, 3, 5, 6]
        self.assertEqual(len(algorithm.eulerian_cycle), len(self.edges) + 1)
        self.assertEqual(algorithm.eulerian_cycle, expected_cycle)

    def test_euler_dfs_with_edges(self):
        algorithm = EulerianCycleDFSWithEdges(self.G)
        algorithm.run(6)
        #expected_cycle = [6, 4, 0, 1, 4, 5, 2, 3, 5, 6]
        expected_cycle = [
            Edge(6, 4), Edge(4, 0), Edge(0, 1), Edge(1, 4), Edge(4, 5), 
            Edge(5, 2), Edge(2, 3), Edge(3, 5), Edge(5, 6)]
        self.assertEqual(len(algorithm.eulerian_cycle), len(self.edges))
        self.assertEqual(algorithm.eulerian_cycle, expected_cycle)

    def test_eulerian(self):
        self.G.add_edge(Edge(1, 2))
        self.assertRaises(ValueError, EulerianCycleDFS, self.G)
        self.assertRaises(ValueError, EulerianCycleDFSWithEdges, self.G)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
