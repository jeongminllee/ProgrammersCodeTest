import heapq

INF = 1<<32

def dijkstra(start: int) -> int :
    q = []
    q.append((0, start))    # dist, node
    distances = [INF] * (P+1)
    distances[0] = 0        # padding 자리는 0으로 초기화
    distances[start] = 0    # 현재 노드를 0으로 초기화

    while q :
        curr_dist, curr = heapq.heappop(q)


        # 이미 더 짧은 거리로 방문한 적이 있다면
        if curr_dist > distances[curr] :
            continue

        for edge_cost, nxt in edges[curr] :
            nd = curr_dist + edge_cost
            if nd < distances[nxt] :
                distances[nxt] = nd
                heapq.heappush(q, (nd, nxt))

    # 이 start에 설탕을 둘 때, 각 목장까지 거리 * 소 마리 수 합산
    total = 0
    for pasture in range(1, P+1) :
        if cows[pasture] :
            total += distances[pasture] * cows[pasture]
    return total


def main() :
    """
    N: the number of cows
    P: the number of pastures
    C: the number of connecting paths
    """
    global N, P, C, cows, edges
    N, P, C = map(int, input().split())
    cows = [0] * (P+1)
    for _ in range(N) :
        pasture = int(input())
        cows[pasture] += 1

    edges = [[] for _ in range(P+1)]
    for _ in range(C) :
        u, v, w = map(int, input().split())
        edges[u].append((w, v))
        edges[v].append((w, u))

    res = INF

    for sugar in range(1, P+1) :
        res = min(res, dijkstra(sugar))
    return res

if __name__ == "__main__" :
    print(main())