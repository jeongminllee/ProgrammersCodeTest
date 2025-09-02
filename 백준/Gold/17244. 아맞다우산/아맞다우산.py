from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(si, sj, ei, ej, visited) :
    q = deque()
    q.append((si, sj, 0))
    visited[0][si][sj] = 0

    while q :
        ci, cj, bit = q.popleft()
        if arr[ci][cj] == 'E' and bit == 2 ** cnt - 1 :
            return visited[bit][ci][cj]

        for d in range(4) :
            ni, nj = ci + di[d], cj + dj[d]

            if 0 <= ni < N and 0 <= nj < M and visited[bit][ni][nj] == -1 and arr[ni][nj] != '#':
                if arr[ni][nj] == 'X' :
                    nxt_bit = bit | 1<<tbl[(ni, nj)]
                    visited[nxt_bit][ni][nj] = visited[bit][ci][cj] + 1
                    q.append((ni, nj, nxt_bit))
                else :
                    visited[bit][ni][nj] = visited[bit][ci][cj] + 1
                    q.append((ni, nj, bit))


M, N = map(int, input().split())
arr = [list(input()) for _ in range(N)]
tbl, cnt = {}, 0

for i in range(N) :
    for j in range(M) :
        if arr[i][j] == 'S' :
            arr[i][j] = '.'
            start = (i, j)
        elif arr[i][j] == 'E' :
            end = (i, j)
        elif arr[i][j] == 'X' :
            tbl[(i, j)] = cnt
            cnt += 1

visited = [[[-1] * M for _ in range(N)] for _ in range(1<<cnt)]
si, sj = start
ei, ej = end
print(bfs(si, sj, ei, ej, visited))