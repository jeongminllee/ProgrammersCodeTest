from collections import deque

def solution(board):
    N = len(board)
    costs = [[[float('inf')] * 2 for _ in range(N)] for _ in range(N)]  # 각 위치의 최소 비용을 저장하는 3차원 배열
    costs[0][0] = [0, 0]
    queue = deque([((0, 0), 0, -1)])  # ((x, y), cost, direction) (-1: 시작, 0: 수평, 1: 수직)

    while queue:
        (x, y), cost, direction = queue.popleft()
        for dx, dy, new_direction in ((0, 1, 0), (1, 0, 1), (0, -1, 0), (-1, 0, 1)):  # 우, 하, 좌, 상 순서
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                new_cost = cost + 600 if direction != new_direction and direction != -1 else cost + 100  # 방향이 바뀌면 코너 비용 추가
                if costs[nx][ny][new_direction] > new_cost:
                    costs[nx][ny][new_direction] = new_cost
                    queue.append(((nx, ny), new_cost, new_direction))
    return min(costs[-1][-1])