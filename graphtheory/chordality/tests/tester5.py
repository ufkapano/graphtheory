#!/usr/bin/env python3

from graphtheory.chordality.intervaltools import make_random_interval
from graphtheory.chordality.intervaltools import make_path_interval
from graphtheory.chordality.intervaltools import make_tepee_interval
from graphtheory.chordality.intervaltools import make_2tree_interval
from graphtheory.chordality.intervaltools import interval_drawing

n = 10   # liczba wierzcholkow
perm = make_random_interval(n)
print(perm)
interval_drawing(perm)
print()

# znak stop
perm = ["A","BB","CCC","A","BB","D","CCC","D"]
print(perm)
interval_drawing(perm)
print()

perm = make_path_interval(n)
print(perm)
interval_drawing(perm)
print()

perm = make_tepee_interval(n)
print(perm)
interval_drawing(perm)
print()

perm = make_2tree_interval(n)
print(perm)
interval_drawing(perm)
print()

# EOF
