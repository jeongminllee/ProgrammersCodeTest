from collections import deque

def bfs(start) :
    q = deque()
    q.append((start, 1))

    v_station = [0] * (N + 1)
    v_hyper = [0] * (M + 1)

    v_station[start] = 1

    while q :
        curr, cnt = q.popleft()
        if curr == N :
            return cnt

        for hyper in station[curr] :
            if not v_hyper[hyper] :
                v_hyper[hyper] = 1

                for nxt in hyper_tube[hyper] :
                    if not v_station[nxt] :
                        v_station[nxt] = 1
                        q.append((nxt, cnt + 1))

    return -1

N, K, M = map(int, input().split())

station = [[] for _ in range(N + 1)]
hyper_tube = [[] for _ in range(M + 1)]

for idx in range(M) :
    lst = list(map(int, input().split()))
    hyper_tube[idx] = lst
    for num in lst :
        station[num].append(idx)

print(bfs(1))