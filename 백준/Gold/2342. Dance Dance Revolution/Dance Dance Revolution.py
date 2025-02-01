arr = [0] + list(map(int, input().split()))
arr.pop()
n = len(arr)
power = [[0] * 5 for _ in range(5)]

def po(a, b) :
    if a == b :
        return 1
    elif a == 0 :
        return 2
    elif abs(a - b) == 2 :
        return 4
    else :
        return 3

for i in range(5) :
    for j in range(5) :
        power[i][j] = po(i, j)

MAX = 4 * 100000 + 1

dp = [[[MAX] * 5 for _ in range(5)] for _ in range(n)]
dp[0][0][0] = 0

for i in range(1, n) :
    v = arr[i]

    for l in range(5) :
        for r in range(5) :
            dp[i][v][r] = min(dp[i][v][r], dp[i-1][l][r] + power[l][v])

    for l in range(5) :
        for r in range(5) :
            dp[i][l][v] = min(dp[i][l][v], dp[i-1][l][r] + power[r][v])

mn = MAX

for l in range(5) :
    for r in range(5) :
        mn = min(mn, dp[n-1][l][r])

print(mn)