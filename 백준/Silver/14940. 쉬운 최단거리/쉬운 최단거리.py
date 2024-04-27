from collections import deque

def bfs(x, y) :
    q = deque()
    q.append((x, y))
    v[x][y] = 0

    while q :
        i, j = q.popleft()

        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < n and 0 <= nj < m and v[ni][nj] == -1:
                if arr[ni][nj] == 0 :
                    v[ni][nj] = 0
                elif arr[ni][nj] == 1 :
                    v[ni][nj] = v[i][j] + 1
                    q.append((ni, nj))

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
v = [[-1] * m for _ in range(n)]
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for i in range(n) :
    for j in range(m) :
        if arr[i][j] == 2 and v[i][j] == -1:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(0, end=' ')
        else:
            print(v[i][j], end=' ')
    print()