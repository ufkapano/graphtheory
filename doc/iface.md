# INTERFACE FOR GRAPHS AND MULTIGRAPHS

* G, H - graphs or multigraphs.
* node, source, target - usually integer or string (hashable, with order).
    For matrixgraphs, nodes are int from 0 to n-1.
* edge - an instance of the Edge class (hashable, with order, directed).

## (DIRECTED) EDGES

~~~python
from graphtheory.structures.edges import Edge

edge = Edge(source, target, weight=1)   # return a directed edge
edge.source    # the edge source
edge.target    # the edge target
edge.weight    # the edge weight (default 1)
repr(edge)     # return a string
hash(edge)     # return hash
~edge          # return the edge with the opposite direction

# Comparing edges (order: weight, source, target).
e1 == e2, e1 != e2, e1 < e2, e1 <= e2, e1 > e2, e1 >= e2
~~~

# GRAPHS AND MULTIGRAPHS

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.multigraphs import MultiGraph

Graph()        # return an empty undirected graph (graphs, setgraphs, dictgraphs)
Graph(directed=True) # return an empty directed graph (graphs, setgraphs, dictgraphs)

Graph(n=N)     # return an undirected graph with N nodes (matrixgraphs)
Graph(n=N, directed=True) # return a directed graph with N nodes (matrixgraphs)

MultiGraph()   # return an empty undirected multigraph (multigraphs)
MultiGraph(directed=True) # return an empty directed multigraph (multigraphs)

G.is_directed() # return True if G is a directed graph
G.v()           # return the number of nodes
G.e()           # return the number of edges
G.f()           # return the number of faces (for planar graphs)

G.add_node(node)   # add the node to G (only testing for matrixgraphs)
G.del_node(node)   # remove the node form G (only remove adjacent edges for matrixgraphs)
G.has_node(node)   # return True if the node is in G

G.add_edge(edge)              # add the edge to G
G.add_edge((source, target))  # add the edge to G (default weight is 1)
G.del_edge(edge)              # remove the edge form G
G.del_edge((source, target))  # remove the edge form G
G.has_edge(edge)              # return True if the edge is in G
G.has_edge((source, target))  # return True if the edge is in G
G.weight(edge)                # return the edge weight or zero
G.weight((source, target))    # return the edge weight or zero
# for multigraphs: return the number of parallel edges

G.iternodes()       # generate nodes on demand
G.iteredges()       # generate edges on demand
G.iteredges_connected(start_edge)   # generate connected edges on demand
G.iterfaces()       # generate all faces on demand (for planar graphs)
G.iterface(start_edge)   # generate edges from the same face on demand (for planar graphs)

G.iteroutedges(node)   # generate outedges on demand
G.iterinedges(node)    # generate inedges on demand
G.iteradjacent(node)   # generate adjacent nodes on demand

G.degree(node)      # return the degree of the node (G undirected)
G.indegree(node)    # return the indegree of the node
G.outdegree(node)   # return the outdegree of the node

G.show()            # the graph presentation
G.copy()            # return the graph copy
G.transpose()       # return the transpose of G
G.complement()      # return the complement of G
G.subgraph(nodes)   # return the induced subgraph
G == H, G != H      # graph comparisons
~~~

EOF
