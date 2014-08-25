#!/usr/bin/python

from edges import Edge
from graphs import Graph
from bipartite import BipartiteGraphBFS, BipartiteGraphDFS
import unittest

# A---B---C
# |   |   |
# D---E---F

class TestBipartiteGraph(unittest.TestCase):

    def setUp(self):
        self.N = 6           # number of nodes
        self.G = Graph(self.N, directed=False)
        self.nodes = ["A", "B", "C", "D", "E", "F"]
        self.edges = [Edge("A", "B"), Edge("B", "C"), Edge("A", "D"),
        Edge("B", "E"), Edge("C", "F"), Edge("D", "E"), Edge("E", "F")]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #print self.G
        #self.G.show()

    def test_bipartite_bfs(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = BipartiteGraphBFS(self.G)
        algorithm.run("A")
        color_expected = {'A': 1, 'C': 1, 'E': 1, 'B': -1, 'D': -1, 'F': -1}
        self.assertEqual(algorithm.color, color_expected)

    def test_bipartite_dfs(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = BipartiteGraphDFS(self.G)
        algorithm.run("A")
        color_expected = {'A': 1, 'C': 1, 'E': 1, 'B': -1, 'D': -1, 'F': -1}
        self.assertEqual(algorithm.color, color_expected)

    def test_exceptions(self):
        self.G.add_edge(Edge("A", "E"))
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
