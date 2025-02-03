from collections import deque

def bfs(s) :
    q = deque()
    q.append(s)

    visited = [-1] * (n + 1)
    visited[s] = 0

    while q :
        c = q.popleft()
        for nxt in edges[c] :
            if visited[nxt] == -1 :
                q.append(nxt)
                visited[nxt] = visited[c] + 1

    return visited[1:]

n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]

for _ in range(m) :
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

t = int(input())
distances = [-1] * (n + 1)
distances[1] = 0

for _ in range(t) :
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
    res = bfs(1)
    print(*res)