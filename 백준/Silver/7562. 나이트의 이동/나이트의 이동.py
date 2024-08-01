from collections import deque

di = [2, 2, -2, -2, 1, 1, -1, -1]
dj = [1, -1, 1, -1, 2, -2, 2, -2]

def bfs(si, sj, ei, ej) :
    q = deque()
    q.append((si, sj))
    v = [[0] * l for _ in range(l)]
    v[si][sj] = 1
    while q:
        ci, cj = q.popleft()

        if (ci, cj) == (ei, ej) :
            return v[ci][cj] - 1

        for d in range(8) :
            ni, nj = ci + di[d], cj + dj[d]
            if 0<=ni<l and 0<=nj<l and v[ni][nj] == 0 :
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni, nj))

T = int(input())

for _ in range(T) :
    l = int(input())
    arr = list(map(int, input().split()))
    ans = list(map(int, input().split()))
    print(bfs(arr[0], arr[1], ans[0], ans[1]))