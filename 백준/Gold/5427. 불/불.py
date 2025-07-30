di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

from collections import deque

# 0: 방문하지 않음 , 1: 상근이 방문함, 2: 불이 방문함
def bfs(f_s, q, visited) :  # 불인지 상근인지 파악
    while q :
        ci, cj, time = q.popleft()
        for d in range(4) :
            ni, nj = ci + di[d], cj + dj[d]
            if 0 <= ni < h and 0 <= nj < w :
                if arr[ni][nj] == '.' or arr[ni][nj] == '@' :
                    if visited[ni][nj] > time + 1 :
                        visited[ni][nj] = time + 1
                        q.append((ni, nj, visited[ni][nj]))
            elif f_s == 's' :   # 상근이면 w, h를 벗어나는 순간 스탑
                print(time + 1)
                return
    if f_s == 's' :
        print('IMPOSSIBLE')


T = int(input())
for _ in range(T) :
    w, h = map(int, input().split())
    arr = [list(input()) for _ in range(h)]
    visited = [[1e9] * w for _ in range(h)]

    fq = deque()
    sq = deque()

    for i in range(h) :
        for j in range(w) :
            if arr[i][j] == '@' :   # 상근이 시작 위치
                sq.append((i, j, 0))
            elif arr[i][j] == '*' : # 불 위치
                visited[i][j] = 0
                fq.append((i, j, 0))

    # 불 먼저
    bfs('f', fq, visited)
    bfs('s', sq, visited)