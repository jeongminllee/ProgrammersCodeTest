n = int(input())
lst = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
ans = 0
if max(lst[1:]) < 0 :
    ans = max(lst[1:])
else :
    for i in range(1, n + 1) :
        dp[i] = max(dp[i - 1] + lst[i], 0)
    ans = max(dp[1:])

print(ans)