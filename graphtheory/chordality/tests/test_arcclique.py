#!/usr/bin/env python3

import unittest
from graphtheory.chordality.arcclique import GavrilMaximumClique


class TestGavrilMaximumClique(unittest.TestCase):

    def setUp(self): pass

    def test_max_clique_gavril_paper(self):
        graph_model = [(0,5), (2,6), (4,8), (7,11), (9,13), (10,14),
            (12,16), (15,18), (17,1), (19,3)]

        algorithm = GavrilMaximumClique(graph_model)
        algorithm.run()
        maximum_clique = algorithm.maximum_clique
        
        expected_maximum_cliques = [
                                       [0,1,2],
                                       [0,8,9],
                                       [0,1,9],
                                       [3,4,5],
                                       [4,5,6]
                                    ]
        
        self.assertIn(sorted(maximum_clique), expected_maximum_cliques)


    def test_max_clique_gavril_0(self):
        graph_model = [(10,3),(11,1),(0,2),(4,6),(5,8),(7,9)]

        algorithm = GavrilMaximumClique(graph_model)
        algorithm.run()
        maximum_clique = algorithm.maximum_clique

        expected_maximum_cliques = [ [0,1,2] ]
        
        self.assertIn(sorted(maximum_clique), expected_maximum_cliques)


    def test_max_clique_gavril_1(self):
        graph_model = [(5,11),(6,7),(2,1),(3,0),(8,9),(10,4)]

        algorithm = GavrilMaximumClique(graph_model)
        algorithm.run()
        maximum_clique = algorithm.maximum_clique

        expected_maximum_cliques = [ 
                                        [0,1,2,3],
                                        [0,2,3,4],
                                        [0,2,3,5]
                                    ]
        
        self.assertIn(sorted(maximum_clique), expected_maximum_cliques)


    def test_max_clique_gavril_2(self):
        graph_model = [(0,5),(1,2),(3,9),(4,7),(6,10),(8,11)]

        algorithm = GavrilMaximumClique(graph_model)
        algorithm.run()
        maximum_clique = algorithm.maximum_clique

        expected_maximum_cliques = [ 
                                        [0,2,3],
                                        [2,3,4],
                                        [2,4,5]
                                    ]
        
        self.assertIn(sorted(maximum_clique), expected_maximum_cliques)


    def test_max_clique_gavril_3(self):
        graph_model = [(15,0),(16,3),(17,1),(12,2),(4,6),(5,10),(7,13),
            (9,14),(8,11)]

        algorithm = GavrilMaximumClique(graph_model)
        algorithm.run()
        maximum_clique = algorithm.maximum_clique

        expected_maximum_cliques = [ 
                                        [0,1,2,3],
                                        [4,5,7,8],
                                        [5,6,7,8]
                                    ]
        
        self.assertIn(sorted(maximum_clique), expected_maximum_cliques)


    def test_max_clique_gavril_4(self):
        graph_model = [(0,4),(1,5),(2,7),(3,8),(6,9)]

        algorithm = GavrilMaximumClique(graph_model)
        algorithm.run()
        maximum_clique = algorithm.maximum_clique

        expected_maximum_cliques = [ [0,1,2,3] ]
        
        self.assertIn(sorted(maximum_clique), expected_maximum_cliques)


    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()
