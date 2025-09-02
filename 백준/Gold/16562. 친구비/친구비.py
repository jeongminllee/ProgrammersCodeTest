def find(a) :
    if parent[a] == a :
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b) :
    a, b = find(a), find(b)
    if a == b :
        return

    if costs[a] < costs[b] :
        parent[b] = a
    else :
        parent[a] = b

# 입력사항
N, M, K = map(int, input().split())
costs = [0] + list(map(int, input().split()))
parent = list(range(N + 1))

for _ in range(M) :
    a, b = map(int, input().split())
    union(a, b)

res = 0
for i in range(1, N + 1) :
    if find(i) == i :
        res += costs[i]

print(res if res <= K else "Oh no")