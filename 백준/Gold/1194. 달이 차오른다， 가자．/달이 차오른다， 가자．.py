from collections import deque

def bfs(si, sj) :
    q = deque()
    q.append((si, sj, 0))

    v = [[[-1] * (1<<6) for _ in range(M)] for _ in range(N)]
    v[si][sj][0] = 0

    while q :
        ci, cj, key = q.popleft()

        if arr[ci][cj] == '1' :
            return v[ci][cj][key]

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
            ni, nj = ci + di, cj + dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj][key] == -1 :
                if arr[ni][nj] == '#' :
                    continue
                elif arr[ni][nj] in keys :
                    nxt_key = key | (1<<(ord(arr[ni][nj]) - ord('a')))
                    v[ni][nj][nxt_key] = v[ci][cj][key] + 1
                    q.append((ni, nj, nxt_key))

                elif arr[ni][nj] in doors :
                    if key & (1<<(ord(arr[ni][nj]) - ord('A'))) :
                        # arr[ni][nj] = '.'
                        v[ni][nj][key] = v[ci][cj][key] + 1
                        q.append((ni, nj, key))
                    else :
                        continue
                else :
                    v[ni][nj][key] = v[ci][cj][key] + 1
                    q.append((ni, nj, key))

    return -1

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

keys = set(('a', 'b', 'c', 'd', 'e', 'f'))
doors = set(('A', 'B', 'C', 'D', 'E', 'F'))


for i in range(N) :
    for j in range(M) :
        if arr[i][j] == '0' :
            si, sj = i, j
            arr[i][j] = '.'

print(bfs(si, sj))