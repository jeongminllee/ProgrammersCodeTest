from collections import deque

di = [-1, 1, 0, 0, -1, 1, 1, -1]
dj = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(si, sj) :
    q = deque()
    q.append((si, sj))
    v[si][sj] = 1

    while q :
        i, j = q.popleft()

        for d in range(8):
            ni, nj = i + di[d], j + dj[d]
            if 0 <=ni<h and 0<=nj<w and arr[ni][nj] == 1 and v[ni][nj] == 0 :
                q.append((ni, nj))
                v[ni][nj] = 1


while True :
    w, h = map(int, input().split())
    if (w, h) == (0, 0) :
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    v = [[0] * w for _ in range(h)]
    cnt = 0

    for i in range(h) :
        for j in range(w) :
            if arr[i][j] == 1 and v[i][j] == 0 :
                bfs(i, j)
                cnt += 1
    print(cnt)