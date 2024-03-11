import heapq

INF = float('inf')

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v + 1)]
dst = [INF] * (v + 1)

for _ in range(e) :
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

def dijkstra(s) :
    q = []
    heapq.heappush(q, (0, s))
    dst[s] = 0

    while q :
        dist, node = heapq.heappop(q)

        if dst[node] < dist :
            continue

        for v, w in graph[node] :
            if dst[v] > dst[node] + w :
                dst[v] = dst[node] + w
                heapq.heappush(q, [dst[node] + w, v])

dijkstra(k)

for i in range(1, len(dst)) :
    if dst[i] == float('inf') :
        print("INF")
    else :
        print(dst[i])