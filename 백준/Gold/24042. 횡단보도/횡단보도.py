from collections import defaultdict
import heapq

def dejkstra(start) :
    q = []
    heapq.heappush(q, (0, start))
    visited = [float('inf')] * (N + 1)
    visited[start] = 0

    while q :
        time, node = heapq.heappop(q)
        if node == N :
            return time
        if visited[node] < time :
            continue
        for i, nxt_node in edges[node] :
            nxt_time = i + ((time - i) // M) * M if (time-i) % M == 0 else i + ((time - i) // M + 1) * M
            if visited[nxt_node] > nxt_time + 1 :
                visited[nxt_node] = nxt_time + 1
                heapq.heappush(q, (nxt_time + 1, nxt_node))
                
N, M = map(int, input().split())
edges = defaultdict(list)
for i in range(M) :
    a, b = map(int, input().split())
    edges[a].append((i, b))
    edges[b].append((i, a))

print(dejkstra(1))