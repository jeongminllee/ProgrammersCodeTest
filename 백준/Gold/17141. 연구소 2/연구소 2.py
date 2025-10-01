from collections import deque

def combination(lst, k) :
    def backtrack(start, output) :
        if len(output) == k :
            result.append(output[:])
            return

        for i in range(start, len(lst)) :
            output.append(lst[i])
            backtrack(i+1, output)
            output.pop()

    result = []
    backtrack(0, [])
    return result

def bfs(virus, empty) :
    q = deque(virus)
    time = 0

    v = [[-1] * N for _ in range(N)]
    for i, j in virus :
        v[i][j] = 0

    while q :
        ci, cj = q.popleft()

        if arr[ci][cj] == 0 :
            empty -= 1

        if not empty :
            break

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
            ni, nj = ci + di, cj + dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] == -1 and arr[ni][nj] != 1 :
                v[ni][nj] = v[ci][cj] + 1
                time = v[ni][nj]
                q.append((ni, nj))

    if not empty :
        return time
    else :
        return 1<<32

N, M = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

lst = []
empty = 0
for i in range(N) :
    for j in range(N) :
        if arr[i][j] != 1 :
            if arr[i][j] == 2 :
                lst.append((i, j))
                arr[i][j] = 0
            empty += 1

res = 1<<32
for virus in combination(lst, M) :
    res = min(res, bfs(virus, empty))

if res == 1<<32 :
    print(-1)
else :
    print(res)