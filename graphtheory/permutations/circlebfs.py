#!/usr/bin/env python3

import collections

class CircleBFS:
    """Breadth-First Search for circle graphs in O(n^2) time."""

    def __init__(self, perm):
        """The algorithm initialization."""
        self.perm = perm
        self.parent = dict()   # BFS tree
        self.pairs = dict((node, []) for node in set(self.perm))   # O(n) time
        for idx, node in enumerate(self.perm):   # O(n) time
            self.pairs[node].append(idx)

    def has_edge(self, source, target):
        s1, s2 = self.pairs[source]
        t1, t2 = self.pairs[target]
        return (s1 < t1 < s2 < t2) or (t1 < s1 < t2 < s2)

    def run(self, source=None, pre_action=None, post_action=None):
        """Executable pseudocode."""
        if source is not None:
            self._visit(source, pre_action, post_action)
        else:
            for node in self.perm:   # iternodes()
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
            for target in self.pairs:   # iteroutedges(source), O(n) time
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
