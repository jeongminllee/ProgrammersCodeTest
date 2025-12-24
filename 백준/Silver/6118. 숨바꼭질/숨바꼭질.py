import heapq

INF = 10 ** 9

def find(start) :
    q = []
    heapq.heappush(q, (0, start))
    dist = [INF] * (N+1)
    dist[start] = 0

    while q:
        curr_dist, curr_node = heapq.heappop(q)

        for nxt_node in graph[curr_node] :
            nxt_dist = curr_dist + 1
            if nxt_dist < dist[nxt_node] :
                heapq.heappush(q, (nxt_dist, nxt_node))
                dist[nxt_node] = nxt_dist

    return dist


N, M = map(int, input().split())
start = 1
# M개의 양방향 길
graph = [[] for _ in range(N+1)]

for _ in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = find(start)

res_dist = max(dist[1:])
res_node = dist[1:].index(res_dist) + 1
res_nums = dist[1:].count(res_dist)
print(res_node, res_dist, res_nums)