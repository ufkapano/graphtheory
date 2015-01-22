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
        self.distance = dict((node, float("inf")) for node in self.graph.iternodes())
        # Shortest path tree as a dictionary.
        self.parent = dict((node, None) for node in self.graph.iternodes())

    def run(self, source):
        """Executable pseudocode."""
        self.source = source
        self.distance[source] = 0
        algorithm = TopologicalSortDFS(self.graph)
        algorithm.run()
        for source in algorithm.sorted_nodes:
            for edge in self.graph.iteroutedges(source):
                self._relax(edge)

    def _relax(self, edge):
        """Edge relaxation."""
        alt = self.distance[edge.source] + edge.weight
        if self.distance[edge.target] > alt:
            self.distance[edge.target] = alt
            self.parent[edge.target] = edge.source
            return True
        return False

    def path(self, target):
        """Construct a path from source to target."""
        if self.source == target:
            return [self.source]
        elif self.parent[target] is None:
            raise ValueError("no path to target")
        else:
            return self.path(self.parent[target]) + [target]

# EOF
