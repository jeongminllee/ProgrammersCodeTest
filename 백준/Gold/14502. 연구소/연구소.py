from collections import deque
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs() :
    q = deque()
    tmp_graph = copy.deepcopy(maps)

    for i in range(n) :
        for j in range(m) :
            if tmp_graph[i][j] == 2 :
                q.append((i, j))

    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and tmp_graph[nx][ny] == 0 :
                tmp_graph[nx][ny] = 2
                q.append((nx, ny))

    global answer
    count_0 = 0
    
    for i in range(n) :
        count_0 += tmp_graph[i].count(0)

    answer = max(answer, count_0)
def makeWall(cnt=0) :
    if cnt == 3 :
        bfs()
        return

    for i in range(n) :
        for j in range(m) :
            if maps[i][j] == 0 :
                maps[i][j] = 1
                makeWall(cnt + 1)
                maps[i][j] = 0


n, m = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(n)]
answer = 0
makeWall()
print(answer)