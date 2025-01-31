# 5931. Cow Beauty Pageant

from collections import deque

def find_spots(grid, N, M) :
    visited = [[0] * M for _ in range(N)]
    spots = []

    def bfs(x, y) :
        q = deque()
        q.append((x, y))
        spot = [(x, y)]

        while q :
            cx, cy = q.popleft()
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and grid[nx][ny] == 'X' :
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    spot.append((nx, ny))
        return spot

    for i in range(N) :
        for j in range(M) :
            if grid[i][j] == 'X' and not visited[i][j] :
                spots.append(bfs(i, j))

    return spots

def min_paint_needed(grid, N, M) :
    spots = find_spots(grid, N, M)
    if len(spots) != 2 :
        return 0    # 이미 하나의 spot으로 연결되어 있음

    spot1, spot2 = spots
    min_dist = float('inf')

    for x1, y1 in spot1 :
        for x2, y2 in spot2 :
            dist = abs(x1 - x2) + abs(y1 - y2) - 1  # 맨해튼 거리에서 1을 빼야 최소 추가 'X' 개수
            min_dist = min(min_dist, dist)

    return min_dist

N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]

print(min_paint_needed(grid, N, M))