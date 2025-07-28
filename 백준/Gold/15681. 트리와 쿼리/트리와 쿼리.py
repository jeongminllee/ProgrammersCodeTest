import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
from collections import defaultdict

def dfs(start) :
    global visited
    visited[start] = 1
    for i in edges[start] :
        if visited[i] == - 1 :
            visited[start] += dfs(i)
    return visited[start]

# 트리 정점 갯수, 루트 번호, 쿼리 수
N, R, Q = map(int, input().split())
edges = defaultdict(list)
visited = [-1 for _ in range(N + 1)]

for _ in range(N - 1) :
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

dfs(R)

for _ in range(Q) :
    query = int(input())
    print(visited[query])