import heapq

N, M = map(int, input().split())

edges = [[] for _ in range(N + 1)]
distance = [float('inf')] * (N + 1)
for i in range(M) :
    a, b, c = map(int, input().split())
    edges[a].append((b, c))
    edges[b].append((a, c))

def dejkstra(start) :
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q :
        dst, now = heapq.heappop(q)
        if distance[now] < dst :
            continue

        for i in edges[now] :
            cost = dst + i[1]

            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance

print(dejkstra(1)[N])