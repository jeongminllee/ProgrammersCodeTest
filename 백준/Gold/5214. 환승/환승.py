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

        nxt_hyper = []
        for hyper_idx in station[curr] :
            if not v_hyper[hyper_idx] :
                nxt_hyper.append(hyper_idx)
                v_hyper[hyper_idx] = 1

        for hyper in nxt_hyper :
            for station_idx in hyper_tube[hyper] :
                if not v_station[station_idx] :
                    v_station[station_idx] = 1
                    q.append((station_idx, cnt + 1))

    return -1


N, K, M = map(int, input().split()) # 역 수, 도로 개수, 도로 수
start = 1

station = [[] for _ in range(N+1)]
hyper_tube = [[] for _ in range(M+1)]
for idx in range(M) :
    lst = list(map(int, input().split()))
    for num in lst :
        station[num].append(idx)
        hyper_tube[idx].append(num)

res = bfs(start)
print(res)