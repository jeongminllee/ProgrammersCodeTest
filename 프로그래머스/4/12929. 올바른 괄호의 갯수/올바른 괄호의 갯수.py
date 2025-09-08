def solution(n):
    dp = [0] * (2*n + 1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, 2*n + 1) :
        dp[i] = i * dp[i-1]
        
    return (dp[2*n]) // (dp[n]**2 * (n + 1))
    
'''
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
'''