from collections import deque
from copy import deepcopy

n, m = map(int, input().split())    # n : 세로, m : 가로
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0

# 벽을 꼭 3개를 세우자
def make_wall(cnt=0) :
    if cnt == 3 :
        bfs()
        return
    for i in range(n) :
        for j in range(m) :
            if board[i][j] == 0 :
                board[i][j] = 1
                make_wall(cnt + 1)
                board[i][j] = 0

def bfs() :
    global ans
    q = deque()
    maps = deepcopy(board)

    for i in range(n) :
        for j in range(m) :
            if maps[i][j] == 2 :
                q.append((i, j))

    while q :
        x, y = q.popleft()

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 0 :
                maps[nx][ny] = 2
                q.append((nx, ny))

    cnt_0 = 0
    for i in range(n) :
        cnt_0 += maps[i].count(0)

    ans = max(ans, cnt_0)

make_wall()
print(ans)