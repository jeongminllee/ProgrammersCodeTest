def solution(n):
    if n <= 1 :
        return n
    a, b = 0, 1
    for _ in range(n) :
        a, b = b, (a + b)
        
    return a % 1234567

# def solution(n):
#     if n <= 1 :
#         return n
#     dp = [0] * (n + 1)
#     dp[1] = 1
#     for i in range(2, n + 1) :
#         dp[i] = (dp[i - 1] + dp[i - 2])

#     return dp[n]%1234567

