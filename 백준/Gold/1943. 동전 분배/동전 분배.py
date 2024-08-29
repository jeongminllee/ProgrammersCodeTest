INF = 100001
def solve(N, coin, total) :
    # 돈의 총합이 홀수이면 정확히 반으로 나누는 것은 불가능하다.
    if total & 1 :
        return 0

    total //= 2
    dp = [INF] * (total + 1)

    # 0원은 항상 만들 수 있다.
    dp[0] = 0

    for x in range(1, N+1) :
        cost, amount = coin[x]

        for m in range(cost, total + 1) :
            if dp[m] < INF :
                dp[m] = 0
                continue

            if dp[m - cost] + 1 <= amount :
                dp[m] = dp[m - cost] + 1
    return 1 if dp[total] < INF else 0

for _ in range(3) :
    N = int(input())
    coin, total = [None], 0
    for _ in range(N) :
        cost, amount = map(int, input().split())

        coin.append((cost, amount))
        total += cost * amount

    print(solve(N, coin, total))