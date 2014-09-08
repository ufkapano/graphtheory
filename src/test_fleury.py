#!/usr/bin/python

from edges import Edge
from graphs import Graph
from fleury import FleuryDFS, FleuryBFS
import unittest

# 0 --- 1     2
# |     |   / |
# |     |  /  |
# |     | /   |
# 3 --- 4 --- 5

class TestFleuryUndirectedGraph(unittest.TestCase):

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
        self.G.add_edge(Edge(1, 2))
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
        self.nodes = [0, 1, 2, 3, 4, 5]
        self.edges = [Edge(0, 1), Edge(3, 0), Edge(1, 4),
        Edge(4, 3), Edge(2, 4), Edge(4, 5), Edge(2, 5)]
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
        self.G.add_edge(Edge(1, 2))
        self.assertRaises(ValueError, FleuryDFS, self.G)
        self.assertRaises(ValueError, FleuryBFS, self.G)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
