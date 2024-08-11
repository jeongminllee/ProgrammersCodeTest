n, m = map(int, input().split())
v = [0] * (n + 1)

answer = list(map(int, input().split()))
answer.sort()
result = []

def dfs(depth, idx, n, m):
    if depth == m:
        print(' '.join(map(str, result)))
        return
    for i in range(n):
        if not v[i] :
            v[i] = 1
            result.append(answer[i])
            dfs(depth + 1, i + 1, n, m)
            v[i] = 0
            result.pop()

dfs(0, 1, n, m)