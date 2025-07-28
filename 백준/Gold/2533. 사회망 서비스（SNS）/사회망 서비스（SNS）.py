import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
from collections import defaultdict

# 친구 관계 트리의 정점 개수
N = int(input())
edges = defaultdict(list)
dp = [[0, 0] for _ in range(N + 1)]
for _ in range(N - 1) :
    u, v = map(int, input().split())    # 친구 관계 업데이트
    edges[u].append(v)
    edges[v].append(u)

visited = [0 for _ in range(N + 1)]
def dfs(start) :
    global edges, visited
    visited[start] = 1
    if len(edges[start]) == 0 :
        dp[start][1] = 1
        dp[start][0] = 0
    else :
        for edge in edges[start] :
            if visited[edge] == 0 :
                dfs(edge)
                dp[start][1] += min(dp[edge])
                dp[start][0] += dp[edge][1]

        dp[start][1] += 1

dfs(1)
print(min(dp[1]))