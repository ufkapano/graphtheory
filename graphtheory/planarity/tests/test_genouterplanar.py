#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.planarity.genouterplanar import MaximalOuterplanarGenerator


class TestOuterplanar(unittest.TestCase):

    def setUp(self): pass

    def test_triangle(self):    # graf C3
        n = 3
        algorithm = MaximalOuterplanarGenerator(n)
        algorithm.run()
        self.assertEqual(algorithm.graph.v(), n)
        self.assertEqual(algorithm.graph.e(), 2*n-3)
        #algorithm.graph.show()

    def test_2triangles(self):    # graf C3
        n = 4
        algorithm = MaximalOuterplanarGenerator(n)
        algorithm.run()
        self.assertEqual(algorithm.graph.v(), n)
        self.assertEqual(algorithm.graph.e(), 2*n-3)
        #algorithm.graph.show()

    def test_3triangles(self):    # graf C3
        n = 5
        algorithm = MaximalOuterplanarGenerator(n)
        algorithm.run()
        self.assertEqual(algorithm.graph.v(), n)
        self.assertEqual(algorithm.graph.e(), 2*n-3)
        #algorithm.graph.show()

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
