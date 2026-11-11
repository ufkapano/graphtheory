# GRAPH COLORING

## M COLORING PROBLEM

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.coloring.nodecolorbt import BacktrackingNodeColoring

G = Graph()
# Add nodes and edges here.
# Set m_colors.
algorithm = BacktrackingNodeColoring(G, m_colors)
algorithm.run()
for node in G.iternodes():
    print(node, algorithm.color[node])
~~~

## VERTEX COLORING

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.coloring.nodecolorexact import ExactNodeColoring
from graphtheory.coloring.nodecolorus import UnorderedSequentialNodeColoring
from graphtheory.coloring.nodecolorrs import RandomSequentialNodeColoring
from graphtheory.coloring.nodecolorcs import ConnectedSequentialNodeColoring
from graphtheory.coloring.nodecolorsl import SmallestLastNodeColoring
from graphtheory.coloring.nodecolorlf import LargestFirstNodeColoring
from graphtheory.coloring.nodecolorslf import SLFNodeColoring
from graphtheory.coloring.nodecolorgis import GISNodeColoring
from graphtheory.coloring.nodecolorrlf import RLFNodeColoring
from graphtheory.coloring.nodecolorbrooks import BrooksNodeColoring

G = Graph()
# Add nodes and edges here.
# algorithm = ExactlNodeColoring(G)
# algorithm = UnorderedSequentialNodeColoring(G)   # O(n+m) time
# algorithm = RandomSequentialNodeColoring(G)   # O(n+m) time
# algorithm = ConnectedSequentialNodeColoring(G)   # O(n+m) time
# algorithm = SmallestLastNodeColoring(G)
# algorithm = LargestFirstNodeColoring(G)   # O(n+m) time
# algorithm = SLFNodeColoring(G)
# algorithm = GISNodeColoring(G)
# algorithm = RLFNodeColoring(G)
algorithm = BrooksNodeColoring(G)   # O(n^2) time
# The BrooksNodeColoring implementation finds Delta-coloring in two cases:
# (1) for connected graphs which are not Delta-regular,
# (2) for Delta-regular 3-connected graphs.
algorithm.run()
for node in G.iternodes():
    print(node, algorithm.color[node])
~~~

## EDGE COLORING

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.coloring.edgecolorus import UnorderedSequentialEdgeColoring
from graphtheory.coloring.edgecolorrs import RandomSequentialEdgeColoring
from graphtheory.coloring.edgecolorcs import ConnectedSequentialEdgeColoring
from graphtheory.coloring.edgecolorlg import EdgeColoringWithLineGraph
from graphtheory.coloring.edgecolorntl import NTLEdgeColoring

G = Graph()
# Add nodes and edges here.
# algorithm = UnorderedSequentialEdgeColoring(G)
# algorithm = RandomSequentialEdgeColoring(G)
# algorithm = ConnectedSequentialEdgeColoring(G)
# algorithm = EdgeColoringWithLineGraph(G)
algorithm = NTLEdgeColoring(G)   # use Delta or Delta+1 colors
algorithm.run()
algorithm.show_colors()
for edge in G.iteredges():
    print(edge, algorithm.color[edge])

# Edge coloring for complete graphs and bipartite graphs.
from graphtheory.structures.factory import GraphFactory
from graphtheory.coloring.edgecolorcomplete import CompleteGraphEdgeColoring
from graphtheory.coloring.edgecolorbipartite import CompleteBipartiteGraphEdgeColoring
from graphtheory.coloring.edgecolorbipartite import BipartiteGraphEdgeColoring

gf = GraphFactory(Graph)
G = gf.make_complete(n=10)   # K_10 graph
algorithm = CompleteGraphEdgeColoring(G)   # O(n^2) time
# n colors for n odd, n-1 colors for n even.
algorithm.run()
algorithm.show_colors()

G = gf.make_bipartite(n1=6, n2=7, directed=False, edge_probability=1) # K_{6,7}
algorithm = CompleteBipartiteGraphEdgeColoring(G)
algorithm.run()   # Delta colors are used
algorithm.show_colors()

G = gf.make_bipartite(n1=8, n2=9, directed=False, edge_probability=0.5)
algorithm = BipartiteGraphEdgeColoring(G)   # O(VE) time
algorithm.run()   # Delta colors are used
algorithm.show_colors()
~~~

EOF
