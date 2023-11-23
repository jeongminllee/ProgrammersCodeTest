import heapq

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
dst = [float('inf')] * (n + 1
                        )
for _ in range(m) :
    # a: 출발 도시 번호, b: 도착 도시 번호, c: 버스 비용
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

s, e = map(int, input().split())
def dijkstra(start) :
    q = []
    heapq.heappush(q, (0, start))
    dst[start] = 0

    while q :
        dist, now = heapq.heappop(q)
        if dst[now] < dist :
            continue

        for i in graph[now] :
            cost = dist + i[1]
            if cost < dst[i[0]] :
                dst[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(s)
print(dst[e])