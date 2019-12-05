# graphtheory package

Python implementation of graph data structures and algorithms is presented. 
The minimal graph interface is defined together with several 
classes implementing this interface. 
Graph nodes can be any hashable Python objects. 
Directed edges are instances of the Edge class. 
Graphs are instances of the Graph class (several versions).
Multigraphs are instances of the MultiGraph class.
Many algorithms are implemented using a unified approach. 
There are separate classes and modules devoted to different algorithms.
The graphtheory package is written with Python 2.7 and Python 3.2.

## Problems and algorithms

* Cycle detection, topological sorting (DFS, Kahn), 
transitive closure (matrix multiplication, Floyd-Warshall, BFS, DFS)
* Bipartiteness: bipartite graphs detection (BFS, DFS), 
maximum-cardinality matching (Hopcroft-Karp, Ford-Fulkerson)
* Matching: heuristics (greedy for a maximal cardinality matching,
greedy for a minimum weight matching)


## References

[1] A. Kapanowski and Ł. Gałuszka, *Weighted graph algorithms with Python*. 
http://arxiv.org/abs/1504.07828 [draft]

A. Kapanowski and Ł. Gałuszka, *Weighted graph algorithms with Python*. 
The Python Papers 11, 3 (2016). 
http://ojs.pythonpapers.org/index.php/tpp/article/view/270 [final version]

[2] A. Kapanowski and A. Krawczyk, *Halin graphs are 3-vertex-colorable except even wheels*.
https://arxiv.org/abs/1903.02904

## Contributors

Andrzej Kapanowski (project leader)

Łukasz Gałuszka (MST, shortest paths, flows)

Łukasz Malinowski (matching, Eulerian graphs, graph coloring, bipartite graphs)

Paweł Motyl (multigraphs, graph coloring, independent sets)

Piotr Szestało (Hamiltonian graphs, TSP, tournaments)

Kacper Dziubek (planarity testing)

Sandra Pażyniowska (graph drawing)

Wojciech Sarka (dominating sets)

Igor Samson (graph coloring)

Dariusz Zdybski (cliques)

Aleksander Krawczyk (Halin graphs, wheel graphs)

Małgorzata Olak (chordal graphs)

Krzysztof Niedzielski (matching)

Konrad Gałuszka (series-parallel graphs)

Maciej Niezabitowski (tree decomposition)

Piotr Wlazło (edge coloring)

Magdalena Stępień (planar graphs)

EOF
