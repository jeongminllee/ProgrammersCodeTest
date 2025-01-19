from collections import deque

T = int(input())

for _ in range(T) :
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))

    dp = [0 for _ in range(N + 1)]
    edges_to_fr = [[] for _ in range(N + 1)]
    edges_fr_to = [[] for _ in range(N + 1)]
    incoming = [0 for _ in range(N + 1)]

    for _ in range(K) :
        x, y = map(int, input().split())
        edges_to_fr[y].append(x)
        edges_fr_to[x].append(y)
        incoming[y] += 1

    w = int(input())

    q = deque()

    for i in range(1, N + 1) :
        if incoming[i] == 0 :
            q.append(i)

    while q :
        to = q.popleft()
        frs = edges_to_fr[to]

        if len(frs) == 0:
            dp[to] = D[to]

        else :
            mx_local = 0

            for fr in frs :
                mx_local = max(mx_local, dp[fr])
            dp[to] = D[to] + mx_local

        tos = edges_fr_to[to]
        for to in tos :
            incoming[to] -= 1
            if incoming[to] == 0 :
                q.append(to)

    print(dp[w])
