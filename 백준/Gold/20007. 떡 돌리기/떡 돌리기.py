import heapq

INF = float('inf')

def deijkstra(start, edges, N) :
    q = []
    heapq.heappush(q, (start, 0))

    distnaces = [INF] * N
    distnaces[start] = 0

    while q:
        node, distance = heapq.heappop(q)

        for (nxt_node, nxt_dist) in edges[node] :
            new_dist = nxt_dist + distance
            if distnaces[nxt_node] > new_dist :
                distnaces[nxt_node] = new_dist
                heapq.heappush(q, (nxt_node, new_dist))

    return distnaces

def main() :
    # 이웃집 개수, 양방향 도로 개수, 피로도 제한, 내 집
    N, M, X, Y = map(int, input().split())
    edges = [[] for _ in range(N)]
    for _ in range(M) :
        A, B, C = map(int, input().split()) # A집, B집, C거리
        edges[A].append((B, C))
        edges[B].append((A, C))

    distances = deijkstra(Y, edges, N)

    # 일, 이동 거리 계산
    day = cost = 0

    # 문제점 발생 : 갔다 온다는 설정은 어떻게 해야 할까.
    # 집에 갔다가 그 자리에서 다시 나가는거 설정을 어떻게 할까

    trips = []
    for i in range(N) :
        if i == Y :
            continue
        if distances[i] == INF :
            print(-1)
            return
        trips.append(2 * distances[i])

    trips.sort()    # 가까운 집부터 처리

    days = daily_sum = 0
    for trip in trips :
        # 하루 이동 한도보다 혼자 왕복 거리가 더 크다면 배달 불가능
        if trip > X :
            print(-1)
            return
        # 현재 날짜에 더 가도 한도를 넘지 않으면 같은 날 배달
        if daily_sum + trip <= X :
            daily_sum += trip
        else :
            # 한도를 넘는다면 하루를 마치고 다음 날 시작
            days += 1
            daily_sum = trip

    # 남은 누적 이동 거리가 있다면 마지막 날 추가
    if daily_sum > 0 :
        days += 1

    print(days)

main()