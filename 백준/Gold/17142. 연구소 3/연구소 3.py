di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

from collections import deque
from itertools import combinations

def bfs(virus, time, empty) :
    global res
    q = deque(virus)
    sec = 0
    v = [[0] * N for _ in range(N)]

    for i, j in virus :
        v[i][j] = 1

    while q :
        if not empty :
            break
        sec += 1
        if sec >= time :
            return 1<<32

        for _ in range(len(q)) :
            ci, cj = q.popleft()
            for d in range(4) :
                ni, nj = ci + di[d], cj + dj[d]
                if 0<=ni<N and 0<=nj<N and arr[ni][nj] != 1 and v[ni][nj] == 0 :
                    v[ni][nj] = 1
                    q.append((ni, nj))
                    if arr[ni][nj] == 0 :
                        empty -= 1

    if not empty :
        return sec
    else :
        return 1<<32

# 연구소 크기, 바이러스 개수
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
res = 1<<32

virus_list = []
empty = 0
for i in range(N) :
    for j in range(N) :
        if arr[i][j] == 2 :
            virus_list.append((i, j))
        elif arr[i][j] == 0 :
            empty += 1

for virus in combinations(virus_list, M) :
    res = min(res, bfs(virus, res, empty))

if res == 1<<32 :
    print(-1)
else :
    print(res)