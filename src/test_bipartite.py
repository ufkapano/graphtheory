#!/usr/bin/python

from edges import Edge
from graphs import Graph
from bipartite import BipartiteGraphBFS, BipartiteGraphDFS
import unittest

# 0---1---2
# |   |   |
# 3---4---5

class TestBipartiteGraph(unittest.TestCase):

    def setUp(self):
        self.N = 6           # number of nodes
        self.G = Graph(self.N, directed=False)
        self.nodes = [0, 1, 2, 3, 4, 5]
        self.edges = [Edge(0, 1), Edge(1, 2), Edge(0, 3),
        Edge(1, 4), Edge(2, 5), Edge(3, 4), Edge(4, 5)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #print self.G
        #self.G.show()

    def test_bipartite_bfs(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = BipartiteGraphBFS(self.G)
        algorithm.run(0)
        color_expected = {0: 1, 2: 1, 4: 1, 1: -1, 3: -1, 5: -1}
        self.assertEqual(algorithm.color, color_expected)

    def test_bipartite_dfs(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = BipartiteGraphDFS(self.G)
        algorithm.run(0)
        color_expected = {0: 1, 2: 1, 4: 1, 1: -1, 3: -1, 5: -1}
        self.assertEqual(algorithm.color, color_expected)

    def test_exceptions(self):
        self.G.add_edge(Edge(0, 4))
        algorithm = BipartiteGraphBFS(self.G)
        self.assertRaises(ValueError, algorithm.run)
        algorithm = BipartiteGraphDFS(self.G)
        self.assertRaises(ValueError, algorithm.run)
        self.assertRaises(ValueError, BipartiteGraphBFS, Graph(2, directed=True))
        self.assertRaises(ValueError, BipartiteGraphDFS, Graph(2, directed=True))

    def tearDown(self): pass

if __name__ == "__main__":

    #unittest.main()
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestBipartiteGraph)
    suite = unittest.TestSuite([suite1])
    unittest.TextTestRunner(verbosity=2).run(suite)

# EOF
