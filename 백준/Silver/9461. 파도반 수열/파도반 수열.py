T = int(input())
for _ in range(T) :
    n = int(input())
    dp = [0 for _ in range(101)]
    dp[1] = dp[2] = 1
    for i in range(3, 101) :
        dp[i] = dp[i - 3] + dp[i - 2]

    print(dp[n])