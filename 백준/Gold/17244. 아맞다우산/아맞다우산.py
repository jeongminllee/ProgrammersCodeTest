from collections import deque

def bfs(si, sj, ei, ej, cnt) :
    q = deque()
    v = [[[-1] * (1<<cnt) for _ in range(M)] for _ in range(N)]

    q.append((si, sj, 0))
    v[si][sj][0] = 0

    while q :
        ci, cj, bit = q.popleft()
        if (ci, cj) == (ei, ej) and bit == 2 ** cnt - 1 :
            return v[ci][cj][bit]

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
            ni, nj = ci + di, cj + dj

            if 0<=ni<N and 0<=nj<M and v[ni][nj][bit] == -1 :
                if arr[ni][nj] == '#' :
                    continue
                elif arr[ni][nj] == 'X' :
                    nxt_cnt = bit | (1<<tbl[(ni, nj)])
                    v[ni][nj][nxt_cnt] = v[ci][cj][bit] + 1
                    q.append((ni, nj, nxt_cnt))
                else :
                    v[ni][nj][bit] = v[ci][cj][bit] + 1
                    q.append((ni, nj, bit))

    return -1

M, N = map(int, input().split())
arr = [list(input()) for _ in range(N)]

cnt = 0
tbl = {}
for i in range(N) :
    for j in range(M) :
        if arr[i][j] == 'S' :
            si, sj = i, j
            arr[i][j] = '.'
        if arr[i][j] == 'E' :
            ei, ej = i, j
            arr[i][j] = '.'
        if arr[i][j] == 'X' :
            tbl[(i, j)] = cnt
            cnt += 1

print(bfs(si, sj, ei, ej, cnt))