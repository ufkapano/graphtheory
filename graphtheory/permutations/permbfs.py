#!/usr/bin/env python3

import collections

class PermBFS:
    """Breadth-First Search for permutation graphs in O(n^2) time."""

    def __init__(self, perm):
        """The algorithm initialization."""
        self.perm = perm
        self.parent = dict()   # BFS tree
        self.position = list(perm)   # temporary, O(n) memory
        for k, item in enumerate(perm):   # O(n) time
            self.position[item] = k   # for testing edges

    def has_edge(self, i, j):
        if i > j:
            i, j = j, i
        return self.position[i] > self.position[j]

    def run(self, source=None, pre_action=None, post_action=None):
        """Executable pseudocode."""
        if source is not None:
            self._visit(source, pre_action, post_action)
        else:
            for node in self.perm:
                if node not in self.parent:
                    self._visit(node, pre_action, post_action)

    def _visit(self, node, pre_action=None, post_action=None):
        """Explore the connected component."""
        Q = collections.deque()
        self.parent[node] = None   # before Q.put
        Q.appendleft(node)
        if pre_action:   # when Q.put
            pre_action(node)
        while Q:   # while not empty, O(n) time
            source = Q.pop()
            for target in self.perm:   # iteroutedges(source), O(n) time
                if self.has_edge(source, target) and target not in self.parent:
                    self.parent[target] = source   # before Q.put
                    Q.appendleft(target)
                    if pre_action:   # when Q.put
                        pre_action(target)
            if post_action:
                post_action(source)

    def path(self, source, target):
        """Construct a path from source to target."""
        if source == target:
            return [source]
        elif self.parent[target] is None:
            raise ValueError("no path to target")
        else:
            return self.path(source, self.parent[target]) + [target]

# EOF
