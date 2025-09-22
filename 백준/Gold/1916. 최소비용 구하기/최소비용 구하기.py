import heapq

def deijkstra(start, end) :
    q = []
    distances = [INF] * (N + 1)

    heapq.heappush(q, (start, 0))
    distances[start] = 0

    while q :
        curr, dist = heapq.heappop(q)
        if distances[curr] < dist :
            continue

        for node in edges[curr] :
            nxt_node, nxt_dist = node
            if distances[nxt_node] > dist + nxt_dist :
                distances[nxt_node] = dist + nxt_dist
                heapq.heappush(q, (nxt_node, distances[nxt_node]))

    return distances[end]
#############
# 입력
N = int(input())    # N 개의 도시
M = int(input())    # M 개의 버스
edges = [[] for _ in range(N+1)]

for _ in range(M) :
    u, v, w = map(int, input().split())
    edges[u].append((v, w))

start, end = map(int, input().split())
#############
INF = 1<<32
res = deijkstra(start, end)
print(res)