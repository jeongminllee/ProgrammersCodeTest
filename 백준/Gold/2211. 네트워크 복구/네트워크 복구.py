import heapq

INF = 10**9


def dijkstra(start) :
    q = []
    distances[start] = 0
    heapq.heappush(q, (0, start))

    while q :
        dist, curr = heapq.heappop(q)

        if distances[curr] < dist :
            continue

        for nxt_cost, nxt_node in edges[curr] :
            cost = nxt_cost + dist

            if distances[nxt_node] > cost :
                parent[nxt_node] = curr
                distances[nxt_node] = cost
                heapq.heappush(q, (cost, nxt_node))

def main() :
    global edges, distances, parent
    N, M = map(int, input().split())
    edges = [[] for _ in range(N+1)]
    for _ in range(M) :
        a,b,c = map(int, input().split())
        edges[a].append((c, b))
        edges[b].append((c, a))

    distances = [INF] * (N+1)
    parent = [0] * (N+1)

    dijkstra(1)

    print(N - 1)
    for i in range(2, N+1) :
        print(i, parent[i])


if __name__ == "__main__" :
    main()