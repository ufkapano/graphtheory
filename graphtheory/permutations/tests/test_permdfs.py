#!/usr/bin/env python3

import unittest
from graphtheory.permutations.permdfs import PermDFS

class TestDFS(unittest.TestCase):

    def setUp(self): pass

# 0---4---3
# |   | /
# 2---1
    def test_dfs1(self):
        perm = [2, 4, 0, 3, 1]
        pre_order = []
        post_order = []
        algorithm = PermDFS(perm)
        algorithm.run(0, pre_action=lambda node: pre_order.append(node),
                        post_action=lambda node: post_order.append(node))
        pre_order_expected = [0, 2, 1, 4, 3]
        post_order_expected = [3, 4, 1, 2, 0]
        self.assertEqual(pre_order, pre_order_expected)
        self.assertEqual(post_order, post_order_expected)
        parent_expected = {0: None, 1: 2, 2: 0, 3: 4, 4: 1}
        self.assertEqual(algorithm.parent, parent_expected)
        self.assertEqual(algorithm.path(0, 1), [0, 2, 1])
        self.assertEqual(algorithm.path(0, 3), [0, 2, 1, 4, 3])

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
