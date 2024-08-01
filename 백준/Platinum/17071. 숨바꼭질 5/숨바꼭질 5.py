def bfs(N, K, cnt) :
    if N == K :
        return 0
    v = [[INF] * 500001, [INF] * 500001]
    q = [N]
    v[0][N] = 0
    while K + cnt <= 500_000 :
        K += cnt
        n_q = []
        for x in q :
            for nx in [x * 2, x - 1, x + 1] :
                if 0 <= nx < 500001 :
                    if v[cnt % 2][nx] > cnt :
                        v[cnt % 2][nx] = cnt
                        n_q.append(nx)
        q = n_q
        if v[cnt % 2][K] <= cnt :
            return cnt
        cnt += 1
    return -1

INF = float('inf')
N, K = map(int, input().split())
print(bfs(N, K, 1))