from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(si, sj, size) :
    q = deque()
    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        size += 1
        for d in range(4) :
            ni, nj = ci + di[d], cj + dj[d]

            if 0<=ni<n and 0<=nj<m and arr[ni][nj] == 1 and v[ni][nj] == 0 :
                v[ni][nj] = 1
                q.append((ni, nj))
    return size


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
v = [[0] * m for _ in range(n)]
cnt = 0
ans = 0
for i in range(n) :
    for j in range(m) :
        if arr[i][j] == 1 and v[i][j] == 0 :
            ans = max(ans, bfs(i, j, 0))
            cnt += 1

print(cnt)
print(ans)