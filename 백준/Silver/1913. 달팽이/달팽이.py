di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
N = int(input())        # 홀수 (무조건 가운데 1)
target = int(input())   # 음... 어떻게 접근할까

arr = [[0] * N for _ in range(N)]

i = j = 0
now = N*N
arr[0][0] = now
res = (1, 1)

dr = 0
now -= 1

while now != 0 :
    ni, nj = i + di[dr], j + dj[dr]
    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0 :
        i, j = ni, nj
        arr[i][j] = now
        if now == target :
            res = (i+1, j+1)
        now -= 1
    else :
        dr = (dr+1) % 4

for lst in arr :
    print(*lst)
print(*res)