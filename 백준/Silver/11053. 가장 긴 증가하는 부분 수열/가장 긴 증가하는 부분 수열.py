n = int(input())
arr = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(1, n + 1) :
    mx = 0
    for j in range(0, i) :
        if arr[i] > arr[j] :
            mx = max(mx, dp[j])
    dp[i] = mx + 1

print(max(dp))