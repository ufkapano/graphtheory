#!/usr/bin/env python3
#
# Python 2.7 and Python 3.2+ [@total_ordering]

from functools import total_ordering

@total_ordering
class Edge:
    """The class defining a directed edge.
    
    Attributes
    ----------
    source : starting node
    target : ending node
    weight : number (edge weight)
    
    Examples
    --------
    >>> from graphtheory.structures.edges import Edge
    >>> edge = Edge(1, 2, 5)
    >>> ~edge
    Edge(2, 1, 5)
    
    Notes
    -----
    Hashable edges - the idea for __hash__ from
    
    http://stackoverflow.com/questions/793761/built-in-python-hash-function
    """

    def __init__(self, source, target, weight=1):
        """Load up a directed edge instance.
        
        Parameters
        ----------
        source : starting node
        target : ending node
        weight : number, optional (default=1)
        """
        self.source = source
        self.target = target
        self.weight = weight

    def __repr__(self):
        """Compute the string representation of the edge."""
        if self.weight == 1:
            return "{}({}, {})".format(
                self.__class__.__name__,
                repr(self.source),
                repr(self.target))
        else:
            return "{}({}, {}, {})".format(
                self.__class__.__name__,
                repr(self.source),
                repr(self.target),
                repr(self.weight))

    def __eq__(self, other):
        """Comparing of edges (the weight first)."""
        return (self.source, self.target, self.weight) == (
            other.source, other.target, other.weight)

    def __ne__(self, other):
        """Comparing of edges (the weight first)."""
        return not self == other

    def __lt__(self, other):
        """Comparing of edges (the weight first)."""
        return (self.weight, self.source, self.target) < (
            other.weight, other.source, other.target)

    def __hash__(self):
        """Hashable edges."""
        return hash((self.source, self.target, self.weight))

    def __invert__(self):
        """Return the edge with the opposite direction."""
        return self.__class__(self.target, self.source, self.weight)

    inverted = __invert__

# EOF
