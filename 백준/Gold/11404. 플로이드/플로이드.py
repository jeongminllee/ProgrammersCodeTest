INF = float('inf')

def floyd_warshall(bus) :
    distance = [[INF] * n for _ in range(n)]

    for i in range(n) :
        for j in range(n) :
            if i == j :
                distance[i][j] = 0

    for a, b, c in bus :
        distance[a-1][b-1] = min(distance[a-1][b-1], c)

    for k in range(n) :
        for i in range(n) :
            for j in range(n) :
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance

# 도시의 개수
n = int(input())

# 버스의 개수
m = int(input())

# 버스 정보
bus = [list(map(int, input().split())) for _ in range(m)]

res = floyd_warshall(bus)

for i in range(n) :
    for j in range(n) :
        if res[i][j] == INF :
            res[i][j] = 0
    print(*res[i])