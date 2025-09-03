N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
w = [sum(arr[i][j] + arr[j][i] for j in range(N)) for i in range(N)]
S = sum(w)
dp = 1
for x in w :
    dp |= dp << x

S = sum(w)
half = S // 2
y = dp >> half
res = (y & -y).bit_length() - 1
print(res)