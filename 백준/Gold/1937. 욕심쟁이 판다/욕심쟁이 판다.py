di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(si, sj) :
    if dp[si][sj] :
        return dp[si][sj]

    dp[si][sj] = 1

    for d in range(4) :
        ni, nj = si + di[d], sj + dj[d]
        if 0<=ni<n and 0<=nj<n and arr[ni][nj] > arr[si][sj]:
            dp[si][sj] = max(dp[si][sj], dfs(ni, nj) + 1)

    return dp[si][sj]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

for i in range(n) :
    for j in range(n) :
        if not dp[i][j] :
            dfs(i, j)

res = 0
for i in range(n) :
    res = max(res, max(dp[i]))
print(res)