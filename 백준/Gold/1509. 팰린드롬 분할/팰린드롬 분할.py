S = input()
n = len(S)
dp = [2500] * (n + 1)
dp[-1] = 0
pal = [[0] * n for _ in range(n)]

for i in range(n) :
    pal[i][i] = 1

for i in range(1, n) :
    if S[i-1] == S[i] :
        pal[i-1][i] = 1

for l in range(3, n+1) :
    for start in range(n-l+1) :
        end = start + l - 1
        if S[start] == S[end] and pal[start+1][end-1] :
            pal[start][end] = 1

for end in range(n) :
    for start in range(end+1) :
        if pal[start][end] :
            dp[end] = min(dp[end], dp[start-1]+1)
        else :
            dp[end] = min(dp[end], dp[end-1] + 1)

print(dp[n-1])