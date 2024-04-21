from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(p) :
    start = []
    for i in range(5) : # 시작점이 되는 P좌표 구하기
        for j in range(5) :
            if p[i][j] == 'P' :
                start.append((i, j))

    for s in start :
        q = deque()
        q.append(s)
        v = [[0] * 5 for _ in range(5)] # 방문 처리 리스트
        d = [[0] * 5 for _ in range(5)] # 경로 길이 리스트
        v[s[0]][s[1]] = 1

        while q :
            x, y = q.popleft()

            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<5 and 0<=ny<5 and v[nx][ny] == 0 :
                    if p[nx][ny] == 'O' :
                        q.append((nx, ny))
                        v[nx][ny] = 1
                        d[nx][ny] = d[x][y] + 1

                    if p[nx][ny] == "P" and d[x][y] <= 1 :
                        return 0
    return 1

def solution(places):
    answer = []

    for i in places :
        answer.append(bfs(i))

    return answer