def main(N, K) :
    INF = 10 ** 18
    dp = [INF] * (N + 1)
    dp[0] = 0
    for i in range(N) :
        if dp[i] + 1 < dp[i + 1] :
            dp[i + 1] = dp[i] + 1

        if i >= 2 :
            j = i + i // 2
            if j <= N and dp[i] + 1 < dp[j] :
                dp[j] = dp[i] + 1

    return dp[N] <= K

if __name__ == "__main__" :
    N, K = map(int, input().split())
    print("minigimbob" if main(N, K) else "water")