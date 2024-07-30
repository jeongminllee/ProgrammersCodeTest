from collections import defaultdict

def dfs(graph, node, parent):
    cnt = 1
    for child in graph[node]:
        if child != parent:
            cnt += dfs(graph, child, node)
    return cnt

def solution(n, wires):
    graph = defaultdict(list)
    for v1, v2 in wires :
        graph[v1].append(v2)
        graph[v2].append(v1)

    answer = n
    for v1, v2 in wires:
        graph[v1].remove(v2)
        graph[v2].remove(v1)

        answer = min(answer, abs(n - dfs(graph, v1, v2) * 2))

        graph[v1].append(v2)
        graph[v2].append(v1)

    return answer