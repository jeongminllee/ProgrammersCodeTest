di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

from collections import deque

def is_valid(i, j) :
    return 0 <= i < N and 0 <= j < M

def min_paint_to_merge_spots(n, m) :
    if len(spots) != 2 :
        return 0

    spot1, spot2 = spots[0], spots[1]
    min_distance = n*m

    for (x1, y1) in spot1 :
        for (x2, y2) in spot2 :
            distance = abs(x1 - x2) + abs(y1 - y2) - 1
            min_distance = min(min_distance, distance)

    return min_distance



N, M = map(int, input().split())
grid = [input().strip() for _ in range(N)]

spots = []
visited = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if grid[i][j] == 'X' and not visited[i][j]:
            spot = []
            q = deque()
            q.append((i, j))
            visited[i][j] = 1

            while q:
                ci, cj = q.popleft()
                spot.append((ci, cj))

                for d in range(4):
                    ni, nj = ci + di[d], cj + dj[d]
                    if is_valid(ni, nj) and grid[ni][nj] == 'X' and not visited[ni][nj]:
                        visited[ni][nj] = 1
                        q.append((ni, nj))

            spots.append(spot)

print(min_paint_to_merge_spots(N, M))