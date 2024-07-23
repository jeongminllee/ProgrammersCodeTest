from collections import deque

def bfs(N, M, maps, visited) :
    q = deque()
    q.append((0, 0, 0))     # y, x, broken
    visited[0][0][0] = 1

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q :
        y, x, br = q.popleft()

        if y == N - 1 and x == M - 1:
            return visited[y][x][br]

        for i in range(4) :
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < N and 0 <= nx < M :
                if maps[ny][nx] == 0 and visited[ny][nx][br] == 0 :
                    visited[ny][nx][br] = visited[y][x][br] + 1
                    q.append((ny, nx, br))
                elif maps[ny][nx] == 1 and br == 0 :
                    visited[ny][nx][1] = visited[y][x][0] + 1
                    q.append((ny, nx, 1))


    return -1

N, M = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
print(bfs(N, M, maps, visited))