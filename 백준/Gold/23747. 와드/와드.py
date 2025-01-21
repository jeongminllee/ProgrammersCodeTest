from collections import deque

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

sr, sc = map(int, input().split())
sr, sc = sr - 1, sc - 1

cmd = list(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for c in cmd :
    if c == 'W' :
        q = deque()
        area_seperator = board[sr][sc]
        if area_seperator == '.' :
            continue
        q.append((sr, sc))
        board[sr][sc] = '.'
        while q :
            cr, cc = q.popleft()
            for d in range(4) :
                nr, nc = cr + dr[d], cc + dc[d]
                if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == area_seperator :
                    board[nr][nc] = '.'
                    q.append((nr, nc))

    elif c == 'U' :
        sr -= 1
    elif c == 'D' :
        sr += 1
    elif c == 'L' :
        sc -= 1
    elif c == 'R' :
        sc += 1

board[sr][sc] = '.'
for d in range(4) :
    nr, nc = sr + dr[d], sc + dc[d]
    if 0 <= nr < R and 0 <= nc < C :
        board[nr][nc] = '.'

for row in range(R) :
    for col in range(C) :
        if board[row][col] != '.' :
            print('#', end='')

        else :
            print('.', end='')
    print()