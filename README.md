# Modified Prims Algorithm Assignment

- CSCI 3302
- DATA STRUCTURES AND ALGORITHMS II SEMESTER I, 2022/23
- Name : Muhammad Ali Asghar Bin Muhammad Nasir ( 1918589 )


| Contents |
| ------- |
| Pseudocode |
| Performance |
| Advantage And Disadvantages |
| When to use which algorithm |
| Code | 



# Pseudocode

Algorithm:

MST-MODIFIED PRIM (G, w, r)
Here, G is an undirected graph, w is the weight of the edges 
of graph G and r is the root node.
Let 16 be infinity here.
V [G] denotes the set of vertices of graph G.
E [G] denotes the set of edges of graph G.
Jet [x] denotes the minimum weight of any edge connecting 
x to the tree.
P [x] denotes the parent of vertex x in the tree.

1. Repeat steps 1 to 3 for every x belongs to V [G]
2. Set Jet [x]:= 16 [Initialize every vertex to Infinity]
3. Set P [x]:= NIL [Initialize parent of every Node to NIL]
4. Extract minimum weight edge [r1, r2] from E [G]
5. Set Jet [r1]:= 0 [Set weight of root node 0]
6. Put this minimum edge [r1, r2] back in E [G]
7. Set Q:= V [G]
8. Repeat steps 8 to 13 while Q is not empty
9. Set x:= EXTRACT-MIN (Q) [Vertex with Minimum Jet value is extracted from Q and Put into x]
10. Repeat steps 10 to13 for each y belongs to Adj [x]
11. If y belongs to Q and w(x, y) < Jet [y]
12. Then Set P [y]:= x
13. Set Jet [y]:= w(x, y)

# Performance (time/space complexity or numerical experiment)

| O (E lg V) |
| --------- |

# Advantage And Disadvantages

Advantages : Slightly better performance in case where minimum weight edge is required from the starting phase of minimum spanning tree formation.

Disadvantages : Not Efficient, will find solution but not necessarily the best solution

# When to use which algorithm

When a spesific root node it required .


# Code Explanation

The code is an implementation of the MST-MODIFIED PRIM algorithm, which is used to find the minimum spanning tree (MST) of an undirected graph. The algorithm starts by initializing two dictionaries, Jet and P, where Jet stores the minimum weight of the edge connecting each vertex to the tree and P stores the parent of each vertex in the tree. The algorithm then extracts the minimum weight edge from the set of edges and sets the root node's weight to 0. The algorithm then puts this minimum edge back into the set of edges and sets Q to be the set of vertices of the graph.

The main part of the algorithm is a while loop that runs until Q is empty. In each iteration, the vertex with the minimum weight is extracted from Q and stored in the variable x. Then, for each vertex y in the adjacency list of x, the algorithm checks if y belongs to Q and if the weight of the edge connecting x to y is less than the current weight of y in Jet. If this condition is true, the parent of y is set to x and the weight of y in Jet is updated to the weight of the edge connecting x to y.

After the while loop ends, Q is empty and the algorithm has found the MST of the graph. The MST is represented by the P and Jet dictionaries, where P stores the parent of each vertex in the tree and Jet stores the minimum weight of the edge connecting each vertex to the tree.

The code uses the heapq library to implement a priority queue, which is used to store the edges and their weights, and also to extract the minimum weight edge from the set of edges.

In addition to the function MST_MODIFIED_PRIM, there is a block of code that defines the dummy input data, calls the function with that data, and displays the output.

The input G is assumed to be an adjacency list representation of the graph where each vertex is a key in a dictionary and the value is a list of edges and their weights. The input w is assumed to be a dictionary containing the weight of each edge as the value, with the vertices as the keys. The input r is the root node. The function returns a tuple containing the parent of each vertex in the tree and the minimum weight of the edge connecting each vertex to the tree.
