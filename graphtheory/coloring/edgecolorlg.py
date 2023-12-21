#!/usr/bin/env python3

try:
    range = xrange
except NameError:   # Python 3
    pass

from graphtheory.structures.edges import Edge
from graphtheory.coloring.nodecolorus import UnorderedSequentialNodeColoring as NodeColoring
#from graphtheory.coloring.nodecolorrs import RandomSequentialNodeColoring as NodeColoring


class EdgeColoringWithLineGraph:
    """Find an edge coloring using a line graph.
    
    Based on ideas from
    http://edu.i-lo.tarnow.pl/inf/alg/001_search/0126c.php
    
    Attributes
    ----------
    graph : input undirected graph or multigraph
    color : dict with edges (values are colors)
    m : number (the number od edges)
    
    Notes
    -----
    Colors are 0, 1, 2, ...
    edge.source < edge.target for any edge in color.
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.color = dict()
        self.m = 0   # graph.e() is slow
        for edge in self.graph.iteredges():
            if edge.source == edge.target:
                raise ValueError("a loop detected")
            else:
                self.color[edge] = None   # edge.source < edge.target
                self.m += 1
        if len(self.color) < self.m:
            raise ValueError("edges are not unique")

    def run(self):
        """Executable pseudocode."""
        line_graph = self.graph.__class__(self.graph.e(), directed=False)
        # Trzeba dodac wierzcholki do grafu krawedziowego.
        # Graf krawedziowy moze byc niespojny!
        for edge in self.graph.iteredges():
            line_graph.add_node(edge)
        for node in self.graph.iternodes():
            for edge1 in self.graph.iteroutedges(node):
                for edge2 in self.graph.iteroutedges(edge1.target):
                    # Normalizing edge directions..
                    if edge1.source > edge1.target:
                        edge1 = ~edge1
                    if edge2.source > edge2.target:
                        edge2 = ~edge2
                    if edge1 < edge2:
                        line_graph.add_edge(Edge(edge1, edge2))
        algorithm = NodeColoring(line_graph)
        algorithm.run()
        self.color = algorithm.color
        #line_graph.show()

# EOF
