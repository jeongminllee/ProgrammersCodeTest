def find(v) :
    if v != parents[v] :
        parents[v] = find(parents[v])

    return parents[v]

def union(v1, v2) :
    if v1 > v2 :
        parents[v2] = v1
    else :
        parents[v1] = v2


V, E = map(int, input().split())
parents = [v for v in range(V + 1)]
edges = []

for _ in range(E) :
    v1, v2, w = map(int, input().split())
    edges.append([w, v1, v2])

edges.sort()
sum_weight = 0

for w, v1, v2 in edges :
    v1_root = find(v1)
    v2_root = find(v2)

    if v1_root != v2_root :
        union(v1_root, v2_root)
        sum_weight += w

print(sum_weight)