def dfs(graph, now, N) :
    stack = []
    stack.append(now)
    path = []

    while stack :
        now = stack[-1]
        if graph[now] :
            for near, cnt in graph[now].items() :
                graph[now][near] -= 1
                graph[near][now] -= 1
                if graph[now][near] == 0 :
                    graph[now].pop(near)
                    graph[near].pop(now)
                stack.append(near)
                break
        else :
            path.append(now+1)
            stack.pop()

    return path

N = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]
graph = [{} for _ in range(N)]
for i in range(N) :
    degree = 0
    for j in range(N) :
        degree += adj[i][j]
        if adj[i][j] :
            graph[i][j] = adj[i][j]
    if degree % 2 :
        print(-1)
        exit()
        
print(*dfs(graph, 0, N))