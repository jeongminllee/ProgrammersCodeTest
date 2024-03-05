from collections import deque

T = int(input())

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS
def bfs(x, y) :
    q = deque()    # deque를 이용하겠다. Queue 자료구조 
    q.append((x, y))    # 초기 데이터(들) 입력

    while q :
        x, y = q.popleft()    # 데이터를 가져와서

        for i in range(4) :    # 해당 데이터의 다음 데이터를 상하좌우로 움직인 다음,
            nx = x + dx[i]
            ny = y + dy[i]

            # 상하좌우, 범위 내, 미방문
            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 1 and v[nx][ny] == 0 :
                v[nx][ny] = 1        # 방문 표시
                q.append((nx, ny))   # 다음 데이터 삽입.

# 데이터 입력
for _ in range(T) :
    m, n, k = map(int, input().split())
    arr = [[0] * n for _ in range(m)]   # 배추 심어져있는 배열
    v = [[0] * n for _ in range(m)]     # 배추 심어져 있는 배열을 방문했는지에 대한 여부 판단 배열
    cnt = 0                             # 그래서 지렁이 몇마리 필요한대?

    for _ in range(k) :
        x, y = map(int, input().split())
        arr[x][y] = 1                   # (x, y) 좌표에 1로 입력

    for a in range(m) :
        for b in range(n) :
            # arr 배열에 배추가 심어져 있고 방문하지 않았다면?
            if arr[a][b] == 1 and v[a][b] == 0 :
                bfs(a, b)    # BFS 돌려
                cnt += 1    # 지렁이 수 추가

    print(cnt)