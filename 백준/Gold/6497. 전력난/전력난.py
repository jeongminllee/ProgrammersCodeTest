def sol_6497(m, n) :
    edges = []
    total = 0

    for _ in range(n) :
        x, y, z = map(int, input().split())
        total += z
        edges.append((z, x, y))

    # Kruskal : sort edges by weight
    edges.sort()

    # DSU (Union-Find)
    parent = list(range(m))
    rank = [0] * m

    def find(a) :
        while a != parent[a] :
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b) :
        fa, fb = find(a), find(b)
        if fa == fb :
            return False
        if rank[fa] < rank[fb] :
            parent[fa] = fb
        elif rank[fa] > rank[fb] :
            parent[fb] = fa
        else :
            parent[fb] = fa
            rank[fa] += 1
        return True

    mst = 0
    picked = 0
    for w, u, v in edges :
        if union(u, v) :
            mst += w
            picked += 1
            if picked == m - 1 :
                break

    print(total - mst)
        

while True :
    m, n = map(int, input().split())
    if (m, n) == (0, 0) :
        break
    else :
        sol_6497(m, n)