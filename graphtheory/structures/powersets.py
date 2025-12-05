#!/usr/bin/env python3

import sys

def iter_power_set(T):
    """Generate all subsets (tuples) of the given set T in O(2^n) time.

    The recursion depth equals to len(T).
    Ordering of the elements from T is preserved.
    """
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
