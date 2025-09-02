from collections import defaultdict, deque

N, M = map(int, input().split())
edges = defaultdict(list)

for _ in range(N - 1) :
    u, v, w = map(int, input().split())
    edges[u].append((v, w))
    edges[v].append((u, w))

LOG = N.bit_length() + 1
parent = [[0] * (N + 1) for _ in range(LOG)]
depth = [-1] * (N + 1)
dist = [0] * (N + 1)

def build(root=1) :
    # 1] BFS로 depth, dist, parent[0] 채우기
    q = deque()
    q.append(root)
    depth[root] = 0
    parent[0][root] = 0

    while q :
        u = q.popleft()
        for v, w in edges[u] :
            if depth[v] != -1 :
                continue
            depth[v] = depth[u] + 1
            dist[v] = dist[u] + w
            parent[0][v] = u
            q.append(v)

    for k in range(1, LOG) :
        for v in range(1, N + 1) :
            mid = parent[k-1][v]
            parent[k][v] = parent[k-1][mid] if mid else 0

def lift(u, steps) :
    # u를 steps만큼 위로 올리기
    k = 0
    while steps :
        if steps & 1 :
            u = parent[k][u]
        steps >>= 1
        k += 1
    return u

def lca(a, b) :
    if depth[a] < depth[b] :
        a, b = b, a
    # 깊이 맞추기
    a = lift(a, depth[a] - depth[b])
    if a == b :
        return a
    # 위에서부터 같이 올리기
    for k in reversed(range(LOG)) :
        if parent[k][a] != parent[k][b] :
            a = parent[k][a]
            b = parent[k][b]

    return parent[0][a]

def distance(u, v) :
    c = lca(u, v)
    return dist[u] + dist[v] - 2 * dist[c]

build()

for _ in range(M) :
    u, v = map(int, input().split())
    print(distance(u, v))