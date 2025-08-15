N = int(input())
if N < 10 :
    print(0)
    exit()

MOD = int(1e9)  # 정수 모듈러

# dp[N번째 수][마지막 수][방문한 수 bitmasking(0~1023)]
dp = [[0] * 1024 for _ in range(10)]
for d in range(1, 10) :
    dp[d][1<<d] = 1

for i in range(2, N + 1) :
    nxt = [[0] * 1024 for _ in range(10)]
    for last in range(10) :
        row = dp[last]
        # last - 1 로 전이
        if last > 0 :
            nl = last - 1
            for mask, val in enumerate(row) :
                if val :
                    nm = mask | (1 << nl)
                    nxt[nl][nm] = (nxt[nl][nm] + val) % MOD
        if last < 9 :
            nl = last + 1
            for mask, val in enumerate(row) :
                if val :
                    nm = mask | (1 << nl)
                    nxt[nl][nm] = (nxt[nl][nm] + val) % MOD

    dp = nxt

res = sum(dp[last][1023] for last in range(10)) % MOD
print(res)