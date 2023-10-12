from heapq import heappush, heappop

def solution(maps) :
    R, C = len(maps), len(maps[0])
    maps = [[float("inf") if maps[r][c] else 0 for c in range(C)] for r in range(R)]

    maps[0][0] = 1
    QUEUE = []
    heappush(QUEUE, (1, 0, 0))  # 몇칸, row, col

    while QUEUE :
        cv, cr, cc = heappop(QUEUE)
        for rd, cd in ((-1, 0), (0, 1), (1, 0), (0, -1)) :
            nr, nc = cr + rd, cc + cd
            if nr in range(R) and nc in range(C) and maps[nr][nc] :
                if cv + 1 < maps[nr][nc] :
                    maps[nr][nc] = cv + 1
                    heappush(QUEUE, (maps[nr][nc], nr, nc))

    return -1 if maps[R-1][C-1] == float("inf") else maps[R-1][C-1]