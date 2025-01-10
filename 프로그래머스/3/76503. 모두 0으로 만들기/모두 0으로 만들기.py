import sys
sys.setrecursionlimit(10**6)

def solution(a, edges):
    if sum(a) != 0 :
        return -1

    cnt = 0
    n = len(a)
    graph = [[] for _ in range(n)]

    for u, v in edges :
        graph[u].append(v)
        graph[v].append(u)

    def dfs(child, parent, graph, a) :
        nonlocal cnt
        for c in graph[child] :
            if c != parent :
                dfs(c, child, graph, a)

        a[parent] += a[child]
        cnt += abs(a[child])

    dfs(0, 0, graph, a)

    return cnt