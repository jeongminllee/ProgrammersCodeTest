import heapq

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dijkstra() :
    q = []
    heapq.heappush(q, (arr[0][0], 0, 0))
    visited[0][0] = 0

    while q :
        cost, i, j = heapq.heappop(q)

        if (i, j) == (N-1, N-1) :
            print(f'Problem {cnt}: {visited[i][j]}')
            break

        for d in range(4) :
            ni, nj = i + di[d], j + dj[d]

            if 0 <= ni < N and 0 <= nj < N :
                new_cost = cost + arr[ni][nj]

                if new_cost < visited[ni][nj] :
                    visited[ni][nj] = new_cost
                    heapq.heappush(q, (new_cost, ni, nj))

cnt = 1

while True :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    if N == 0 :
        break
    visited = [[float('inf')] * N for _ in range(N)]

    dijkstra()
    cnt += 1
    