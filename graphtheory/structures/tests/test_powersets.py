#!/usr/bin/env python3

import unittest
from graphtheory.structures.powersets import iter_power_set


class TestPowerSet(unittest.TestCase):

    def setUp(self): pass

    def test_iter_power_set2(self):
        S = set(iter_power_set(range(2)))
        #print(S)
        S_expected = set([(), (1,), (0,), (0, 1), ])
        self.assertEqual(S, S_expected)
        self.assertEqual(len(S), pow(2, 2))

    def test_iter_power_set3(self):
        S = set(iter_power_set(range(3)))
        #print(S)
        S_expected = set([(), (0,), (1,), (2,),
            (0, 1), (0, 2), (1, 2), (0, 1, 2),])
        self.assertEqual(S, S_expected)
        self.assertEqual(len(S), pow(2, 3))

    def test_iter_power_set(self):
        N = 5
        length = sum(1 for s in iter_power_set(range(N)))
        #print(list(iter_power_set(range(N))))
        self.assertEqual(length, pow(2, N))

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
