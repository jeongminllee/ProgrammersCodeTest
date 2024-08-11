def dfs() :
    if len(s) == M :
        print(' '.join(map(str, s)))
        return
    for i in range(1, N + 1) :
        if visited[i] == 1 :
            continue
        visited[i] = 1
        s.append(i)
        dfs()
        s.pop()
        visited[i] = 0

N, M = map(int, input().split())
s = []
visited = [0] * (N + 1)

dfs()