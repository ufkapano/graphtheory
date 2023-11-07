#!/usr/bin/env python3

import unittest
from graphtheory.chordality.intervalbfs import IntervalBFS

class TestBFS(unittest.TestCase):

    def setUp(self): pass

# 0---4---3   2tree graph
# | \ | /
# 2---1
#
# 2-----2
#   0-------0
#     1-------------1
#         4-----4
#             3---3
    def test_bfs1(self):
        perm = [2,0,1,2,4,0,3,4,3,1]
        preorder = []
        postorder = []
        algorithm = IntervalBFS(perm)
        algorithm.run(0, pre_action=lambda node: preorder.append(node),
                        post_action=lambda node: postorder.append(node))
        order_expected = [0, 1, 2, 4, 3]
        self.assertEqual(preorder, order_expected)
        self.assertEqual(postorder, order_expected)
        parent_expected = {0: None, 1: 0, 2: 0, 3: 1, 4: 0}
        self.assertEqual(algorithm.parent, parent_expected)
        self.assertEqual(algorithm.path(0, 3), [0, 1, 3])
        self.assertEqual(algorithm.path(0, 1), [0, 1])

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
