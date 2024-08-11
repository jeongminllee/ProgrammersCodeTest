n, m = map(int, input().split())

answer = []

def dfs(depth, idx, n, m):
    if depth == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(idx, n + 1):
        answer.append(i)
        dfs(depth+1, idx, n, m)
        answer.pop()

dfs(0, 1, n, m)