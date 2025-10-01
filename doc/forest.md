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
G = gf.make_tree(n=10)        # a random tree (connected)
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
from graphtheory.forests.treedset import TreeDominatingSet1
from graphtheory.forests.treedset import TreeDominatingSet2
from graphtheory.forests.treedset import TreeDominatingSet3
from graphtheory.forests.treedset import TreeDominatingSet4

# G is a tree or a forest.
algorithm = BorieDominatingSet(G)
algorithm.run()
print ( algorithm.dominating_set )
print ( algorithm.cardinality )   # the size of min dset
print ( algorithm.parent )        # DFS tree as a dict

algorithm = TreeDominatingSet(G)   # this is version 2
#algorithm = TreeDominatingSet1(G)
#algorithm = TreeDominatingSet2(G)
algorithm.run()
print ( algorithm.dominating_set )
print ( algorithm.cardinality )   # the size of min dset

# Finding a minimum dominating set and a maximum 2-stable set.
algorithm = TreeDominatingSet3(G)
#algorithm = TreeDominatingSet4(G)
algorithm.run()
print ( algorithm.dominating_set )
print ( algorithm.cardinality )   # the size of min dset
print ( algorithm.two_stable_set )   # a maximum 2-stable set
~~~

## FINDING A MINIMUM INDEPENDENT DOMINATING SET

~~~python
from graphtheory.forests.treeidset import TreeIndependentDominatingSet

# G is a tree or a forest.
algorithm = TreeIndependentDominatingSet(G)
algorithm.run()
print ( algorithm.dominating_set )
print ( algorithm.cardinality )   # the size of minimum independent dset
print ( algorithm.parent )        # DFS tree as a dict
~~~

## FINDING A MINIMUM WEIGHT (INDEPENDENT) DOMINATING SET

~~~python
from graphtheory.forests.treewdset import TreeWeightedDominatingSet
from graphtheory.forests.treewidset import TreeWeightedIndependentDominatingSet

# G is a tree or a forest.
# weight_dict is a dict with pairs (node, weight).
algorithm = TreeWeightedDominatingSet(G, weight_dict)   # version 2
#algorithm = TreeWeightedIndependentDominatingSet(G, weight_dict)
algorithm.run()
print ( algorithm.dominating_set )
print ( algorithm.cardinality )   # the size of minimum independent dset
print ( algorithm.parent )        # DFS tree as a dict
print ( algorithm.weight_dict )
print ( algorithm.dominating_set_weight )
~~~

## FINDING A MINIMUM NODE COVER

~~~python
from graphtheory.forests.treecover import BorieNodeCover
from graphtheory.forests.treecover import TreeNodeCover

algorithm = BorieNodeCover(G)
algorithm.run()
print ( algorithm.node_cover )   # a set with nodes
print ( algorithm.cardinality )   # the size of min cover
print ( algorithm.parent )        # DFS tree as a dict

algorithm = TreeNodeCover(G)
algorithm.run()
print ( algorithm.node_cover )   # a set with nodes
print ( algorithm.cardinality )   # the size of min cover
~~~

## FINDING A MAXIMUM MATCHING

~~~python
from graphtheory.forests.treemate import BorieMatching

algorithm = BorieMatching(G)
algorithm.run()
print ( algorithm.mate )   # a dict with pairs (source, target or None)
print ( algorithm.mate_set )   # a set with edges from max matching
print ( algorithm.cardinality )   # the size of max matching
print ( algorithm.parent )        # DFS tree as a dict
~~~

EOF
