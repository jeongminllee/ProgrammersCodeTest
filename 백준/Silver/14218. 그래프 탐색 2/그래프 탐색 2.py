from collections import deque

def bfs(s) :
    q = deque()
    q.append(s)
    distances = [-1] * (n + 1)
    distances[s] = 0

    while q :
        c = q.popleft()

        for nxt in edges[c] :
            dist = distances[c] + 1
            if distances[nxt] == -1 :
                distances[nxt] = dist
                q.append(nxt)

    return distances[1:]


n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]
for _ in range(m) :
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

bridges = int(input())
for _ in range(bridges) :
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)
    res = bfs(s=1)
    print(*res)
