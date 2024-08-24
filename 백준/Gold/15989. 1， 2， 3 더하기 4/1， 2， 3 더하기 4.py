T = int(input())
for _ in range(T) :
    n = int(input())
    dp = [0] * (n + 1)

    for i in range(1, n + 1) :
        if i <= 3 :
            dp[i] = i
        else :
            dp[i] = dp[i-3] + 1 + i//2

    print(dp[n])