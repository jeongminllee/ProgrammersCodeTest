from collections import deque

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y) :
    q = deque()
    q.append((x, y))

    while q :
        x, y = q.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 1 and v[nx][ny] == 0:
                v[nx][ny] = 1
                q.append((nx, ny))
        
for _ in range(T) :
    m, n, k = map(int, input().split())
    arr = [[0] * n for _ in range(m)]
    v = [[0] * n for _ in range(m)]
    cnt = 0

    for _ in range(k) :
        x, y = map(int, input().split())
        arr[x][y] = 1

    for a in range(m) :
        for b in range(n) :
            if arr[a][b] == 1 and v[a][b] == 0 :
                bfs(a, b)
                cnt += 1

    print(cnt)