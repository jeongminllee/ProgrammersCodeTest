def main() :
    N, M = map(int, input().split())
    memories = [0] + list(map(int, input().split()))
    costs = [0] + list(map(int, input().split()))
    
    cost_max = sum(costs)
    dp = [[0] * (cost_max + 1) for _ in range(N + 1)]
    answer = cost_max + 1

    for idx_app in range(1, N + 1) :
        for cost_curr in range(cost_max + 1) :
            if cost_curr < costs[idx_app] :
                dp[idx_app][cost_curr] = dp[idx_app - 1][cost_curr]
            else :
                dp[idx_app][cost_curr] = max(dp[idx_app - 1][cost_curr - costs[idx_app]] + memories[idx_app], dp[idx_app - 1][cost_curr])

            if dp[idx_app][cost_curr] >= M :
                answer = min(answer, cost_curr)

    print(answer)

main()