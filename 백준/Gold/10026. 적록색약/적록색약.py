from collections import deque

n = int(input())
normal = [list(input().rstrip()) for _ in range(n)]
blind = [[normal[i][j] if normal[i][j] != 'G' else 'R' for j in range(n)] for i in range(n)]

n_visited = [[0] * n for _ in range(n)]
b_visited = [[0] * n for _ in range(n)]
n_cnt = b_cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, arr, visited) :
    color = arr[x][y]
    q = deque()
    q.append((x, y))

    while q :
        x, y = q.popleft()

        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == color and visited[nx][ny] == 0 :
                visited[nx][ny] = 1
                q.append((nx, ny))
    return visited

for i in range(n) :
    for j in range(n) :
        if n_visited[i][j] == 0 :
            n_visited = bfs(i, j, normal, n_visited)
            n_cnt += 1
        if b_visited[i][j] == 0:
            b_visited = bfs(i, j, blind, b_visited)
            b_cnt += 1

print(n_cnt, b_cnt)