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