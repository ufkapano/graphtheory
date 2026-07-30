#!/usr/bin/env python3

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.chordality.arctools import make_random_arc
from graphtheory.chordality.arctools import make_cycle_arc
from graphtheory.chordality.arctools import make_complete_arc
from graphtheory.chordality.arctools import make_abstract_arc_graph


class TestCircularArcGraphs(unittest.TestCase):

    def setUp(self): pass

    def test_random_arc(self):
        n = 10
        reprB = make_random_arc(n)
        #print("random", reprB)
        self.assertEqual(len(reprB), n)
        self.assertTrue(reprB[0][0] < reprB[0][1])
        events = [event for pair in reprB for event in pair]
        #print("events", events)
        self.assertEqual(sorted(events), list(range(2*n)))

    def test_cycle_arc(self):
        self.assertEqual(make_cycle_arc(3), [(0,3),(2,5),(4,1)])
        self.assertEqual(make_cycle_arc(4), [(0,3),(2,5),(4,7),(6,1)])
        self.assertRaises(AssertionError, make_cycle_arc, 1)
        self.assertRaises(AssertionError, make_cycle_arc, 2)

    def test_complete_arc(self):
        self.assertEqual(make_complete_arc(3), [(0, 3), (1, 4), (2, 5)])
        self.assertEqual(make_complete_arc(4), [(0, 4), (1, 5), (2, 6), (3, 7)])

    def test_make_abstract_arc_graph1(self):
        #   1       graf znaku 'stop' po wygenerowaniu
        #  / \
        # 3---2---0
        reprB = [(5,7), (0,3), (2,6), (1,4)]   # 'stop' graph
        G = make_abstract_arc_graph(reprB)
        #G.show()
        self.assertEqual(G.v(), len(reprB))
        self.assertEqual(G.e(), len(reprB))

    def test_make_abstract_arc_graph2(self):
        #   3       graf znaku 'stop' po wygenerowaniu
        #  / \
        # 0---1---2
        reprB = [(0, 1), (4, 3), (5, 6), (7, 2)]   # 'stop' graph
        G = make_abstract_arc_graph(reprB)
        #G.show()
        self.assertEqual(G.v(), len(reprB))
        self.assertEqual(G.e(), len(reprB))

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
