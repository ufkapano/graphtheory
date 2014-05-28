#!/usr/bin/python
#
# test_bfs.py
#
# Tests for BFS.

from edges import Edge
from graphs import Graph
from bfs import BFSWithQueue
import unittest

# r---s   t---u
# |   | / | / |
# v   w---x---y

class TestBFS(unittest.TestCase):

    def setUp(self):
        # The graph from Cormen p.607
        self.N = 8           # number of nodes
        self.G = Graph(self.N)
        self.nodes = ["r", "s", "t", "u", "v", "w", "x", "y"]
        self.edges = [Edge("r", "v"), Edge("r", "s"), 
        Edge("s", "w"), Edge("w", "t"), Edge("w", "x"), Edge("t", "x"),
        Edge("t", "u"), Edge("x", "u"), Edge("x", "y"), Edge("u", "y")]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #print self.G
        #self.G.show()

    def test_bfs(self):
        self.assertEqual(self.G.v(), self.N)
        ordering = []
        algorithm = BFSWithQueue(self.G)
        algorithm.run("s", action=lambda node: ordering.append(node))
        ordering_expected = ['s', 'r', 'w', 'v', 'x', 't', 'y', 'u']
        self.assertEqual(ordering, ordering_expected)
        dist_expected = dict([('s', 0), ('r', 1), ('w', 1), 
        ('t', 2), ('v', 2), ('x', 2), ('u', 3), ('y', 3)])
        self.assertEqual(algorithm.dist, dist_expected)
        prev_expected = dict([('s', None), ('r', 's'), ('u', 'x'), 
        ('t', 'w'), ('w', 's'), ('v', 'r'), ('y', 'x'), ('x', 'w')])
        # second possibility: (u,t) instead of (u,x)
        self.assertEqual(algorithm.prev, prev_expected)
        #algorithm.tree.show()
        self.assertEqual(algorithm.tree.v(), self.N)
        self.assertEqual(algorithm.tree.e(), self.N-1)

    def test_to_dag(self):
        algorithm = BFSWithQueue(self.G)
        algorithm.run("s")
        dag = algorithm.to_dag()
        self.assertTrue(dag.is_directed())
        self.assertEqual(dag.v(), self.N)
        self.assertEqual(dag.e(), self.N-1)

    def tearDown(self): pass

if __name__ == "__main__":

    #unittest.main()
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestBFS)
    suite = unittest.TestSuite([suite1])
    unittest.TextTestRunner(verbosity=2).run(suite)

# EOF
