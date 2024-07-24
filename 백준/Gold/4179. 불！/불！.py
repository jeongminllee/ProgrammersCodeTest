from collections import deque

def solve_maze(R, C, maze) :
    # 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # Joe와 불의 초기 위치 찾기
    jq, fq = deque(), deque()
    for i in range(R) :
        for j in range(C) :
            if maze[i][j] == 'J' :
                jq.append((i, j, 0))
            elif maze[i][j] == 'F' :
                fq.append((i, j))

    fire_time = [[float('inf')] * C for _ in range(R)]
    for i, j in fq :
        fire_time[i][j] = 0

    # 불 번짐 시뮬레이션
    while fq :
        i, j = fq.popleft()

        for d in range(4) :
            ni, nj = i + di[d], j + dj[d]

            if 0 <= ni < R and 0 <= nj < C and maze[ni][nj] != '#' and fire_time[ni][nj] == float('inf') :
                fire_time[ni][nj] = fire_time[i][j] + 1
                fq.append((ni, nj))

    visited = [[0] * C for _ in range(R)]
    while jq :
        i, j, time = jq.popleft()

        # 정답처리
        if i == 0 or i == R - 1 or j == 0 or j == C - 1:
            return time + 1

        for d in range(4) :
            ni, nj = i + di[d], j + dj[d]

            if 0 <= ni < R and 0 <= nj < C and maze[ni][nj] != '#' and visited[ni][nj] == 0 :
                if time + 1 < fire_time[ni][nj] :
                    visited[ni][nj] = 1
                    jq.append((ni, nj, time + 1))

    return "IMPOSSIBLE"

R, C = map(int, input().split())
maze = [input().strip() for _ in range(R)]

print(solve_maze(R, C, maze))