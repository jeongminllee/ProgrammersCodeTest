N, L = map(int, input().split())
arr =[[0, 0, 1]] + [list(map(int, input().split())) for _ in range(N)] + [[L, 0, 1]]

cnt = 0
for i in range(1, len(arr)) :
    D, R, G = arr[i]
    cnt += (D - arr[i - 1][0])
    cnt += max(0, R - (cnt % (R + G)))

print(cnt)