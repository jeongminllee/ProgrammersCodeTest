import heapq

# 이동 벡터
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(si, sj) :
    q = []
    heapq.heappush(q, (si, sj, 0))
    v[si][sj] = 0

    while q :
        ci, cj, cost = heapq.heappop(q)

        for d in range(4) :
            ni, nj = ci + di[d], cj + dj[d]
            # 여기 좀 헷갈림 특히 괄호 안.
            if 0 <= ni < N and 0 <= nj < M :
                if board[ni][nj] + cost < v[ni][nj] :
                    v[ni][nj] = cost + board[ni][nj]
                    heapq.heappush(q, (ni, nj, v[ni][nj]))


    return v

# 가로, 세로
M, N = map(int, input().split())

# board
board = [list(map(int, input().rstrip())) for _ in range(N)]

v = [[1e10] * M for _ in range(N)]

# 정답
ans = bfs(0, 0)
print(ans[N-1][M-1])