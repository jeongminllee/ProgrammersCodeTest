# 일단 패턴을 구해보자
# idx = 1, 2, 3, 4, 5 ...
# val = 1, 2, 3, 5, 8 ...
# 이것 역시 피보나치 인 듯 하다. 
def solution(n) :
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1) :
        dp[i] = (dp[i - 2] + dp[i - 1]) % 1000000007

    return dp[n]