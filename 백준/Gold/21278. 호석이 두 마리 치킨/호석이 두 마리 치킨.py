INF = 1<<32

N, M = map(int, input().split())

edges = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(N + 1) :
    edges[i][i] = 0
for _ in range(M) :
    u, v = map(int, input().split())
    edges[u][v] = 1
    edges[v][u] = 1

# 결과 : 건물번호1, 건물번호2, 왕복시간의 합
# 우선순위 : [왕복시간의 합, 건물번호1, 건물번호2]
# 정점에서 정점으로 가는 최소 거리 구하기
for k in range(1, N+1) :
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            edges[i][j] = min(edges[i][j], edges[i][k] + edges[k][j])

# 거리 합 구하기
mn = INF
for i in range(1, N) :
    for j in range(i+1, N+1) :
        sm = 0
        for k in range(1, N+1) :
            sm += min(edges[k][i], edges[k][j]) * 2
        if sm < mn :
            mn = sm
            res = [i, j, sm]

print(*res)