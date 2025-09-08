# dp2 = dp1 + dp1
# dp3 = dp2 + dp1 + dp2
# dp4 = dp3 + dp2 + dp2 + dp3
# dp5 = dp4 + dp3 + dp2 + dp1 + dp2 + dp3 + dp4 = 14 + 5 + 2 + 1 + 2 + 5 + 14 = 28 + 10 + 5 = 42
def solution(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1) :
        s = 0
        left, right = 0, i - 1
        while left < right :
            s += 2 * dp[left] * dp[right]
            left += 1
            right -= 1
            
        if left == right :
            s += dp[left] * dp[left]
            
        dp[i] = s
        
    return dp[n]