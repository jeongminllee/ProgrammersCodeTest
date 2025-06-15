N, M, H = map(int, input().split())

arr = [[0] * N for _ in range(H)]
for i in range(M) :
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
    arr[a-1][b] = 2

def atoa() :
    same = 0
    for s in range(N) :
        now = s
        for j in range(H) :
            if arr[j][now] == 1 :
                now += 1
            elif arr[j][now] == 2 :
                now -= 1
        if now == s :
            same += 1
    return same

def dfs(n) :
    global res

    if res != -1 :
        return

    tmp = atoa()

    if tmp + (cnt - n) * 2 < N :
        return

    if n == cnt :
        if tmp == N :
            res = cnt
        return

    for i in range(H) :
        for j in range(N - 1) :
            if arr[i][j] or arr[i][j+1] :
                continue
                
            arr[i][j], arr[i][j+1] = 1, 2
            dfs(n + 1)
            arr[i][j], arr[i][j+1] = 0, 0

res = -1
for cnt in range(4) :
    dfs(0)
    if res != -1 :
        break

print(res)