#!/usr/bin/python
#
# Budowanie przypadkowych sp-grafow w postaci sp-tree.
# Rozpoznawanie sp-grafow i budowa sp-tree.
# Wersje funkcji do importu.

import random
from graphtheory.structures.edges import Edge
from graphtheory.seriesparallel.spnodes import Node
from graphtheory.seriesparallel.spnodes import btree_print
from graphtheory.seriesparallel.spnodes import btree_postorder
from graphtheory.seriesparallel.spnodes import btree_count
from graphtheory.seriesparallel.spnodes import btree_count_iter


def swap(L, i, j):
    """Swap items on the list."""
    L[i], L[j] = L[j], L[i]


def make_random_sptree(n):
    """Make a random sp-tree with n vertices."""
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
        if tnode.target == sink:
            action = random.choice(["series", "parallel", "jackknife"])
        else:
            action = random.choice(["series", "parallel"])
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
        elif action == "jackknife":
            tnode.type = "jackknife"
            tnode.left = Node(tnode.source, tnode.target, "edge")
            tnode.right = Node(tnode.target, node, "edge")
            tnode_list.append(tnode.left)
            tnode_list.append(tnode.right)
        else:
            raise ValueError("bad action")
        node -= 1
    return root


def find_sptree(graph):
    """Find an sp-tree for an sp-graph."""
    if graph.is_directed():
        raise ValueError("the graph is directed")
    graph_copy = graph.copy()
    degree2 = set(node for node in graph.iternodes()
        if graph.degree(node) == 2)   # active nodes with degree 2
    call_stack = []
    tnode_dict = dict()
    # Etap I. Redukcja grafu do krawedzi lub gwiazdy.
    # Dopoki sa wierzcholki stopnia 2 wykonuj odrywanie.
    while degree2:
        source = degree2.pop()
        if graph_copy.degree(source) != 2:
            # Czasem stopien wierzcholka moze sie zmniejszyc!
            continue
        node1, node2 = tuple(graph_copy.iteradjacent(source))
        edge = Edge(node1, node2)
        if graph_copy.has_edge(edge):
            # Jezeli ma krawedz, to trzeba poprawic stopnie wierzcholkow,
            # bo przy usuwaniu krawedzi przy source zmniejsza sie stopnie.
            if graph_copy.degree(node1) == 3:
                degree2.add(node1)
            if graph_copy.degree(node2) == 3:
                degree2.add(node2)
            call_stack.append(("parallel", source, node1, node2))
        else:   # tu nie trzeba poprawiac stopni
            graph_copy.add_edge(edge)
            call_stack.append(("series", source, node1, node2))
        # Usuwamy krawedzie z source.
        graph_copy.del_edge(Edge(source, node1))
        graph_copy.del_edge(Edge(source, node2))
    # Etap II. Sprawdzamy co zostalo.
    degree1 = set(node for node in graph_copy.iternodes()
        if graph_copy.degree(node) == 1)
    if len(degree1) == 2 and len(call_stack) + 2 == graph.v():
        # Zostala jedna krawedz, dodajemy konce do PEO.
        node1 = degree1.pop()
        node2 = degree1.pop()
        root = Node(node1, node2, "edge")
        tnode_dict[(node1, node2)] = root
    elif len(call_stack) + len(degree1) + 1 == graph.v():
        # Zostala gwiazda, jest jackknife.
        # Szukam centrum gwiazdy.
        for node in graph_copy.iternodes():
            deg = graph_copy.degree(node)
            if deg > 1:
                if deg == len(degree1):
                    sink = node   #  centum gwiazdy
                    break
                else:
                    raise ValueError("not an sp-graph")
        # Trzeba ustalic jedno ramie jako koniec, w parze do centrum.
        source = degree1.pop()
        while degree1:
            call_stack.append(("jackknife", degree1.pop(), source, sink))
        root = Node(source, sink, "edge")
        tnode_dict[(source, sink)] = root
    else:
        raise ValueError("not an sp-graph")
    # Etap III. Budowa sp-tree na bazie call_stack.
    while call_stack:
        action, node, node1, node2 = call_stack.pop()
        if (node1, node2) in tnode_dict:
            tnode = tnode_dict[(node1, node2)]
        elif (node2, node1) in tnode_dict:
            tnode = tnode_dict[(node2, node1)]
        else:
            raise ValueError("key not in tnode_dict")
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
        elif action == "jackknife":
            #del tnode_dict[(tnode.source, tnode.target)]   # nadpisuje
            tnode.type = "jackknife"
            tnode.left = Node(tnode.source, tnode.target, "edge")
            tnode.right = Node(tnode.target, node, "edge")
            tnode_dict[(tnode.source, tnode.target)] = tnode.left
            tnode_dict[(tnode.target, node)] = tnode.right
        else:
            raise ValueError("bad action")
        #assert all(tnode_dict[key].type == "edge" for key in tnode_dict)
    return root

# EOF
