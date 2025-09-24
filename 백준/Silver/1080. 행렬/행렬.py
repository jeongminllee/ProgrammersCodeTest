
def rev(i, j) :
    for y in range(i, i+3) :
        for x in range(j, j+3) :
            if arr[y][x] == 1 :
                arr[y][x] = 0
            else :
                arr[y][x] = 1

N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]
target = [list(map(int, input())) for _ in range(N)]

cnt = 0
if (N < 3 or M < 3) and arr != target :
    cnt = -1
else :
    for i in range(N-2) :
        for j in range(M-2) :
            if arr[i][j] != target[i][j] :
                cnt += 1
                rev(i, j)

if cnt != -1 and arr != target :
    cnt = -1

print(cnt)