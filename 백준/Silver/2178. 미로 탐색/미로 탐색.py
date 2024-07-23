from collections import deque

N, M = map(int, input().split())
arr = [list(map(int,input())) for _ in range(N)]
v = [[0] * M for _ in range(N)]

q = deque()
q.append((0, 0))
v[0][0] = 1

while q :
    i, j = q.popleft()

    if i == N - 1 and j == M - 1 :
        break

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
        ni, nj = i + di, j + dj

        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and v[ni][nj] == 0 :
            v[ni][nj] = v[i][j] + 1
            q.append((ni, nj))

print(v[-1][-1])