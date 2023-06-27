#!/usr/bin/env python3

try:
    integer_types = (int, long)
    range = xrange
except NameError:   # Python 3
    integer_types = (int,)

import random
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph

def make_random_circle(n):
    """Return a random circle graph as double perm."""
    #double_perm = list(range(n)) * 2
    double_perm = [i % n for i in range(2*n)]
    random.shuffle(double_perm)
    return double_perm

def make_path_circle(n):
    """Return a path graph P_n as double perm."""
    perm = []
    for i in range(n):
        perm.extend((i, i))
    for i in range(1, 2*n-1, 2):
        perm[i], perm[i+1] = perm[i+1], perm[i]
    return perm

def make_cycle_circle(n):
    """Return a cycle graph C_n as double perm."""
    if n < 3:
        raise ValueError("n has to be greater than 2")
    perm = []
    for i in range(n):
        perm.extend((i, i))
    for i in range(1, 2*n-1, 2):
        perm[i], perm[i+1] = perm[i+1], perm[i]
    perm[0], perm[-1] = perm[-1], perm[0]
    return perm

# EOF
