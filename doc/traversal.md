# GRAPH TRAVERSAL

## DFS

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.traversing.dfs import DFSWithStack
from graphtheory.traversing.dfs import DFSWithRecursion
from graphtheory.traversing.dfs import SimpleDFS
from graphtheory.traversing.dfs import DFSWithDepthTracker

G = Graph()
# Add nodes and edges here.
source = ...   # starting node
order = []
#algorithm = DFSWithStack(G)
#algorithm = DFSWithRecursion(G)
algorithm = SimpleDFS(G)
algorithm.run(source, pre_action=lambda node: order.append(node))
print(order)   # visited nodes
print(algorithm.parent)   # DFS tree as a dict
algorithm.dag.show()    # DFS tree as a directed graph
algorithm.path(source, target)   # construct a path from source to target

# finding a depth for nodes
algorithm = DFSWithDepthTracker(G)
algorithm.run(source, pre_action=lambda pair: order.append(pair))
print(order)   # visited nodes with depths, a list of pairs (node, depth)
~~~

## BFS

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.traversing.bfs import BFSWithQueue
from graphtheory.traversing.bfs import SimpleBFS
from graphtheory.traversing.bfs import BFSWithDepthTracker

G = Graph()
# Add nodes and edges here.
source = ...   # starting node
order = []
#algorithm = BFSWithQueue(G)
algorithm = SimpleBFS(G)
algorithm.run(source, pre_action=lambda node: order.append(node))
print(order)   # visited nodes
print(algorithm.parent)   # BFS tree as a dict
algorithm.dag.show()    # BFS tree as a directed graph
algorithm.path(source, target)   # construct a path from source to target

# Finding a depth for nodes.
algorithm = BFSWithDepthTracker(G)
algorithm.run(source, pre_action=lambda pair: order.append(pair))
print(order)   # visited nodes with depths, a list of pairs (node, depth)
~~~

EOF
