# 입력 받기
n, k = map(int, input().split())

items = [[0, 0]]

for _ in range(n) :
    items.append(list(map(int, input().split())))

# dp[i][j] : i번째 물건까지 고려했을 때, 무게 weight에서의 최대 가치
dp = [[0] * (k + 1) for _ in range(n + 1)]

# 각 물건에 대해
for i in range(1, n + 1) :
    weight, value = items[i]
    # 각 무게에 대해
    for j in range(1, k + 1) :
        if j < weight :     # 현재 물건을 넣을 수 없는 경우
            dp[i][j] = dp[i - 1][j]

        else :  # 현재 물건을 넣을 수 있는 경우
            # 현재 물건을 넣지 않는 경우와 넣는 경우 중 최댓값 선택
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

# 결과 출력
print(dp[n][k])