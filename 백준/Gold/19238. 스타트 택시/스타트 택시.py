import heapq

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def find_passenger(ti, tj) :
    global board, fuel
    N = len(board)
    q = []
    visited = [[0] * N for _ in range(N)]

    heapq.heappush(q, (0, ti, tj))
    visited[ti][tj] = 1

    while q :
        depth, ci, cj = heapq.heappop(q)

        if depth > fuel :
            return -1

        if board[ci][cj] < 0 :
            return ci, cj, depth

        for d in range(4) :
            ni, nj = ci + di[d], cj + dj[d]
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0 :
                if board[ni][nj] <= 0 :
                    heapq.heappush(q, (depth+1, ni, nj))
                    visited[ni][nj] = 1

    return -1

def move_passenger(si, sj, ei, ej) :
    global board, fuel
    N = len(board)
    q = []
    visited = [[0] * N for _ in range(N)]

    q.append((0, si, sj))
    visited[si][sj] = 1

    while q :
        depth, ci, cj = q.pop(0)

        if depth > fuel :
            return -1

        if (ci, cj) == (ei, ej) :
            return depth

        for d in range(4) :
            ni, nj = ci + di[d], cj + dj[d]
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0 :
                if board[ni][nj] <= 0 :
                    q.append((depth+1, ni, nj))
                    visited[ni][nj] = 1

    return -1

def main() :
    global board, fuel
    N, M, fuel = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    ti, tj = map(int, input().split())
    ti, tj = ti-1, tj-1
    destinations = []
    for i in range(1, M+1) :
        si, sj, ei, ej = map(int, input().split())
        board[si-1][sj-1] = -i
        destinations.append((ei-1, ej-1))

    passengers = M

    while passengers > 0 :
        result = find_passenger(ti, tj)
        if result == -1 :
            return -1
        ti, tj, cost = result
        fuel -= cost

        person = -board[ti][tj] - 1
        board[ti][tj] = 0

        cost = move_passenger(ti, tj, destinations[person][0], destinations[person][1])

        if cost == -1 :
            return -1
        ti, tj = destinations[person][0], destinations[person][1]
        fuel += cost

        passengers -= 1

    return fuel

if __name__ == "__main__" :
    print(main())