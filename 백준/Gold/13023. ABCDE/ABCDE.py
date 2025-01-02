def dfs(c, depth) :
    global res
    visited[c] = 1
    if depth == 5 :
        res = 1
        return
    for nxt in graph[c] :
        if visited[nxt] == 0 :
            dfs(nxt, depth + 1)
    visited[c] = 0

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N)]

for a, b in arr :
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * N

res = 0

for i in range(N) :
    dfs(i, 1)
    if res :
        break

print(res)