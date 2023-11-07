#!/usr/bin/env python3

import sys
import collections

class IntervalDFS:
    """Depth-First Search for interval graphs in O(n^2) time."""

    def __init__(self, perm):
        """The algorithm initialization."""
        self.perm = perm
        self.parent = dict()   # BFS tree
        self.pairs = dict((node, []) for node in set(self.perm)) # O(n) time
        for idx, node in enumerate(self.perm): # O(n) time
            self.pairs[node].append(idx)
        #print("pairs", self.pairs)
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(len(self.perm) * 2, recursionlimit))

    def has_edge(self, source, target):
        s1, s2 = self.pairs[source]
        t1, t2 = self.pairs[target]
        return not (s2 < t1 or t2 < s1)

    def run(self, source=None, pre_action=None, post_action=None):
        """Executable pseudocode."""
        if source is not None:
            self.parent[source] = None   # before _visit
            self._visit(source, pre_action, post_action)
        else:
            for node in self.pairs:   # iternodes()
                if node not in self.parent:
                    self.parent[node] = None   # before _visit
                    self._visit(node, pre_action, post_action)

    def _visit(self, node, pre_action=None, post_action=None):
        """Explore recursively the connected component."""
        if pre_action:
            pre_action(node)
        for target in self.pairs: # iteroutedges(node), O(n) time
            if self.has_edge(node, target) and target not in self.parent:
                self.parent[target] = node   # before _visit
                self._visit(target, pre_action, post_action)
        if post_action:
            post_action(node)

    def path(self, source, target):
        """Construct a path from source to target."""
        if source == target:
            return [source]
        elif self.parent[target] is None:
            raise ValueError("no path to target")
        else:
            return self.path(source, self.parent[target]) + [target]

# EOF
