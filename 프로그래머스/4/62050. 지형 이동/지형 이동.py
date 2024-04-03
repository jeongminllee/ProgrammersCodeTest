import heapq

def solution(land, height):
    answer = 0
    n = len(land)
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    v = [[0] * n for _ in range(n)]

    q = []
    heapq.heappush(q, [0, 0, 0])    # 비용, i, j

    while q:
        cost, i, j = heapq.heappop(q)
        if not v[i][j]:
            v[i][j] = 1

            answer += cost
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]

                if 0 <= ni < n and 0 <= nj < n:
                    tmp_cost = abs(land[i][j] - land[ni][nj])
                    if tmp_cost > height:
                        new_cost = tmp_cost
                    else:
                        new_cost = 0

                    heapq.heappush(q, [new_cost, ni, nj])

    return answer