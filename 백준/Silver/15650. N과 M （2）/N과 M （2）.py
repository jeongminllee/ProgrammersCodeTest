n, m = map(int, input().split())

visited = [0] * (n + 1)
answer = []

def dfs(depth, idx, n, m) :
    if depth == m :
        print(' '.join(map(str, answer)))
        return
    for i in range(idx, n + 1) :
        if not visited[i] :
            visited[i] = 1
            answer.append(i)
            dfs(depth + 1, i + 1, n, m)
            visited[i] = 0
            answer.pop()
            
dfs(0, 1, n, m)