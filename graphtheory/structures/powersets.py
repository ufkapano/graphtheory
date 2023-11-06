#!/usr/bin/env python3
#
# Zbiory sa reprezentaowane jako krotki.
# Zachowywana jest kolejnosc elementow w krotce.

import sys

def iter_power_set(T):
    """Generuje wszystkie podzbiory danego zbioru."""
    # Glebokosc rekurencji rowna sie len(T).
    recursionlimit = sys.getrecursionlimit()
    sys.setrecursionlimit(max(len(T) * 2, recursionlimit))
    if len(T) == 0:
        yield tuple()
    else:
        item = (T[0],)
        for subset in iter_power_set(T[1:]):
            yield subset
            yield item + subset

# EOF
