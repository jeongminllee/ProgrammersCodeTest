di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

def check(i, j) :
    for d in range(5) :
        ni, nj = i + di[d], j + dj[d]
        if visited[ni][nj] :
            return False
    return True

def dfs() :
    global cnt, res, cost
    if cnt == 3 :
        res = min(res, cost)
        return

    for i in range(1, N - 1) :
        for j in range(1, N - 1) :
            if check(i, j) :
                cnt += 1
                for d in range(5) :
                    ni, nj = i + di[d], j + dj[d]
                    visited[ni][nj] = 1
                    cost += arr[ni][nj]

                dfs()
                cnt -= 1
                for d in range(5) :
                    ni, nj = i + di[d], j + dj[d]
                    visited[ni][nj] = 0
                    cost -= arr[ni][nj]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cnt = 0
cost = 0
res = 10001
dfs()
print(res)