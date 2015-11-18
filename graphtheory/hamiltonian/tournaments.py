#!/usr/bin/python

from graphtheory.structures.edges import Edge


def is_transitive(graph):
    """Test if the tournament is transitive in O(V) time."""
    if not graph.is_directed():
        raise ValueError("the graph is not directed")
    node_list = [None] * graph.v()
    # Calculate outdegrees - different numbers are expected.
    for node in graph.iternodes():
        node_list[graph.outdegree(node)] = node
    return all(item is not None for item in node_list)


def find_hamiltonian_path(graph):
    """Find a Hamiltonian path in a tournament."""
    if not graph.is_directed():
        raise ValueError("the graph is not directed")
    return sorted(graph.iternodes(), cmp=lambda x, y:
        -1 if graph.has_edge(Edge(x, y)) else 1)

# EOF
