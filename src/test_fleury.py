#!/usr/bin/python
#
# test_fleury.py
#
# Fleury's algorithm test.

from edges import Edge
from graphs import Graph
from fleury import FleuryDFS, FleuryBFS
import unittest

# A --- B     C
# |     |   / |
# |     |  /  |
# |     | /   |
# D --- E --- F

class TestFleuryUndirectedGraph(unittest.TestCase):

    def setUp(self):
        self.N = 6           # number of nodes
        self.G = Graph(self.N, directed=False)
        self.nodes = ["A", "B", "C", "D", "E", "F"]
        self.edges = [Edge("A", "B"), Edge("A", "D"), Edge("B", "E"),
        Edge("D", "E"), Edge("E", "C"), Edge("E", "F"), Edge("C", "F")]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_fleury_dfs(self):
        algorithm = FleuryDFS(self.G)
        algorithm.run()
        #print "dfs", algorithm.euler_cycle
        self.assertEqual(len(algorithm.euler_cycle), len(self.edges)+1)

    def test_fleury_bfs(self):
        algorithm = FleuryBFS(self.G)
        algorithm.run()
        #print "bfs", algorithm.euler_cycle
        self.assertEqual(len(algorithm.euler_cycle), len(self.edges)+1)

    def test_eulerian(self):
        self.G.add_edge(Edge("B", "C"))
        self.assertRaises(ValueError, FleuryDFS, self.G)
        self.assertRaises(ValueError, FleuryBFS, self.G)

    def tearDown(self): pass

# A --> B     C
# ^     |   / ^
# |     |  /  |
# |    .|./   |
# D <-- E --> F

class TestFleuryDirectedGraph(unittest.TestCase):

    def setUp(self):
        self.N = 6           # number of nodes
        self.G = Graph(self.N, directed=False)
        self.nodes = ["A", "B", "C", "D", "E", "F"]
        self.edges = [Edge("A", "B"), Edge("D", "A"), Edge("B", "E"),
        Edge("E", "D"), Edge("C", "E"), Edge("E", "F"), Edge("C", "F")]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_fleury_dfs(self):
        algorithm = FleuryDFS(self.G)
        algorithm.run()
        #print "dfs", algorithm.euler_cycle
        self.assertEqual(len(algorithm.euler_cycle), len(self.edges)+1)

    def test_fleury_bfs(self):
        algorithm = FleuryBFS(self.G)
        algorithm.run()
        #print "bfs", algorithm.euler_cycle
        self.assertEqual(len(algorithm.euler_cycle), len(self.edges)+1)

    def test_eulerian(self):
        self.G.add_edge(Edge("B", "C"))
        self.assertRaises(ValueError, FleuryDFS, self.G)
        self.assertRaises(ValueError, FleuryBFS, self.G)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
