from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(s, e, maps) :
    n, m = len(maps), len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(m):
            if maps[i][j] == s:
                q.append((i, j, 0))
                visited[i][j] = 1
                break

    while q:
        y, x, cost = q.popleft()

        if maps[y][x] == e:
            return cost

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != "X" and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                q.append((ny, nx, cost + 1))

    return -1

def solution(maps):
    p1 = bfs("S", "L", maps)
    p2 = bfs("L", "E", maps)

    if p1 != -1 and p2 != -1 :
        return p1 + p2

    return -1