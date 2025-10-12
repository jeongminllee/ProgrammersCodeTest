n = int(input())
weights = [0] + list(map(int, input().split()))   # 패딩
edges = [[] for _ in range(n+1)]
while True: # 트리(연결되어 있고 사이클이 없는 그래프) -> 간선의 개수가 n-1임
    try :
        v, e = map(int, input().split())
        edges[v].append(e)
        edges[e].append(v)
    except :
        break

dp = [[0, 0] for _ in range(n+1)]
path = [[[] for _ in range(2)] for _ in range(n+1)]
v = [0] * (n + 1)

def dfs(node: int) -> list[list[int]]  :
    v[node] = 1
    dp[node][1] += weights[node]
    path[node][1].append(node)

    for x in edges[node] :
        if not v[x] :
            res = dfs(x)
            dp[node][0] += max(dp[x][0], dp[x][1])
            dp[node][1] += dp[x][0]

            path[node][1] += res[0]
            if dp[x][0] > dp[x][1] :
                path[node][0] += res[0]
            else :
                path[node][0] += res[1]

    return path[node]

p = dfs(1)

if dp[1][0] > dp[1][1] :
    print(dp[1][0])
    p[0].sort()
    for i in p[0] :
        print(i, end=' ')
else :
    print(dp[1][1])
    p[1].sort()
    for i in p[1] :
        print(i, end=' ')