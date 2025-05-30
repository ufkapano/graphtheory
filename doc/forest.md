# ALGORITHMS FOR TREES

## RECOGNITION

~~~python
from graphtheory.algorithms.acyclic import is_acyclic
from graphtheory.connectivity.connected import is_connected

# Testing a single tree G.
assert not G.is_directed()
assert G.v() == G.e() + 1
assert is_acyclic(G)
assert is_connected(G)
~~~

## RANDOM TREES

~~~python
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.factory import GraphFactory

gf = GraphFactory(Graph)
G = gf.make_tree(n=10)        # a random tree
assert G.v() == G.e() + 1
~~~

## FINDING A TREE CENTER (FOR A SINGLE TREE)

~~~python
from graphtheory.forests.treecenter import TreeCenter

algorithm = TreeCenter(G)
algorithm.run()
print ( algorithm.tree_center )   # one or two nodes
print ( algorithm.tree_radius )
~~~

## FINDING THE LONGEST PATH (FOR A SINGLE TREE)

~~~python
from graphtheory.forests.treelongestpath import TreeLongestPath

algorithm = TreeLongestPath(G)
algorithm.run()
print ( algorithm.longest_path )   # a list of nodes
~~~

## FINDING A PERFECT ELIMINATION ORDERING (PEO)

~~~python
from graphtheory.forests.treepeo import find_peo_tree
from graphtheory.forests.treepeo import TreePEO

# Every tree is a chordal graph.
peo = find_peo_tree(G)   # a list of nodes
assert len(peo) == G.v()

algorithm = TreePEO(G)
algorithm.run()
print ( algorithm.peo )   # a list of nodes
print ( algorithm.parent )   # a tree as a dict
~~~

## DRAWING A SINGLE TREE

~~~python
from graphtheory.forests.treeplot import TreePlot
from graphtheory.forests.treeplot import TreePlotRadiusAngle

algorithm = TreePlot(G)   # using float,  only for trees with n < 1e4
algorithm.run()
print ( algorithm.point_dict )   # a dict with point positions (float) in the plane

algorithm = TreePlotRadiusAngle(G)   # using fractions
algorithm.run()
print ( algorithm.point_dict )   # a dict with pairs (radius(int), angle(Fraction))
~~~

## FINDING A MAXIMUM INDEPENDENT SET

~~~python
from graphtheory.forests.treeiset import BorieIndependentSet
from graphtheory.forests.treeiset import TreeIndependentSet

algorithm = BorieIndependentSet(G)
algorithm.run()
print ( algorithm.independent_set )
print ( algorithm.cardinality )   # the size of max iset
print ( algorithm.parent )        # DFS tree as a dict

algorithm = TreeIndependentSet(G)
algorithm.run()
print ( algorithm.independent_set )
print ( algorithm.cardinality )   # the size of max iset
~~~

## FINDING A MINIMUM DOMINATING SET

~~~python
from graphtheory.forests.treedset import BorieDominatingSet
from graphtheory.forests.treedset import TreeDominatingSet

algorithm = BorieDominatingSet(G)
algorithm.run()
print ( algorithm.dominating_set )
print ( algorithm.cardinality )   # the size of min dset
print ( algorithm.parent )        # DFS tree as a dict

algorithm = TreeDominatingSet(G)
algorithm.run()
print ( algorithm.dominating_set )
print ( algorithm.cardinality )   # the size of min dset
~~~

## FINDING A MINIMUM NODE COVER

~~~python
from graphtheory.forests.treecover import BorieNodeCover
from graphtheory.forests.treecover import TreeNodeCover

algorithm = BorieNodeCover(G)
algorithm.run()
print ( algorithm.node_cover )
print ( algorithm.cardinality )   # the size of min cover
print ( algorithm.parent )        # DFS tree as a dict

algorithm = TreeNodeCover(G)
algorithm.run()
print ( algorithm.node_cover )
print ( algorithm.cardinality )   # the size of min cover
~~~

## FINDING A MAXIMUM MATCHING

~~~python
from graphtheory.forests.treemate import BorieMatching

algorithm = BorieMatching(G)
algorithm.run()
print ( algorithm.mate )
print ( algorithm.mate_set )
print ( algorithm.cardinality )   # the size of max matching
print ( algorithm.parent )        # DFS tree as a dict
~~~

EOF
