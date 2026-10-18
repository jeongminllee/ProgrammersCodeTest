INF = 1<<32
def solution(info, n, m):
    dp = [[INF] * m for _ in range(len(info) + 1)]
    
    # 물건 0개, B의 흔적 0 -> A의 흔적 0
    dp[0][0] = 0
    
    for i in range(1, len(info) + 1) :
        a = info[i - 1][0]
        b = info[i - 1][1]
        
        for j in range(m) :
            # A를 선택하는 경우
            dp[i][j] = min(dp[i][j], dp[i-1][j] + a)
            
            # B가 선택하는 경우
            if j + b < m :
                dp[i][j + b] = min(dp[i][j+b], dp[i-1][j])
                
    min_value = INF
    
    for j in range(m) :
        min_value = min(min_value, dp[-1][j])
        
    return -1 if min_value >= n else min_value