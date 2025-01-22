R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

dp = [[0] * C for _ in range(R)]
dp[R-1][C-1] = 1

for i in range(R-1, -1, -1) :
    for j in range(C-1, -1, -1) :
        if (i, j) == (R-1, C-1) :
            continue

        for ni in range(i + 1, R) :
            for nj in range(j + 1, C) :
                if arr[i][j] != arr[ni][nj] :
                    dp[i][j] += dp[ni][nj]

print(dp[0][0])