#!/usr/bin/python
#
# edges.py
#
# Hashable edges - the idea for __hash__ from
# http://stackoverflow.com/questions/793761/built-in-python-hash-function

class Edge:
    """The class defining an edge."""

    def __init__(self, source, target, weight=1):
        """Loads up an Edge instance."""
        self.source = source
        self.target = target
        self.weight = weight

    def __repr__(self):
        """Computes the string representation of the edge."""
        return "Edge(%s, %s, %s)" % (
        repr(self.source), repr(self.target), self.weight)

    def __cmp__(self, other):
        """Comparing of edges (the weight first)."""
        # Check weights.
        if self.weight > other.weight: return 1
        if self.weight < other.weight: return -1
        # Check the first node.
        if self.source > other.source: return 1
        if self.source < other.source: return -1
        # Check the second node.
        if self.target > other.target: return 1
        if self.target < other.target: return -1
        return 0

    def __hash__(self):
        """Hashable edges."""
        return hash(repr(self))

    def __invert__(self):
        """Returns the edge with the opposite direction."""
        return Edge(self.target, self.source, self.weight)

    inverted = __invert__

# EOF
