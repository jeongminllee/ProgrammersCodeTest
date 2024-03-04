from collections import deque

def bfs() :
    q = deque()
    v = [[0] * m for _ in range(n)]

    cnt = 0
    for i in range(n) :
        for j in range(m) :
            if arr[i][j] == 1 :
                q.append((i, j))
                v[i][j] = 1
                
            elif arr[i][j] == 0 :
                cnt += 1

    while q :
        ci, cj = q.popleft()

        # 4방향, 범위 내, 미방문, arr[ni][nj] == 0 
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and v[ni][nj] == 0 and arr[ni][nj] == 0 :
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
                cnt -= 1

    if cnt == 0 :
        return v[ci][cj] - 1

    else :
        return -1

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
print(bfs())