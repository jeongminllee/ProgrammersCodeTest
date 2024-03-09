import heapq

def dijkstra(graph, start) :
    distances = {node : float('inf') for node in range(1, len(graph) + 1)}
    distances[start] = 0
    q = []
    heapq.heappush(q, [distances[start], start])

    while q:
        current_distance, current_node = heapq.heappop(q)

        if distances[current_node] < current_distance :
            continue

        for adj, weight in graph[current_node].items() :
            distance = current_distance + weight

            if distance < distances[adj] :
                distances[adj] = distance
                heapq.heappush(q, [distance, adj])
    return distances

n, m, x = map(int, input().split())
graph = {node:{} for node in range(1, n + 1)}
r_graph = {node:{} for node in range(1, n + 1)}

for _ in range(m) :
    s, e, t = map(int, input().split())
    graph[s][e] = t
    r_graph[e][s] = t

to_x = dijkstra(graph, x)
from_x = dijkstra(r_graph, x)

ans = 0
for i in range(1, n + 1) :
    ans = max(ans, to_x[i] + from_x[i])

print(ans)