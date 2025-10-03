#!/usr/bin/env python3

import sys
import collections

class PermDFS:
    """Depth-First Search for permutation graphs in O(n^2) time."""

    def __init__(self, perm):
        """The algorithm initialization."""
        self.perm = perm
        self.parent = dict()   # DFS tree
        self.position = list(perm)   # temporary, O(n) memory
        for k, item in enumerate(perm):   # O(n) time
            self.position[item] = k   # for testing edges
        recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(max(len(self.perm) * 2, recursionlimit))

    def has_edge(self, i, j):
        if i > j:
            i, j = j, i
        return self.position[i] > self.position[j]

    def run(self, source=None, pre_action=None, post_action=None):
        """Executable pseudocode."""
        if source is not None:
            self.parent[source] = None   # before _visit
            self._visit(source, pre_action, post_action)
        else:
            for node in self.perm:
                if node not in self.parent:
                    self.parent[node] = None   # before _visit
                    self._visit(node, pre_action, post_action)

    def _visit(self, node, pre_action=None, post_action=None):
        """Explore recursively the connected component."""
        if pre_action:
            pre_action(node)
        for target in self.perm: # iteroutedges(node)
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
