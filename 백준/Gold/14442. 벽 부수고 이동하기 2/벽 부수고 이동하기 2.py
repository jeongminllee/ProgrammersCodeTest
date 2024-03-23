from collections import deque

def bfs(N, M, K, arr, visited) :
    # BFS 시작 설정
    q = deque()
    q.append((0, 0, 0))     # (x, y, broken)
    visited[0][0][0] = 1    # 시작 지점 방문 처리

    # 방향 벡터 (상 하 좌 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # BFS 실행
    while q :
        x, y, br = q.popleft()

        # 종료 조건
        if x == N - 1 and y == M - 1 :
            return visited[x][y][br]

        # 상하좌우 이동
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]

            # arr의 범위를 벗어나지 않고
            if 0 <= nx < N and 0 <= ny < M :
                # 이동할 수 있는 칸이고 아직 방문하지 않았다면
                if arr[nx][ny] == 0 and visited[nx][ny][br] == 0 :
                    visited[nx][ny][br] = visited[x][y][br] + 1
                    q.append((nx, ny, br))

                # 벽을 부술 수 있는 횟수가 남아있고, 벽이며, 아직 방문하지 않았다면
                elif arr[nx][ny] == 1 and br < K and visited[nx][ny][br + 1] == 0 :
                    visited[nx][ny][br + 1] = visited[x][y][br] + 1
                    q.append((nx, ny, br + 1))
    # 목표 지점에 도달하지 못할 경우
    return -1

N, M, K = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

# 방문 배열 초기화 (벽을 부순 횟수에 따라 다른 상태를 저장)
visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
print(bfs(N, M, K, arr, visited))