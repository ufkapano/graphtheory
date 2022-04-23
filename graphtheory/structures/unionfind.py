#!/usr/bin/env python3

class UnionFind:
    """Disjoint-set data structure.
    
    Notes
    -----
    Union-Find according to
    
    Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C., 2009, 
        Introduction to Algorithms, third edition, The MIT Press, 
        Cambridge, London.
    """

    def __init__(self):
        """Disjoint-set initialization."""
        self.parent = dict()
        self.rank = dict()

    def create(self, x):
        """Make a set containing only a given element."""
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

    def find(self, x):
        """Determine which subset an element is in."""
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x]) # kompresja
        return self.parent[x]

    def union(self, x, y):
        """Join two subsets into a single subset."""
        x = self.find(x)
        y = self.find(y)
        if x == y:   # the same set
            return
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] = self.rank[y] + 1

# EOF
