from collections import deque

            
INF = -(10 ** 9)

def bellman(start, end) :
    distances = [INF for _ in range(N)]
    distances[start] = make_money[start]

    for i in range(N - 1) :
        for u, v, w in cities :
            if distances[u] != INF and distances[u] + w > distances[v] :
                distances[v] = distances[u] + w

    if distances[end] == INF :
        return "gg"

    for u, v, w in cities :
        if distances[u] != INF and distances[u] + w > distances[v] :
            if bfs(v, end) :
                return "Gee"

    return distances[end]
    
def bfs(start, end) :
    q = deque()
    q.append(start)
    visited = [0] * N
    visited[start] = 1

    while q :
        cur = q.popleft()
        if cur == end :
            return True

        for u, v, w in cities :
            if u == cur and not visited[v] :
                visited[v] = 1
                q.append(v)

    return False


N, start, end, M = map(int, input().split())
cities = []

for _ in range(M) :
    s, e, p = map(int, input().split())
    cities.append([s, e, -p])   # 주어진 방향으로만 이용 가능

make_money = list(map(int, input().split()))
for i in range(M) :
    cities[i][2] = cities[i][2] + make_money[cities[i][1]]

print(bellman(start, end))