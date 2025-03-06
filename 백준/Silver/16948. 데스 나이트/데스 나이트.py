import sys
input = sys.stdin.readline

from collections import deque

di = [-2, -2, 0, 0, 2, 2]
dj = [-1, 1, -2, 2, -1, 1]

def is_valid(i, j, N) :
    return 0 <= i < N and 0 <= j < N

def bfs(si, sj, ei, ej, N) :
    visited = [[-1] * N for _ in range(N)]
    visited[si][sj] = 0
    q = deque()
    q.append((si, sj, 0))

    while q :
        ci, cj, cnt = q.popleft()
        if (ci, cj) == (ei, ej) :
            return cnt

        for d in range(6) :
            ni, nj = ci + di[d], cj + dj[d]

            if is_valid(ni, nj, N) and visited[ni][nj] == -1 :
                visited[ni][nj] = visited[ci][cj] + 1
                q.append((ni, nj, visited[ni][nj]))

    return -1

def sol_16948() :
    N = int(input())
    r1,c1,r2,c2 = map(int, input().split())

    print(bfs(r1, c1, r2, c2, N))

sol_16948()