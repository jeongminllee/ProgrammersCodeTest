from collections import deque

def bfs(si, sj, board) :
    q = deque()
    q.append((si, sj, 0))
    N, M = len(board), len(board[0])

    visited = [[0] * M for _ in range(N)]
    visited[si][sj] = 1

    while q :
        ci, cj, cnt = q.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and board[ni][nj] == 'L' and not visited[ni][nj] :
                visited[ni][nj] = visited[ci][cj] + 1
                q.append((ni, nj, cnt + 1))

    return cnt


def sol_2589() :
    N, M = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(N)]

    res = 0
    cnt = 0
    
    for i in range(N) :
        for j in range(M) :
            if board[i][j] == 'L' :
                cnt = bfs(i, j, board)
            res = max(res, cnt)
    print(res)
sol_2589()