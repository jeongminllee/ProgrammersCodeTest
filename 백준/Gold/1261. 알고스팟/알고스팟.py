from collections import deque

# 이동 벡터
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(si, sj) :
    q = deque()
    q.append((si ,sj))
    v[si][sj] = 0

    while q :
        ci, cj = q.popleft()

        for d in range(4) :
            ni, nj = ci + di[d], cj + dj[d]
            # 여기 좀 헷갈림 특히 괄호 안.
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == -1 :
                if board[ni][nj] == 0 :
                    v[ni][nj] = v[ci][cj]
                    q.appendleft((ni, nj))
                else :
                    v[ni][nj] = v[ci][cj] + 1
                    q.append((ni, nj))

    return v

# 가로, 세로
M, N = map(int, input().split())

# board
board = [list(map(int, input().rstrip())) for _ in range(N)]

v = [[-1] * M for _ in range(N)]

# 정답
ans = bfs(0, 0)
print(ans[N-1][M-1])