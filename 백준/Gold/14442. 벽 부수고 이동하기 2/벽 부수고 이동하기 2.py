from collections import deque

# 입력 받기
N, M, K = map(int, input().split())
map = [list(map(int, list(input().strip()))) for _ in range(N)]

# 방문 배열 초기화 (벽을 부순 횟수에 따라 다른 상태를 저장)
visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]

# BFS를 위한 시작 상태 설정
queue = deque([(0, 0, 0)])  # (x좌표, y좌표, 부순 벽의 개수)
visited[0][0][0] = 1  # 시작 지점을 방문 처리

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 실행
while queue:
    x, y, broken = queue.popleft()

    # 목표 지점에 도달했다면 중단
    if x == N - 1 and y == M - 1:
        print(visited[x][y][broken])
        break

    # 상하좌우 이동
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        # 맵의 범위를 벗어나지 않고
        if 0 <= nx < N and 0 <= ny < M:
            # 이동할 수 있는 칸이고 아직 방문하지 않았다면
            if map[nx][ny] == 0 and visited[nx][ny][broken] == 0:
                visited[nx][ny][broken] = visited[x][y][broken] + 1
                queue.append((nx, ny, broken))
            # 벽을 부술 수 있는 횟수가 남아있고, 벽이며, 아직 방문하지 않았다면
            elif map[nx][ny] == 1 and broken < K and visited[nx][ny][broken + 1] == 0:
                visited[nx][ny][broken + 1] = visited[x][y][broken] + 1
                queue.append((nx, ny, broken + 1))

# 목표 지점에 도달하지 못한 경우
else:
    print(-1)
