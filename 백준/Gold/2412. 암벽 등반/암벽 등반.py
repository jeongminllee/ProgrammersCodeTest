from collections import deque

def bfs(si, sj, graph) :
    q = deque()
    q.append((si, sj, 0))

    while q :
        ci, cj, cnt = q.popleft()

        if cj == T :
            return cnt

        for di in range(-2, 3) :
            for dj in range(-2, 3) :
                ni, nj = ci + di, cj + dj
                if (ni, nj) in graph :
                    q.append((ni, nj, cnt + 1))
                    graph.remove((ni, nj))
    return -1

n, T = map(int, input().split())
graph = set()
for _ in range(n) :
    graph.add(tuple(map(int, input().split())))

res = bfs(0, 0, graph)
print(res)