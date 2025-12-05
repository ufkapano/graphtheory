#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.cliques.bronkerbosch2 import BronKerboschClassicIterator
from graphtheory.cliques.bronkerboschrp2 import BronKerboschRandomPivotIterator
from graphtheory.cliques.bronkerboschdp2 import BronKerboschDegreePivotIterator
from graphtheory.cliques.bronkerboschdeg2 import BronKerboschDegeneracyIterator

# 0---1---2---3   maximum clique {2, 3, 5}
#     |   | /     MDO [0, 1, 4, 2, 5, 3]
#     4---5

class TestBronKerbosch(unittest.TestCase):

    def setUp(self):
        self.N = 6           # number of nodes
        self.G = Graph()
        self.nodes = range(self.N)
        self.edges = [Edge(0, 1), Edge(1, 2), Edge(1, 4), Edge(2, 3),
            Edge(2, 5), Edge(3, 5), Edge(4, 5)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_bron_kerbosch_classic_iterator(self):
        algorithm = BronKerboschClassicIterator(self.G)
        iterator = algorithm.run()
        cliques_expected = [{0, 1}, {1, 2}, {1, 4}, {4, 5}, {2, 3, 5}]
        cliques = sorted(iterator, key=len)
        self.assertEqual(cliques, cliques_expected)

    def test_bron_kerbosch_random_pivot_iterator(self):
        algorithm = BronKerboschRandomPivotIterator(self.G)
        iterator = algorithm.run()
        cliques_expected = [{0, 1}, {1, 2}, {1, 4}, {4, 5}, {2, 3, 5}]
        cliques = sorted(iterator, key=len)
        self.assertEqual(cliques, cliques_expected)

    def test_bron_kerbosch_degree_pivot_iterator(self):
        algorithm = BronKerboschDegreePivotIterator(self.G)
        iterator = algorithm.run()
        cliques_expected = [{0, 1}, {1, 2}, {1, 4}, {4, 5}, {2, 3, 5}]
        cliques = sorted(iterator, key=len)
        self.assertEqual(cliques, cliques_expected)

    def test_bron_kerbosch_degeneracy_iterator(self):
        algorithm = BronKerboschDegeneracyIterator(self.G)
        iterator = algorithm.run()
        cliques_expected = [{0, 1}, {1, 4}, {1, 2}, {4, 5}, {2, 3, 5}]
        cliques = sorted(iterator, key=len)
        self.assertEqual(cliques, cliques_expected)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
