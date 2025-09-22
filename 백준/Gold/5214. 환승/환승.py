# 그냥 BFS 하면 메모리 초과가 나옴.
# 역 - 하이퍼튜브 - 역 으로 방문하는 구조를 만들어야 된다.
# 그 말은 하이퍼 튜브 배열과 역 배열을 따로 만들어서 관리하고
# visited 배열 역시 따로 만들어서 관리.

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

    # 도달하지 못한다면
    return -1

N, K, M = map(int, input().split()) # 역, 하이퍼 튜브가 연결하는 역 개수, 하이퍼 튜브
station = [[] for _ in range(N + 1)]    # 1-idx
hyper_tube = [[] for _ in range(M + 1)]

for idx in range(M) :
    lst = list(map(int, input().split()))
    hyper_tube[idx] = lst
    for num in lst :
        station[num].append(idx)

res = bfs(1)
print(res)