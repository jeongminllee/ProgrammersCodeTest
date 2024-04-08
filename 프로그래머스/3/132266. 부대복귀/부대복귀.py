from collections import deque

def solution(n, roads, sources, destination):
    # 그래프 초기화
    graph = {i: [] for i in range(1, n + 1)}

    # 양방향 그래프 구성
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    v = [-1] * (n + 1)
    v[destination] = 0
    q = deque()
    q.append(destination)
    while q:
        curr = q.popleft()
        for node in graph[curr] :
            if v[node] == -1 :
                v[node] = v[curr] + 1
                q.append(node)

    return [v[i] for i in sources]