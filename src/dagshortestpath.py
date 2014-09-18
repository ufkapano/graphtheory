#!/usr/bin/python

from edges import Edge
from topsort import TopologicalSortDFS


class DAGShortestPath:
    """The shortest path problem for DAG."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if not graph.is_directed():
            raise ValueError("graph is not directed")
        self.graph = graph
        self.dist = dict((node, float("inf")) for node in self.graph.iternodes())
        # shortest path tree
        self.prev = dict((node, None) for node in self.graph.iternodes())

    def run(self, source):
        """Executable pseudocode."""
        self.source = source
        self.dist[source] = 0
        ts = TopologicalSortDFS(self.graph)
        ts.run()
        for source in ts.sorted_nodes:
            for edge in self.graph.iteroutedges(source):
                self.relax(edge)

    def relax(self, edge):
        """Edge relaxation."""
        alt = self.dist[edge.source] + edge.weight
        if self.dist[edge.target] > alt:
            self.dist[edge.target] = alt
            self.prev[edge.target] = edge.source
            return True
        return False

    def path(self, target):
        """Construct a path from source to target."""
        if self.source == target:
            return [self.source]
        elif self.prev[target] is None:
            raise ValueError("no path to target")
        else:
            return self.path(self.prev[target]) + [target]

# EOF