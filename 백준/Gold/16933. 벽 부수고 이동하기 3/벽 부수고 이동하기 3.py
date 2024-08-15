from collections import deque
import sys
input = sys.stdin.readline

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(N, M, K, arr, visited) :
    # 큐 초기화
    q = deque()
    q.append((0, 0, 0, 1))       # x, y, broken, 이동거리
    visited[0][0][0] = 1         # x, y, broken

    while q :
        ci, cj, br, dist = q.popleft()

        # 정답처리
        if ci == N - 1 and cj == M - 1 :
            return dist

        for d in range(4) :
            ni, nj = ci + di[d], cj + dj[d]

            # 범위내
            if 0 <= ni < N and 0 <= nj < M :
                # 이동 가능, 미방문
                if arr[ni][nj] == 0 and visited[ni][nj][br] == 0 :
                    visited[ni][nj][br] = 1
                    q.append((ni, nj, br, dist + 1))

                # 벽을 부술 수 있는 횟수가 남아있고, 벽이며, 아직 방문하지 않았다면
                elif arr[ni][nj] == 1 and br < K and visited[ni][nj][br + 1] == 0 :
                    # 낮인 경우
                    if dist % 2 == 1 :
                        visited[ni][nj][br + 1] = 1
                        q.append((ni, nj, br + 1, dist + 1))

                    # 밤인 경우 => 제자리에서 대기
                    else :
                        q.append((ci, cj, br, dist + 1))

    # 목적지에 도달하지 못할 경우
    return -1

N, M, K = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0 for _ in range(K + 1)] for _ in range(M)] for _ in range(N)]
print(bfs(N, M, K, arr, visited))