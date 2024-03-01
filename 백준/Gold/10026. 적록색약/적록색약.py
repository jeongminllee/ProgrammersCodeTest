import sys
sys.setrecursionlimit(10 ** 4)

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
v = [[0] * n for _ in range(n)]

cnt1 = cnt2 = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y) :
    v[x][y] = 1
    cur = arr[x][y]

    for k in range(4) :
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == cur and v[nx][ny] == 0 :
            dfs(nx, ny)

for i in range(n) :
    for j in range(n) :
        if v[i][j] == 0 :
            dfs(i, j)
            cnt1 += 1

# 적록색약
for i in range(n) :
    for j in range(n) :
        if arr[i][j] == 'R' :
            arr[i][j] = 'G'

v = [[0] * n for _ in range(n)]

for i in range(n) :
    for j in range(n) :
        if v[i][j] == 0 :
            dfs(i, j)
            cnt2 += 1

print(cnt1, cnt2)