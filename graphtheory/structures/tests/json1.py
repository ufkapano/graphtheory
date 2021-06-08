#!/usr/bin/python

import json
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.structures.multigraphs import MultiGraph

def dumps_graph(graph):
    """Convert the graph or the multigraph to a JSON string."""
    D = dict()
    D['directed'] = graph.is_directed()
    D['multigraph'] = isinstance(graph, MultiGraph)
    D['nodes'] = [{'id': node} for node in graph.iternodes()]
    D['edges'] = [edge.__dict__ for edge in graph.iteredges()]
    #print(D)
    return json.dumps(D, indent=2)

def dump_graph(graph, file_name):
    """Convert the graph or the multigraph to a JSON string."""
    D = dict()
    D['directed'] = graph.is_directed()
    D['multigraph'] = isinstance(graph, MultiGraph)
    D['nodes'] = [{'id': node} for node in graph.iternodes()]
    D['edges'] = [edge.__dict__ for edge in graph.iteredges()]
    #print(D)
    with open(file_name, mode='w') as outfile:
        json.dump(D, outfile, indent=2)

def loads_graph(json_string):
    """Convert a JSON string to a graph or a multigraph."""
    D = json.loads(json_string)
    if D['multigraph']:
        graph = MultiGraph(directed=D['directed'])
    else:
        graph = Graph(directed=D['directed'])
    for d in D['nodes']:
        graph.add_node(d['id'])
    for d in D['edges']:
        graph.add_edge(Edge(**d))
    return graph

def load_graph(file_name):
    """Convert a JSON string to a graph or a multigraph."""
    with open(file_name, mode='r') as infile:
        D = json.load(infile)
    if D['multigraph']:
        graph = MultiGraph(directed=D['directed'])
    else:
        graph = Graph(directed=D['directed'])
    for d in D['nodes']:
        graph.add_node(d['id'])
    for d in D['edges']:
        graph.add_edge(Edge(**d))
    return graph

G = Graph()
#G = Graph(directed=True)
#G = MultiGraph()
#G = MultiGraph(directed=True)

G.add_edge(Edge("A", "B"))
G.add_edge(Edge("B", "C", 2))

word = dumps_graph(G)
print(word)
H = loads_graph(word)
assert G == H

#dump_graph(G, "json1graph.json")
#H = load_graph("json1graph.json")
#assert G == H

# EOF
