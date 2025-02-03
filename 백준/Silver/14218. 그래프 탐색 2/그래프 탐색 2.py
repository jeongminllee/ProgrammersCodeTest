from collections import deque

def bfs(s) :
    queue = deque()
    queue.append(s)

    visited = [-1] * (n + 1)

    while queue :
        node, path = queue.popleft()
        if distances[node] > path :
            distances[node] = path
        visited[node] = 1
        for i in range(len(edges[node])) :
            if edges[node][i] == 1 and visited[i] == -1 :
                queue.append([i, path + 1])
                visited[i] = 1

INF = 1001
n, m = map(int, input().split())
edges = [[0] * (n + 1) for _ in range(n+1)]
distances = [INF] * (n + 1)
distances[1] = 0

for _ in range(m) :
    u, v = map(int, input().split())
    edges[u][v] = 1
    edges[v][u] = 1

q = int(input())
for _ in range(q) :
    i, j = map(int, input().split())
    edges[i][j] = 1
    edges[j][i] = 1
    bfs([1, 0])
    for i in range(1, n + 1) :
        if distances[i] == INF :
            print(-1, end=' ')
        else :
            print(distances[i], end=' ')
    print()