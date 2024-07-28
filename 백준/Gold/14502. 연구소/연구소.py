from collections import deque
from copy import deepcopy

# 상하좌우 이동을 위한 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    global answer
    q = deque()
    maps = deepcopy(arr)  # 원본 배열을 변경하지 않기 위해 깊은 복사

    # 초기 바이러스 위치를 큐에 삽입
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 2:
                q.append((i, j))

    # BFS로 바이러스 확산
    while q:
        x, y = q.popleft()
        for d in range(4):  # 4방향 탐색
            nx, ny = x + dx[d], y + dy[d]

            # 맵 범위 내이고 빈 칸인 경우
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 0:
                maps[nx][ny] = 2  # 바이러스 확산
                q.append((nx, ny))

    # 안전 영역(0) 개수 세기
    cnt_0 = 0
    for i in range(N):
        cnt_0 += maps[i].count(0)

    # 최대 안전 영역 크기 갱신
    answer = max(answer, cnt_0)


def makeWall(cnt=0):
    if cnt == 3:  # 벽 3개를 모두 세웠으면
        bfs()  # 바이러스 확산 시뮬레이션 실행
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:  # 빈 칸인 경우
                arr[i][j] = 1  # 벽 세우기
                makeWall(cnt + 1)  # 재귀적으로 다음 벽 세우기
                arr[i][j] = 0  # 백트래킹: 벽 다시 제거


# 입력 받기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0

# 모든 가능한 벽 조합 시도
makeWall()

# 결과 출력
print(answer)