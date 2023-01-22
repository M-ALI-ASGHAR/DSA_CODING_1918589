import heapq

def MST_MODIFIED_PRIM(G, w, r):
    INF = float('inf')
    V = G.keys() # set of vertices of graph G
    E = []
    for v in V:
        for u, weight in G[v]:
            E.append((weight, v, u))
    Jet = {v: INF for v in V} # minimum weight of any edge connecting v to the tree
    P = {v: None for v in V} # parent of vertex v in the tree
    Jet[r] = 0
    heapq.heapify(E)
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

if __name__ == "__main__":
    # Dummy input data
    G = {
        'A': [('B', 2), ('C', 3)],
        'B': [('A', 2), ('C', 1), ('D', 4)],
        'C': [('A', 3), ('B', 1), ('D', 5)],
        'D': [('B', 4), ('C', 5)]
    }
    w = {
        'A': {'B': 2, 'C': 3},
        'B': {'A': 2, 'C': 1, 'D': 4},
        'C': {'A': 3, 'B': 1, 'D': 5},
        'D': {'B': 4, 'C': 5}
    }
    r = 'A'
    P, Jet = MST_MODIFIED_PRIM(G, w, r)
    print("Parent of each vertex:", P)
    print("Minimum weight of each vertex:", Jet)