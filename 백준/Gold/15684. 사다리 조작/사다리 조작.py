N, M, H = map(int, input().split())

arr = [[0] * N for _ in range(H)]
for i in range(M) :
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1

def atoa() :
    for i in range(N) :
        start_num = i
        for j in range(H) :
            if arr[j][start_num] == 1 :
                start_num += 1
            elif start_num > 0 and arr[j][start_num-1] == 1 :
                start_num -= 1

        if i != start_num :
            return False
    return True

def dfs(cnt, x, y) :
    global res
    if res <= cnt :
        return
    if atoa() :
        res = min(res, cnt)
        return
    if cnt == 3 :
        return
    for i in range(x, H) :
        for j in range(0, N - 1) :
            if arr[i][j] == 0 :
                arr[i][j] = 1
                dfs(cnt + 1, i, j + 2)
                arr[i][j] = 0

res = 4
dfs(0, 0, 0)
if res > 3 :
    res = -1
print(res)