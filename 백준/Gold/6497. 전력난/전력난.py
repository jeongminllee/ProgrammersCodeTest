import sys
input = sys.stdin.readline

def sol_6497(m, n) :
    edges = []

    for _ in range(n) :
        x, y, z = map(int, input().split())
        edges.append((z, x, y))

    # Kruskal : sort edges by weight
    edges.sort()

    # DSU (Union-Find)
    parent = list(range(m))

    def find(a) :
        if a != parent[a] :
            parent[a] = find(parent[a])
        return parent[a]

    def union(a, b) :
        fa, fb = find(a), find(b)
        if fa > fb :
            parent[fa] = parent[fb]
        else :
            parent[fb] = parent[fa]

    mst = 0
    for w, u, v in edges :
        if find(u) == find(v) :
            mst += w
            continue
        union(u, v)

    print(mst)
        

while True :
    m, n = map(int, input().split())
    if (m, n) == (0, 0) :
        break
    else :
        sol_6497(m, n)