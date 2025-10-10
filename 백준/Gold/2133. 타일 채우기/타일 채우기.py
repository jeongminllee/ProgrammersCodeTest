N = int(input())
# 홀수는 당연히 안될거고
dp = [0] * 31

# 초기값
dp[0] = 1
dp[2] = 3

for i in range(4, N+1, 2) :
    dp[i] = dp[i-2] * 3
    for j in range(i-4, -1, -2) :
        dp[i] += dp[j] * 2

print(dp[N])