dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque

def bfs(sy, sx) :
    global res
    q = deque()
    q.append((sy, sx))    # i, j, nums, cnt
    arr[sy][sx] = 1
    cnt = 1

    while q :
        cy, cx = q.popleft()
        for d in range(4) :
            ny, nx = cy + dy[d], cx + dx[d]
            if 0 <= ny < M and 0 <= nx < N and arr[ny][nx] == 0 :
                arr[ny][nx] = 1
                q.append((ny, nx))
                cnt += 1
    res.append(cnt)


M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]
res = []

# x1, y1, x2, y2
for _ in range(K) :
    x1, y1, x2, y2 = map(int, input().split())
    w, h = (x2- x1), (y2 - y1)
    for y in range(y1, y2) :
        for x in range(x1, x2) :
            arr[y][x] = -1

for y in range(M) :
    for x in range(N) :
        if arr[y][x] == 0 :
            bfs(y, x)
res.sort()
print(len(res))
print(*res)