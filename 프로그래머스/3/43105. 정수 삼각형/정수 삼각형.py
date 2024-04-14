def solution(triangle):
    n = len(triangle)
    dp = [[0] * n for _ in range(n)]
    
    # 배열 가장 아래 라인초기화
    for i in range(n) :
        dp[n-1][i] = triangle[n-1][i]

    # 아래쪽 라인부터 올라가면서 빈 배열 채우기
    for i in range(n - 2, -1, -1) :
        for j in range(i + 1) :
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1])+ triangle[i][j]
            
    # 꼭대기 값 리턴
    return dp[0][0]