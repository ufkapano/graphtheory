#!/usr/bin/python
#
# test_acyclic.py
#
# Tests.

from edges import Edge
from graphs import Graph
from acyclic import AcyclicGraphDFS
import unittest

# r---s   t---u   cycles are present
# |   | / | / |
# v   w---x---y

# r---s   t   u   without cycles
# |   | / | /
# v   w   x---y

class TestAcyclicUdirectedGraph(unittest.TestCase):

    def setUp(self):
        # The graph from Cormen p.607 changed.
        self.N = 8           # number of nodes
        self.G = Graph(self.N)
        self.nodes = ["r", "s", "t", "u", "v", "w", "x", "y"]
        self.edges = [Edge("r", "v"), Edge("r", "s"), Edge("s", "w"), 
        Edge("w", "t"), Edge("t", "x"), Edge("x", "u"), Edge("x", "y")]
        self.cycle_edges = [Edge("w", "x"), Edge("t", "u"), Edge("u", "y")]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #print self.G
        #self.G.show()

    def test_detect_no_cycles(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = AcyclicGraphDFS(self.G)
        algorithm.run("s")
        prev_expected = {'s': None, 'r': 's', 'u': 'x', 
        't': 'w', 'w': 's', 'v': 'r', 'y': 'x', 'x': 't'}
        self.assertEqual(algorithm.prev, prev_expected)

    def test_detect_cycle1(self):
        self.assertEqual(self.G.v(), self.N)
        self.G.add_edge(self.cycle_edges[0])
        algorithm = AcyclicGraphDFS(self.G)
        #self.assertRaises(ValueError, algorithm.run, "s")
        self.assertRaises(ValueError, algorithm.run)

    def test_detect_cycle2(self):
        self.assertEqual(self.G.v(), self.N)
        self.G.add_edge(self.cycle_edges[1])
        algorithm = AcyclicGraphDFS(self.G)
        #self.assertRaises(ValueError, algorithm.run, "s")
        self.assertRaises(ValueError, algorithm.run)

    def test_detect_cycle3(self):
        self.assertEqual(self.G.v(), self.N)
        self.G.add_edge(self.cycle_edges[2])
        algorithm = AcyclicGraphDFS(self.G)
        #self.assertRaises(ValueError, algorithm.run, "s")
        self.assertRaises(ValueError, algorithm.run)

    def tearDown(self): pass

#     A----------+
#     | \        |
#     |. \.      |
# +-->B   E      |
# |   |    \     |
# |   |.    \.  .|
# |   C<-----F-->H
# |   |      |
# |   |.     |.
# +---D      G

class TestAcyclicDirectedGraph(unittest.TestCase):

    def setUp(self):
        # The graph from
        self.N = 8           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = ["A","B","C","D","E","F","G","H"]
        self.edges = [Edge("A", "B"), Edge("B", "C"), Edge("C", "D"),
        Edge("A", "E"), Edge("E", "F"), Edge("F", "G"), Edge("F", "H"),
        Edge("F", "C"), Edge("A", "H")]
        self.cycle_edges = [Edge("D", "B"), Edge("F", "E")]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #print self.G
        #self.G.show()

    def test_detect_no_directed_cycles(self):
        self.assertEqual(self.G.v(), self.N)
        algorithm = AcyclicGraphDFS(self.G)
        algorithm.run("A")
        prev_expected = {'A': None, 'C': 'B', 'B': 'A', 
        'E': 'A', 'D': 'C', 'G': 'F', 'F': 'E', 'H': 'A'}
        self.assertEqual(algorithm.prev, prev_expected)

    def test_detect_directed_cycle1(self):
        self.assertEqual(self.G.v(), self.N)
        self.G.add_edge(self.cycle_edges[0])
        algorithm = AcyclicGraphDFS(self.G)
        #self.assertRaises(ValueError, algorithm.run, "A")
        self.assertRaises(ValueError, algorithm.run)

    def test_detect_directed_cycle2(self):
        self.assertEqual(self.G.v(), self.N)
        self.G.add_edge(self.cycle_edges[1])
        algorithm = AcyclicGraphDFS(self.G)
        #self.assertRaises(ValueError, algorithm.run, "A")
        self.assertRaises(ValueError, algorithm.run)

    def tearDown(self): pass

if __name__ == "__main__":

    #unittest.main()
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestAcyclicUdirectedGraph)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestAcyclicDirectedGraph)
    suite = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)

# EOF
