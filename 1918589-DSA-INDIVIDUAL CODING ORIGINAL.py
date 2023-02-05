import math

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

def MST_PRIM(G, w, r):
    V = G.keys() # set of vertices of graph G
    Jet = {v: math.inf for v in V} # minimum weight of any edge connecting v to the tree
    P = {v: None for v in V} # parent of vertex v in the tree
    Jet[r] = 0
    Q = set(V)
    while Q:
        u = min(Q, key=lambda x: Jet[x])
        Q.remove(u)
        for v, weight in G[u]:
            if v in Q and weight < Jet[v]:
                Jet[v] = weight
                P[v] = u
    return P, Jet

if __name__ == "__main__":
    r = 'A'
    P, Jet = MST_PRIM(G, w, r)
    print("Parent of each vertex:", P)
    print("Minimum weight of each vertex:", Jet)