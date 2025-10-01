# GRAPH GENERATORS

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory

gf = GraphFactory(Graph)

G = gf.make_complete(n=10)        # complete graph (undirected)
G = gf.make_complete(n=10, directed=True)   # tournament (directed)
G = gf.make_path(n=10)            # undirected path graph P_n
G = gf.make_path(n=10, directed=True)   # directed path
G = gf.make_cyclic(n=10)         # undirected cyclic graph C_n
G = gf.make_cyclic(n=10, directed=True)    # directed cyclic graph
G = gf.make_sparse(n=10, directed=False, m=12) # random undirected graph with m edges
G = gf.make_tree(n=10)             # random tree
G = gf.make_connected(n=10, m=12)   # connected undirected graph
G = gf.make_random(n=10, directed=False, edge_probability=0.5)      # random undirected graph
G = gf.make_bipartite(10, 12, directed=False, edge_probability=0.5)   # random bipartite undirected graph
G = gf.make_grid(size=4)          # grid graph, size > 2
G = gf.make_grid_periodic(size=4)   # periodic grid graph, size > 2
G = gf.make_triangle(size=4)       # triangle graph, size > 2
G = gf.make_triangle_periodic(size=4)   # periodic triangle graph, size > 2
G = gf.make_ladder(size=4)        # ladder, size > 2
G = gf.make_prism(size=4)        # prism graph, size > 2
G = gf.make_antiprism(size=4)   # antiprism graph, size > 2
G = gf.make_flow_network(n=10)   # flow network (directed)
G = gf.make_necklace(n=10)   # necklace graph, n even
G = gf.make_wheel(n=10)       # wheel graph
G = gf.make_fake_wheel(n=10)       # fake wheel graph, n > 6

G.show()
~~~

EOF
