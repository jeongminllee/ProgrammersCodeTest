from collections import deque

def pour(x, y) :
    if not visited[x][y] :
        visited[x][y] = 1
        q.append((x, y))

def bfs() :
    while q :
        a, b = q.popleft()
        nc = C - a - b

        if a == 0 :
            res.append(nc)

        water = min(a, B - b)
        pour(a - water, b + water)

        water = min(a, C - nc)
        pour(a - water, b)

        water = min(b, C - nc)
        pour(a, b - water)

        water = min(nc, A - a)
        pour(a + water, b)

        water = min(nc, B - b)
        pour(a, b + water)

A, B, C = map(int, input().split())

q = deque()
q.append((0, 0))

visited = [[0] * (B + 1) for _ in range(A + 1)]
visited[0][0] = 1

res = []
bfs()
res.sort()
print(*res)