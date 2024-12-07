INF = 500 * 2500 * 200 + 1

def bf() :
    for i in range(N) :
        for j in range(len(edges)) :
            curr, nxt, cost = edges[j]
            if distance[nxt] > distance[curr] + cost :
                distance[nxt] = distance[curr] + cost
                if i == N - 1 :
                    return True
    return False

T = int(input())

for _ in range(T) :
    N, M, W = map(int, input().split())
    edges = []
    distance = [INF] * (N + 1)
    for i in range(M + W) :
        S, E, T = map(int, input().split())
        if i >= M :
            T = -T
        else :
            edges.append((E, S, T))
        edges.append((S, E, T))

    if bf() :
        print("YES")
    else :
        print("NO")