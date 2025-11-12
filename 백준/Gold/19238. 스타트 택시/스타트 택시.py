import heapq

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def find_passenger(ti, tj) :
    global board, fuel
    N = len(board)
    q = []
    visited = [[0] * N for _ in range(N)]

    heapq.heappush(q, (0, ti, tj))  # 우선순위: 거리, 행, 열
    visited[ti][tj] = 1

    while q :
        curr, ci, cj = heapq.heappop(q)

        if curr > fuel :    # 현재 소모한 연료가 충전되어 있는 연료보다 많다면
            return -1

        if board[ci][cj] < 0 :  # 승객이 서있는 자리라면
            return ci, cj, curr

        for d in range(4) :
            ni, nj = ci + di[d], cj + dj[d]
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0 :
                if board[ni][nj] <= 0 : # 다른 승객이 있는 자리도 포함
                    heapq.heappush(q, (curr+1, ni, nj))
                    visited[ni][nj] = 1

    # 그럼에도 불구하고 도달하지 못했다면...
    return -1

def move_passenger(si, sj, ei, ej) :
    global board, fuel
    N = len(board)
    q = []
    visited = [[0] * N for _ in range(N)]

    q.append((0, si, sj))
    visited[si][sj] = 1

    while q :
        curr, ci, cj = q.pop(0)

        if curr > fuel :    # 도착지 전에 연료가 모두 소모됨
            return -1

        if (ci, cj) == (ei, ej) :   # 도착지에 잘 도착했다면
            return curr

        for d in range(4) :
            ni, nj = ci + di[d], cj + dj[d]
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0 :
                if board[ni][nj] <= 0 :
                    q.append((curr+1, ni, nj))
                    visited[ni][nj] = 1

    return -1

def main() :
    """
    손님을 도착지로 데려다 주면 연료가 충전된다.
    이동할 때마다 연료는 1씩 소모
    승객을 태운 후 도착지로 가면 소모한 연료의 두 배 만큼 충전된다.
    => 도착지에 도착했을 때 연료가 0 이상이면 사용한 연료만큼 충전?
    => 이동하는 도중에 음수로 전환되면 return -1 인게 더 나은감?

    M명의 승객을 태워야 함. 그렇지 않으면 return -1
    먼저 태울 승객은 현재 택시의 위치에서 가장 가까운 승객, 가장 작은 행번호, 가장 작은 열번호 순
    """
    global board, fuel
    N, M, fuel = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    ti, tj = map(int, input().split())  # 택시 시작 위치
    ti, tj = ti-1, tj-1
    destinations = []
    for i in range(1, M+1) :
        si, sj, ei, ej = map(int, input().split())
        board[si-1][sj-1] = -i  # 승객 번호
        destinations.append((ei-1, ej-1))

    passengers = M

    while passengers > 0 :  # M명 태우기를 원하니까
        res = find_passenger(ti, tj)    # 승객 찾기

        if res == -1 :  # 연료가 다 소모되었거나, 다음 승객을 태울 수 없는 상황일 경우
            return -1

        ti, tj, cost = res  # 택시가 승객의 위치까지 이동
        fuel -= cost    # 승객의 위치까지 이동하는데 소모된 연료

        # 승객을 태움
        person = -board[ti][tj] - 1     # 현재 탑승한 승객 정보를 받아온다.
        board[ti][tj] = 0   # 태운 승객 위치는 0으로 갱신
        
        # 승객을 태운 택시가 도착지 까지 이동
        cost = move_passenger(ti, tj, destinations[person][0], destinations[person][1])
        
        # 도달하지 못했으면
        if cost == -1 :
            return -1
        
        # 도착지까지 도착한 택시의 위치 및 연료 충전
        ti, tj = destinations[person][0], destinations[person][1]
        fuel += cost
        
        # 승객은 내린다. 
        passengers -= 1

    return fuel

if __name__ == "__main__" :
    print(main())