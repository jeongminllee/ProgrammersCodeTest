from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
maxNum = 0

for i in range(N) :
    for j in range(N) :
        if arr[i][j] > maxNum :
            maxNum = arr[i][j]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b, val, visited) :
    q = deque()
    q.append((a, b))
    visited[a][b] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N :
                if arr[nx][ny] > val and visited[nx][ny] == 0 :
                    visited[nx][ny] = 1
                    q.append((nx, ny))

ans = 0
for i in range(maxNum) :
    visited = [[0] * N for _ in range(N)]
    cnt = 0

    for j in range(N) :
        for k in range(N) :
            if arr[j][k] > i and visited[j][k] == 0 :
                bfs(j, k, i, visited)
                cnt += 1

    if ans < cnt :
        ans = cnt

print(ans)