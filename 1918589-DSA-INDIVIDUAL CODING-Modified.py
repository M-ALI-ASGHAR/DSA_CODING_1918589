""" Name:Muhammad Ali Asghar Bin Muhammad Nasir
    Id  :1918589                                  Finish at 22/1 6.15 p.m  """

import heapq


def MST_MODIFIED_PRIM(G, w, r):
    # Initialize infinity and set of vertices and edges of graph G
    INF = float('inf')
    V = G.keys()  # set of vertices of graph G
    E = []
    # create edges with weight, v, u format
    for v in V:
        for u, weight in G[v]:
            E.append((weight, v, u))
    # Initialize every vertex's Jet value to infinity and parent to NIL
    Jet = {v: INF for v in V}  # minimum weight of any edge connecting v to the tree
    P = {v: None for v in V}  # parent of vertex v in the tree
    Jet[r] = 0
    heapq.heapify(E)            # Convert the list to a heap
    Q = set(V)
    while Q:
        _, x, y = heapq.heappop(E)
        if y not in Q:
            continue
        Q.remove(y)
        P[y] = x
        Jet[y] = w[x][y]
        for u, weight in G[y]:
            if u in Q and weight < Jet[u]:
                Jet[u] = weight
                heapq.heappush(E, (weight, y, u))
    return P, Jet


# Test if the code is working
if __name__ == "__main__":
    # Dummy input data
G = {
        'A': [('B', 4), ('C', 3), ('D', 7)],
        'B': [('A', 4), ('C', 6), ('D', 2)],
        'C': [('A', 3), ('B', 6), ('D', 5)],
        'D': [('A', 7), ('B', 2), ('C', 5)]
    }
    w = {
        'A': {'B': 4, 'C': 3, 'D': 7},
        'B': {'A': 4, 'C': 6, 'D': 2},
        'C': {'A': 3, 'B': 6, 'D': 5},
        'D': {'A': 7, 'B': 2, 'C': 5}
    }
    r = 'A'
    P, Jet = MST_MODIFIED_PRIM(G, w, r)
    print("Parent of each vertex:", P)
    print("Minimum weight of each vertex:", Jet)
