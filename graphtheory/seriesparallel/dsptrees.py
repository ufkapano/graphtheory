#!/usr/bin/env python3
#
# Budowanie przypadkowych dsp-grafow w postaci dsp-tree.
# Rozpoznawanie dsp-grafow i budowa dsp-tree.

import random
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.seriesparallel.spnodes import Node
from graphtheory.seriesparallel.spnodes import btree_print2
from graphtheory.seriesparallel.spnodes import btree_postorder
from graphtheory.seriesparallel.spnodes import btree_count
from graphtheory.seriesparallel.spnodes import btree_count_iter
from graphtheory.seriesparallel.dsptools import make_random_dspgraph


def swap(L, i, j):
    """Swap items on the list."""
    L[i], L[j] = L[j], L[i]


def make_random_dsptree(n):
    """Make a random dsp-tree with n vertices."""
    if n < 2:
        raise ValueError("bad n")
    source = 0
    sink = n-1
    root = Node(source, sink, "edge")
    tnode_list = [root]   # na tej liscie maja byc type=edge
    node = n-2
    while node > 0:
        # Losowanie krawedzi na ktorej bedzie operacja.
        i = random.randrange(0, len(tnode_list))
        swap(tnode_list, i, -1)
        tnode = tnode_list.pop()
        # Losowanie operacji.
        action = random.choice(("series", "parallel"))
        #print("action {}".format(action))
        if action == "series":
            tnode.type = "series"
            tnode.left = Node(tnode.source, node, "edge")
            tnode.right = Node(node, tnode.target, "edge")
            tnode_list.append(tnode.left)
            tnode_list.append(tnode.right)
        elif action == "parallel":
            tnode.type = "parallel"
            tnode.left = Node(tnode.source, tnode.target, "edge")
            tnode.right = Node(tnode.source, tnode.target, "series")
            tnode.right.left = Node(tnode.source, node, "edge")
            tnode.right.right = Node(node, tnode.target, "edge")
            tnode_list.append(tnode.left)
            tnode_list.append(tnode.right.left)
            tnode_list.append(tnode.right.right)
        else:
            raise ValueError("bad action")
        node -= 1
        assert all(tnode.type == "edge" for tnode in tnode_list)
    return root


def find_dsptree(graph):
    """Find an sp-tree for an sp-graph."""
    if not graph.is_directed():
        raise ValueError("the graph is undirected")
    graph_copy = graph.copy()
    degree11 = set(node for node in graph.iternodes()
        if graph.indegree(node) == 1 and graph.outdegree(node) == 1)
        # active nodes with indegree=1 and outdegree=1
    #print "degree11", degree11
    call_stack = []
    tnode_dict = dict()   # tnode dla krawedzi
    # Etap I. Redukcja grafu do krawedzi.
    # Dopoki sa wierzcholki wykonuj odrywanie.
    while degree11:
        source = degree11.pop()
        if graph_copy.indegree(source) != 1:
            # Czasem stopien wierzcholka moze sie zmniejszyc!
            #print ("indegree != 1 for", source)
            continue
        if graph_copy.outdegree(source) != 1:
            # Czasem stopien wierzcholka moze sie zmniejszyc!
            #print ("outdegree != 1 for", source)
            continue
        #print ("source", source)
        for edge in graph_copy.iterinedges(source):
            node1 = edge.source   # tylko jedna
        for edge in graph_copy.iteroutedges(source):
            node2 = edge.target   # tylko jedna
        edge = Edge(node1, node2)
        if graph_copy.has_edge(edge):
            # Jezeli ma krawedz, to trzeba poprawic stopnie wierzcholkow,
            # bo przy usuwaniu krawedzi przy node1 zmniejsza sie outdegree,
            # a przy node2 zmniejsza sie indegree.
            if graph_copy.outdegree(node1) == 2 and graph_copy.indegree(node1) == 1:
                degree11.add(node1)
                #print "degree11 add", node1
            if graph_copy.outdegree(node2) == 1 and graph_copy.indegree(node2) == 2:
                degree11.add(node2)
                #print "degree11 add", node2
            call_stack.append(("parallel", source, node1, node2))
        else:   # tu nie trzeba poprawiac stopni
            graph_copy.add_edge(edge)
            call_stack.append(("series", source, node1, node2))
        # Usuwamy krawedzie z source.
        graph_copy.del_edge(Edge(node1, source))
        graph_copy.del_edge(Edge(source, node2))
    # Etap II. Sprawdzamy co zostalo. Ma zostac jedna krawedz.
    if graph_copy.e() == 1:
        # Zostala jedna krawedz.
        #for edge in graph_copy.iteredges():
        #    print "edge", edge
        edge = next(graph_copy.iteredges())
        root = Node(edge.source, edge.target, "edge")
        tnode_dict[(edge.source, edge.target)] = root
    else:
        raise ValueError("not an sp-graph, e() != 1")
    # Etap III. Budowa sp-tree na bazie call_stack.
    while call_stack:
        action, node, node1, node2 = call_stack.pop()
        if (node1, node2) in tnode_dict:
            tnode = tnode_dict[(node1, node2)]
        else:
            raise ValueError("key not in tnode_dict")
        #print "action", action
        if action == "series":
            del tnode_dict[(tnode.source, tnode.target)]
            tnode.type = "series"
            tnode.left = Node(tnode.source, node, "edge")
            tnode.right = Node(node, tnode.target, "edge")
            tnode_dict[(tnode.source, node)] = tnode.left
            tnode_dict[(node, tnode.target)] = tnode.right
        elif action == "parallel":
            #del tnode_dict[(tnode.source, tnode.target)]   # nadpisuje
            tnode.type = "parallel"
            tnode.left = Node(tnode.source, tnode.target, "edge")
            tnode.right = Node(tnode.source, tnode.target, "series")
            tnode.right.left = Node(tnode.source, node, "edge")
            tnode.right.right = Node(node, tnode.target, "edge")
            tnode_dict[(tnode.source, tnode.target)] = tnode.left
            tnode_dict[(tnode.source, node)] = tnode.right.left
            tnode_dict[(node, tnode.target)] = tnode.right.right
        else:
            raise ValueError("bad action")
        assert all(tnode_dict[key].type == "edge" for key in tnode_dict)
    return root


if __name__ == "__main__":

    V = 10
    print ("Generate random dsp-tree ...")
    root = make_random_dsptree(V)
    print ("btree_count", btree_count(root))
    print ("btree_count_iter", btree_count_iter(root))
    print ("btree_print ...")
    #btree_print(root)
    print ("btree_postorder ...")
    #for tnode in btree_postorder(root):
    #    print (tnode)

    print ("Finding dsp-tree ...")
    G = make_random_dspgraph(V)
    G.show()
    root = find_dsptree(G)
    print ("btree_print ...")
    #btree_print(root)
    #for tnode in btree_postorder(root):
    #    print (tnode)

    print ("Testing bad dsp-graph")
    # 0--o3
    # |  o|
    # | / |
    # o/  o
    # 1--o2
    N = 4
    G = Graph(N, True)
    for node in range(N):
        G.add_node(node)
    edge_list = [Edge(0, 1), Edge(0, 3), Edge(1, 2), Edge(3, 2), Edge(1, 3)]
    for edge in edge_list:
        G.add_edge(edge)
    G.show()
    #root = find_dsptree(G)   # ValueError: not an sp-graph, e() != 1
    G.del_edge(Edge(1, 3))
    G.add_edge(Edge(0, 2))
    root = find_dsptree(G)   # s=0, t=2
    print ("btree_print ...")
    btree_print2(root)

# EOF
