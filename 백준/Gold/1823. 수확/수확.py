n = int(input())
v = list(int(input()) for _ in range(n))

dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n) :
    dp[i][i] = n * v[i]


for length in range(2, n+1) :
    cnt = n - length + 1
    for s in range(0, n - length + 1) :
        e = s + length - 1
        dp[s][e] = max(
            dp[s+1][e] + cnt * v[s],
            dp[s][e-1] + cnt * v[e]
        )
        
print(dp[0][n-1])