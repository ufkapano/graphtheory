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

## Problems and algorithms

* Connectivity: connected components, strongly connected components,
cut nodes, cut edges (bridges)
* Cycle detection, topological sorting (DFS, Kahn), 
transitive closure (matrix multiplication, Floyd-Warshall, BFS, DFS)
* Bipartiteness: bipartite graphs detection (BFS, DFS), 
maximum-cardinality matching (Hopcroft-Karp, Ford-Fulkerson)
* Matching: heuristics (greedy for a maximal cardinality matching,
greedy for a minimum weight matching)
* Vertex coloring: sequential (US, RS, CS),
Brooks' theorem (Delta colors),
m-coloring (backtracking, exact),
counter method (exact),
LF, SLF, RLF, SL, GIS
* Edge coloring: with the line graph (using vertex coloring), 
sequential (US, RS, CS), 
NTL (using Delta or Delta+1 colors),
complete graphs (exact),
bipartite graphs (exact)
* Independent sets: backtracking (exact), US, RS, LL, SF
* Dominating sets: backtracking (exact), hybrid (exact), US, RS, LF
* Vertex covers (heuristics): greedy, 2-approximation, LF
* Minimum spanning trees (weighted undirected graphs): 
Boruvka, Prim, Kruskal
* Single-source shortest paths (weighted directed graphs without negative cycles): 
Dijkstra (nonnegative weights), DAGs (using topological sorting), 
Bellman-Ford
* All-pairs shortest paths (weighted directed graphs without negative cycles): 
Floyd-Warshall, Johnson, matrix multiplications
* Eulerian graphs: DFS, Fleury, Hierholzer
* Hamiltonian graphs: DFS, tournaments, 
TSP (DFS, with MST, NN, RNN, sorted edges)
* Forests (exact algorithms): iset, dset, vertex cover, matching, 
tree center, longest path problem, plotting
* Series-parallel graphs (exact algorithms): recognition, generators,
iset, dset, vertex cover, matching, 
chordal completion (PEO), vertex coloring
* Halin graphs (exact algorithms): recognition, generators, vertex coloring,
chordal completion (PEO), tree decomposition, plotting
* Chordal graphs (exact algorithms): recognition, generators, 
finding PEO (MCS), 
finding maximum clique (PEO, MDO),
finding all maximal cliques (PEO),
finding maximum independent set (PEO),
finding tree decomposition (TD),
finding minimum dominating set (TD),
finding minimum node cover (TD)
* Interval graphs: double perm representation, generators, 
traversing (BFS, DFS),
finding path decomposition
* Outerplanar graphs (exact algorithms): recognition, 
chordal completion (PEO), vertex coloring
* Permutation graphs: generators, 
traversing (BFS, DFS) O(n^2), 
connectivity O(n)
* Circle graphs: double perm representation, generators, 
traversing (BFS, DFS) O(n^2),
connectivity O(n^2)
* Clustering: Kruskal

## Download

To install an official release do

    python3 -m pip install graphtheory

To get the git version do

    git clone https://github.com/ufkapano/graphtheory.git

## Usage

See doc/quickstart.txt and other doc/*.txt files.

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

Sandra Rudnicka (outerplanar graphs)

Albert Surmacz (permutation graphs, circle graphs)

Maciej Mularski (interval graphs)

Angelika Siwek (AT-free graphs)

Honorata Zych (chordal completion)

EOF
