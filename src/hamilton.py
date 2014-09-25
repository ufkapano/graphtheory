#!/usr/bin/python

from edges import Edge

class HamiltonCycle:
    """Finding a Hamiltonian cycle in a Hamiltonian graph."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        self.hamilton_cycle = list()

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:   # get first random node
            source = self.graph.iternodes().next()
        self.source = source
        self.queue = []
        self.visited = set()
        self._hamilton_dfs(self.source)

    def _hamilton_dfs(self, node):
        """Modified DFS from the node."""
        if self.hamilton_cycle:
            return
        self.queue.append(node)
        if len(self.queue) == self.graph.v():
            if self.graph.has_edge(Edge(self.queue[-1], self.source)):
                self.hamilton_cycle = list(self.queue)
        else:
            self.visited.add(node)
            for target in self.graph.iteradjacent(node):
                if target not in self.visited:
                    self._hamilton_dfs(target)
            self.visited.discard(node)
        self.queue.pop()

# EOF
