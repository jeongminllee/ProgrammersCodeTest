text1 = input()
text2 = input()

m = len(text1)
n = len(text2)

dp = [[0] * (n + 1) for _ in range(m + 1)]  # dp 설정
for i in range(1, m + 1) :
    for j in range(1, n + 1) :
        if text1[i-1] == text2[j-1] :       # 완전 탐색 - 같으면
            dp[i][j] = dp[i-1][j-1] + 1     # 다음 배열에 + 1
        else :
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # 인접 벡터? 배열?에서 최대값을 불러온다.

print(dp[m][n])