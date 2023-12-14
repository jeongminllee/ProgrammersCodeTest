n = int(input())
lst = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n + 1)


dp[0] = lst[0]
dp[1] = sum(lst[:2])

for i in range(2, n + 1) :
    dp[i] = max(dp[i - 1], dp[i - 2] + lst[i], dp[i - 3] + lst[i - 1] + lst[i])

print(max(dp))