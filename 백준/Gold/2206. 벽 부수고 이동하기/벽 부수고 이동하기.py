from collections import deque

def bfs() :
    q = deque()
    q.append((0, 0, 0))
    v = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    v[0][0][0] = 1

    while q :
        ci, cj, br = q.popleft()

        if (ci, cj) == (N-1, M-1) :
            return v[ci][cj][br]

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj][br] == 0 :
                if board[ni][nj] == 0 :
                    v[ni][nj][br] = v[ci][cj][br] + 1
                    q.append((ni, nj, br))
                elif board[ni][nj] == 1 and br == 0 :
                    v[ni][nj][1] = v[ci][cj][0] + 1
                    q.append((ni, nj, 1))

    return -1


N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
print(bfs())