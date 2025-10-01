# CLUSTERING

~~~python
from graphtheory.structures.points import Point
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.spanningtrees.clustering import KruskalClustering

G = Graph()
point_list = [ ... ]   # points in the plane
for point in point_list:
    G.add_node(point)
for p1 in point_list:
    for p2 in point_list:
        if p1 < p2:
            G.add_edge(Edge(p1, p2, (p1-p2).length()))
# Set the number of clusters here (n_clusters).
algorithm = KruskalClustering(G, n_clusters)
algorithm.run()
# The result is in algorithm.uf (union-find structure)
# and in algorithm.clusters (keys are representatives, values are clusters).
for rep in algorithm.clusters:
    print ( algorithm.clusters[rep] )
~~~

EOF
