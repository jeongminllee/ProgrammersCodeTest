from collections import defaultdict, deque

N, M = map(int, input().split())
edges = defaultdict(list)
for _ in range(N - 1) :
    u, v, dist = map(int, input().split())
    edges[u].append((v, dist))
    edges[v].append((u, dist))

for _ in range(M) :
    start, end = map(int, input().split())

    q = deque()
    visited = [1e9] * (N + 1)

    q.append(start)
    visited[start] = 0

    while q :
        curr = q.popleft()
        if curr == end :
            print(visited[end])
            break
        for nxt in edges[curr] :
            nxt_node, nxt_dist = nxt
            if visited[nxt_node] > visited[curr] + nxt_dist  :
                q.append(nxt_node)
                visited[nxt_node] = visited[curr] + nxt_dist