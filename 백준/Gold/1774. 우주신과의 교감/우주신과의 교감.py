def find(parent, a) :
    if a != parent[a] :
        parent[a] = find(parent, parent[a])

    return parent[a]

def union(parent, a, b) :
    a = find(parent,a)
    b = find(parent,b)

    if a < b :
        parent[b] = a
    else :
        parent[a] = b

def get_dist(loc1, loc2) :
    x1, y1, x2, y2 = loc1[0], loc1[1], loc2[0], loc2[1]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

N, M = map(int, input().split())    # 우주신들 개수, 연결된 통로 개수
parent = list(range(N+1))

edges = [[-1, -1]]
for i in range(1, N+1) :
    edges.append(list(map(int, input().split())))

for _ in range(M) :
    a, b = map(int, input().split())
    union(parent, a, b)

possible = []
for i in range(1, len(edges)-1) :
    for j in range(i+1, len(edges)) :
        possible.append([get_dist(edges[i], edges[j]), i, j])

possible.sort()
res = 0

for p in possible :
    cost, x, y = p

    if find(parent, x) != find(parent, y) :
        union(parent, x, y)
        res += cost

print(f"{res:.2f}")