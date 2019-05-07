#!/usr/bin/python
#
# Kazdy node oznacza pewien sp-graf.
# Liscie to pojedyncze krawedzie, type=edge.
# Node z type=series oznacza wynik polaczenia szeregowego.
# Node z type=parallel oznacza wynik polaczenia rownoleglego.
# Node z type=jackknife oznacza wynik operacji jackknife.

class Node:
    """The class defining a node."""

    def __init__(self, source=None, target=None, type=None, left=None, right=None):
        self.source = source
        self.target = target
        self.type = type   # edge, series, parallel, jackknife
        self.left = left
        self.right = right

    def __str__(self):
        return "Node({0}, {1}, '{2}')".format(self.source, self.target, self.type)


def btree_print(top, level=0):
    if top is None:
        return
    btree_print(top.right, level+1)
    print ( "{0}[{1}]{2}".format('   ' * level, level, top) )
    btree_print(top.left, level+1)


def btree_count(top):
    if top is None:
        return 0
    return btree_count(top.left) + 1 + btree_count(top.right)


def btree_count_iter(top):
    if top is None:
        return 0
    counter = 0
    stack = list()
    stack.append(top)
    while stack:
        node = stack.pop()
        counter += 1
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return counter

# Tworze liste calych wierzcholkow.
def btree_inorder(top):
    if top is None:
        return []
    order = []
    order.extend(btree_inorder(top.left))
    order.append(top)
    order.extend(btree_inorder(top.right))
    return order


def btree_preorder(top):
    if top is None:
        return []
    order = []
    order.append(top)
    order.extend(btree_preorder(top.left))
    order.extend(btree_preorder(top.right))
    return order


def btree_postorder(top):
    if top is None:
        return []
    order = []
    order.extend(btree_postorder(top.left))
    order.extend(btree_postorder(top.right))
    order.append(top)
    return order

# EOF
