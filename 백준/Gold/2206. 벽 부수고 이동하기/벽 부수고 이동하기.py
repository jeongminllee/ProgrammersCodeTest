from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(N, M, board, visited) :
    q = deque()
    q.append((0, 0, 0)) # i, j, br
    visited[0][0][0] = 1

    while q :
        ci, cj, br = q.popleft()
        
        # 목적지까지 도달했을 경우
        if (ci, cj) == (N-1, M-1) :
            return visited[ci][cj][br]

        for d in range(4) :
            ni, nj = ci + di[d], cj + dj[d]

            if 0 <= ni < N and 0 <= nj < M :
                if board[ni][nj] == 0 and visited[ni][nj][br] == 0 :
                    visited[ni][nj][br] = visited[ci][cj][br] + 1
                    q.append((ni, nj, br))
                elif board[ni][nj] == 1 and br == 0 :
                    visited[ni][nj][1] = visited[ci][cj][0] + 1
                    q.append((ni, nj, 1))

    # 다 돌지 못했을 경우
    return -1


N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
print(bfs(N, M, board, visited))