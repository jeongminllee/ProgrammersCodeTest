N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
w = [sum(arr[i][j] + arr[j][i] for j in range(N)) for i in range(N)]
S = sum(w)
dp = 1
for i in range(N) :
    dp |= (dp << w[i])
half = S // 2
res = half
dp = bin(dp)
for i, bit in enumerate(dp[2+half:]) :
    if bit == '1' :
        res = i
        break
print(res)