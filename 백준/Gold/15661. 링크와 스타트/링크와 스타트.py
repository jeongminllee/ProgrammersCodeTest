N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
res = 99999

def cal() :
    global res
    left, right = 0, 0
    for i in range(N) :
        for j in range(N) :
            if visited[i] and visited[j] :
                left += arr[i][j]
            elif not visited[i] and not visited[j] :
                right += arr[i][j]

    res = min(res, abs(left - right))

def bt(depth) :
    if depth == N :
        cal()
        return

    visited[depth] = 1
    bt(depth + 1)
    visited[depth] = 0
    bt(depth + 1)

bt(0)
print(res)