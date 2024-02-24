from collections import deque

def solution(maps) :
    n, m = len(maps), len(maps[0])
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    dist = [[-1] * m for _ in range(n)]

    def bfs(start) :
        q = deque([start])
        dist[start[0]][start[1]] = 1

        while q :
            cur = q.popleft()

            for d in direction :
                x, y = cur[0] + d[0], cur[1] + d[1]

                if x < 0 or x >= n or y < 0 or y >= m :
                    continue
                if maps[x][y] == 0 :
                    continue

                if dist[x][y] == -1 :
                    q.append([x, y])
                    dist[x][y] = dist[cur[0]][cur[1]] + 1

        return dist
    bfs([0, 0])

    return dist[n - 1][m - 1]

# from heapq import heappush, heappop
# import sys
# 
# 
# def DFS(maps, cr, cc, R, C):
#     cv = maps[cr][cc]
#     for rd, cd in ((-1, 0), (0, 1), (1, 0), (0, -1)):  # URDL
#         nr, nc = cr + rd, cc + cd
#         if nr in range(R) and nc in range(C) and cv + 1 < maps[nr][nc]:
#             maps[nr][nc] = cv + 1
#             DFS(maps, nr, nc, R, C)
# 
# 
# def BFS(maps, cr, cc, R, C):
#     QUEUE = []
#     heappush(QUEUE, (1, 0, 0))  # 몇칸, row, col
# 
#     while QUEUE:
#         cv, cr, cc = heappop(QUEUE)
#         for rd, cd in ((-1, 0), (0, 1), (1, 0), (0, -1)):
#             nr, nc = cr + rd, cc + cd
#             if nr in range(R) and nc in range(C) and maps[nr][nc]:
#                 if cv + 1 < maps[nr][nc]:
#                     maps[nr][nc] = cv + 1
#                     heappush(QUEUE, (maps[nr][nc], nr, nc))
# 
# 
# def solution(maps):
#     R, C = len(maps), len(maps[0])
#     maps = [[float("inf") if maps[r][c] else 0 for c in range(C)] for r in range(R)]
#     maps[0][0] = 1
# 
#     sys.setrecursionlimit(10000)
#     DFS(maps, 0, 0, R, C)
#     # BFS(maps, 0, 0, R, C)
# 
#     return -1 if maps[R - 1][C - 1] == float("inf") else maps[R - 1][C - 1]