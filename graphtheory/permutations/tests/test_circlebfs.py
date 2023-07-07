#!/usr/bin/env python3

import unittest
from graphtheory.permutations.circlebfs import CircleBFS

class TestBFS(unittest.TestCase):

    def setUp(self): pass

# 0---4---3   house, prime circle graph
# |   | /
# 2---1
    def test_bfs1(self):
        perm = [3, 4, 1, 3, 0, 4, 2, 0, 1, 2]
        pre_order = []
        post_order = []
        algorithm = CircleBFS(perm)
        algorithm.run(0, pre_action=lambda node: pre_order.append(node),
                        post_action=lambda node: post_order.append(node))
        order_expected = [0, 2, 4, 1, 3]
        self.assertEqual(pre_order, order_expected)
        self.assertEqual(post_order, order_expected)
        parent_expected = {0: None, 1: 2, 2: 0, 3: 4, 4: 0}
        self.assertEqual(algorithm.parent, parent_expected)
        self.assertEqual(algorithm.path(0, 1), [0, 2, 1])
        self.assertEqual(algorithm.path(0, 3), [0, 4, 3])

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
