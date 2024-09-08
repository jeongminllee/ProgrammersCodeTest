def solution(money):
    n = len(money)

    # 첫 번째 집을 털었을 경우 (마지막 집은 털 수 없음)
    dp1 = [0] * n
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])

    for i in range(2, n - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])

    # 첫 번째 집을 털지 않았을 경우 (마지막 집을 털 수 있음)
    dp2 = [0] * n
    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(2, n):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

    # 두 경우 중 최댓값 반환
    return max(max(dp1), max(dp2))