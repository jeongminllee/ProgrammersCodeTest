import heapq

INF = float('inf')

def deijkstra(start) :
    distances[start] = 0
    q = []
    heapq.heappush(q, (start, 0))

    while q:
        node, weight = heapq.heappop(q)

        if weight > distances[node] :
            continue

        for nxt_node, nxt_weight in edges[node] :
            if distances[nxt_node] > nxt_weight + weight :
                distances[nxt_node] = nxt_weight + weight
                prev_node[nxt_node] = node
                heapq.heappush(q, (nxt_node, distances[nxt_node]))


n = int(input())    # 도시 개수
m = int(input())    # 버스 개수

edges = [[] for _ in range(n+1)]
for _ in range(m) :
    s, e, w = map(int, input().split())
    edges[s].append((e, w))

start, end = map(int, input().split())

distances = [INF] * (n + 1)
prev_node = [0] * (n + 1)

deijkstra(start)
print(distances[end])

path = [end]
now = end
while now != start :
    now = prev_node[now]
    path.append(now)

path.reverse()

print(len(path))
print(*path)