#!/usr/bin/env python3

import json
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
#from graphtheory.structures.dictgraphs import Graph
#from graphtheory.structures.setgraphs import Graph   # weights are ignored
from graphtheory.structures.multigraphs import MultiGraph

def dumps_graph(graph):
    """Convert the graph or the multigraph to a JSON string."""
    D = dict()
    D['directed'] = graph.is_directed()
    D['multigraph'] = isinstance(graph, MultiGraph)
    D['nodes'] = [{'id': node} for node in graph.iternodes()]
    D['edges'] = [edge.__dict__ for edge in graph.iteredges()]
    # NetworkX uses 'links'.
    #print(D)
    return json.dumps(D, indent=2)

def dump_graph(graph, file_name):
    """Convert the graph or the multigraph to a JSON string."""
    D = dict()
    D['directed'] = graph.is_directed()
    D['multigraph'] = isinstance(graph, MultiGraph)
    D['nodes'] = [{'id': node} for node in graph.iternodes()]
    D['edges'] = [edge.__dict__ for edge in graph.iteredges()]
    # NetworkX uses 'links'.
    #print(D)
    with open(file_name, mode='w') as outfile:
        json.dump(D, outfile, indent=2)

def loads_graph(json_string):
    """Convert a JSON string to a graph or a multigraph."""
    D = json.loads(json_string)
    if D['multigraph']:
        graph = MultiGraph(n=len(D['nodes']), directed=D['directed'])
    else:
        graph = Graph(n=len(D['nodes']), directed=D['directed'])
    for d in D['nodes']:
        graph.add_node(d['id'])
    for d in D['edges']:   # NetworkX uses 'links'.
        graph.add_edge(Edge(**d))
    return graph

def load_graph(file_name):
    """Convert a JSON string to a graph or a multigraph."""
    with open(file_name, mode='r') as infile:
        D = json.load(infile)
    if D['multigraph']:
        graph = MultiGraph(n=len(D['nodes']), directed=D['directed'])
    else:
        graph = Graph(n=len(D['nodes']), directed=D['directed'])
    for d in D['nodes']:
        graph.add_node(d['id'])
    for d in D['edges']:    # NetworkX uses 'links'.
        graph.add_edge(Edge(**d))
    return graph

G1 = Graph()
for edge in [Edge("A", "B"), Edge("B", "C", 2)]:
    G1.add_edge(edge)

G2 = Graph(directed=True)
for edge in [Edge("A", "B"), Edge("B", "C", 2)]:
    G2.add_edge(edge)

G3 = MultiGraph()
for edge in [Edge("A", "B"), Edge("B", "C", 2), Edge("B", "C", 3)]:
    G3.add_edge(edge)

G4 = MultiGraph(directed=True)
for edge in [Edge("A", "B"), Edge("B", "C", 2), Edge("B", "C", 3)]:
    G4.add_edge(edge)

G = G2

word = dumps_graph(G)
print(word)
H = loads_graph(word)
assert G == H

#dump_graph(G, "json1graph.json")
#H = load_graph("json1graph.json")
#assert G == H

# EOF
