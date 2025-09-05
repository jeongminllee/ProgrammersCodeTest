import heapq
from collections import defaultdict

INF = float('inf')

def dejkstra(start, end, C, mx, edges, costs) :
    dist = [INF] * (N + 1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q :
        w, v = heapq.heappop(q)

        if dist[v] != w :
            continue

        for nxt_w, nxt_v in edges[v] :
            cost = w + nxt_w
            if nxt_w <= mx and cost < dist[nxt_v] :
                dist[nxt_v] = cost
                heapq.heappush(q, (cost, nxt_v))

    return dist[end] <= C

def solution(N, M, A, B, C, edges, costs) :
    '''
    :param N: 교차로 개수
    :param M: 골목 개수
    :param A: 시작번호
    :param B: 종료번호
    :param C: 가진 금액
    :param edges: 그래프 목록
    :return: 갈 수 있는 골목의 최대 금액의 최솟값을 구하라.
    '''
    costs.sort()
    left, right = 0, len(costs) - 1
    res = INF
    while left <= right :
        mid = (left + right) // 2
        if dejkstra(A, B, C, costs[mid], edges, costs) :
            right = mid - 1
            if costs[mid] < res :
                res = costs[mid]
        else :
            left = mid + 1

    return res if res != INF else -1

if __name__ == '__main__' :
    N, M, A, B, C = map(int, input().split())
    edges = defaultdict(list)
    costs = []
    for _ in range(M) :
        u, v, cost = map(int, input().split())
        edges[u].append((cost, v))
        edges[v].append((cost, u))
        costs.append(cost)
    print(solution(N, M, A, B, C, edges, costs))