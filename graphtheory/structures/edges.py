#!/usr/bin/python

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
        return (self.source == other.source and self.target == other.target
            and self.weight == other.weight)

    def __ne__(self, other):
        """Comparing of edges (the weight first)."""
        return not (self == other)

    def __lt__(self, other):
        """Comparing of edges (the weight first)."""
        # Check weights.
        if self.weight > other.weight:
            return False
        if self.weight < other.weight:
            return True
        # Check the first node.
        if self.source > other.source:
            return False
        if self.source < other.source:
            return True
        # Check the second node.
        if self.target > other.target:
            return False
        if self.target < other.target:
            return True
        return False

    def __le__(self, other):
        """Comparing of edges (the weight first)."""
        # Check weights.
        if self.weight > other.weight:
            return False
        if self.weight < other.weight:
            return True
        # Check the first node.
        if self.source > other.source:
            return False
        if self.source < other.source:
            return True
        # Check the second node.
        if self.target > other.target:
            return False
        if self.target < other.target:
            return True
        return True

    def __gt__(self, other):
        """Comparing of edges (the weight first)."""
        # Check weights.
        if self.weight > other.weight:
            return True
        if self.weight < other.weight:
            return False
        # Check the first node.
        if self.source > other.source:
            return True
        if self.source < other.source:
            return False
        # Check the second node.
        if self.target > other.target:
            return True
        if self.target < other.target:
            return False
        return False

    def __ge__(self, other):
        """Comparing of edges (the weight first)."""
        # Check weights.
        if self.weight > other.weight:
            return True
        if self.weight < other.weight:
            return False
        # Check the first node.
        if self.source > other.source:
            return True
        if self.source < other.source:
            return False
        # Check the second node.
        if self.target > other.target:
            return True
        if self.target < other.target:
            return False
        return True

    def __cmp__(self, other):
        """Comparing of edges (the weight first)."""
        # Check weights.
        if self.weight > other.weight:
            return 1
        if self.weight < other.weight:
            return -1
        # Check the first node.
        if self.source > other.source:
            return 1
        if self.source < other.source:
            return -1
        # Check the second node.
        if self.target > other.target:
            return 1
        if self.target < other.target:
            return -1
        return 0

    def __hash__(self):
        """Hashable edges."""
        #return hash(repr(self))
        return hash((self.source, self.target, self.weight))

    def __invert__(self):
        """Return the edge with the opposite direction."""
        return self.__class__(self.target, self.source, self.weight)

    inverted = __invert__


class UndirectedEdge(Edge):
    """The class defining an undirected edge."""

    def __init__(self, source, target, weight=1):
        """Load up an edge instance."""
        if source > target:
            self.source = target
            self.target = source
        else:
            self.source = source
            self.target = target
        self.weight = weight

    def __invert__(self):
        """The edge direction is not defined."""
        return self

# EOF
