def dfs(s) :
    stack = []
    stack.append(s)

    cnt = 1
    while stack :
        node = stack.pop()
        if not visited[node] :
            visited[node] = cnt
            cnt += 1
            stack += sorted(graph[node], reverse=True)
            
N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(R)

for n in range(1, N + 1) :
    print(visited[n])