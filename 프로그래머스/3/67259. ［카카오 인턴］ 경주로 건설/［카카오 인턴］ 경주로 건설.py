from collections import deque

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

def solution(board):
    n = len(board)
    costs = [[[1<<32] * 2 for _ in range(n)] for _ in range(n)]
    
    q = deque()
    q.append(((0, 0), 0, -1))   # (x, y), cost, direction
    costs[0][0] = [0, 0]
    
    while q :
        (i, j), cost, direction = q.popleft()
        
        for d in range(4) :
            ni, nj = i + di[d], j + dj[d]
            new_direction = d % 2
            
            if 0 <= ni < n and 0 <= nj < n and board[ni][nj] == 0 :
                if direction != new_direction and direction != -1 :
                    new_cost = cost + 600
                else :
                    new_cost = cost + 100
                    
                if costs[ni][nj][new_direction] > new_cost :
                    costs[ni][nj][new_direction] = new_cost
                    q.append(((ni, nj), new_cost, new_direction))
                    
    return min(costs[-1][-1])

# def solution(board):
#     N = len(board)
#     costs = [[[float('inf')] * 2 for _ in range(N)] for _ in range(N)]  # 각 위치의 최소 비용을 저장하는 3차원 배열
#     costs[0][0] = [0, 0]
#     queue = deque([((0, 0), 0, -1)])  # ((x, y), cost, direction) (-1: 시작, 0: 수평, 1: 수직)

#     while queue:
#         (x, y), cost, direction = queue.popleft()
#         for dx, dy, new_direction in ((0, 1, 0), (1, 0, 1), (0, -1, 0), (-1, 0, 1)):  # 우, 하, 좌, 상 순서
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
#                 new_cost = cost + 600 if direction != new_direction and direction != -1 else cost + 100  # 방향이 바뀌면 코너 비용 추가
#                 if costs[nx][ny][new_direction] > new_cost:
#                     costs[nx][ny][new_direction] = new_cost
#                     queue.append(((nx, ny), new_cost, new_direction))
#     return min(costs[-1][-1])


# def solution(board) :
#     # 1. 주어진 좌표가 보드의 범위 내에 있는지 확인
#     def is_valid(x, y) :
#         return 0 <= x < n and 0 <= y < n

#     # 2. 주어진 좌표가 차단되었거나 이동할 수 있는지 확인
#     def is_blocked(x, y) :
#         return (x, y) == (0, 0) or not is_valid(x, y) or board[x][y] == 1

#     # 3. 이전 방향과 현재 방향에 따라 비용 계산
#     def calculate_cost(direction, prev_direction, cost) :
#         if prev_direction == -1 or (prev_direction - direction) % 2 == 0 :
#             return cost + 100
#         else :
#             return cost + 600

#     # 4. 주어진 좌표와 방향이 아직 방문하지 않았거나 새 비용이 더 적은 경우
#     def isShouldUpdate(x, y, direction, new_cost) :
#         return visited[x][y][direction] == 0 or visited[x][y][direction] > new_cost

#     queue = deque([((0, 0), -1, 0)])
#     n = len(board)
#     directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
#     visited = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(n)]
#     answer = float('inf')

#     # 5. 큐가 빌 때까지 반복
#     while queue :
#         (x, y), prev_direction, cost = queue.popleft()

#         # 6. 가능한 모든 방향에 대해 반복
#         for direction, (dx, dy) in enumerate(directions) :
#             nx, ny = x + dx, y + dy

#             # 7. 이동할 수 없는 좌표는 건너뛰기
#             if is_blocked(nx, ny) :
#                 continue

#             new_cost = calculate_cost(direction, prev_direction, cost)

#             # 8. 도착지에 도달한 경우 최소 비용 업데이트
#             if (nx, ny) == (n - 1, n - 1) :
#                 answer = min(answer ,new_cost)

#             # 9. 좌표와 방향이 아직 방문하지 않았거나 새 비용이 더 작은 경우 큐에 추가
#             elif isShouldUpdate(nx, ny, direction, new_cost) :
#                 queue.append(((nx, ny), direction, new_cost))
#                 visited[nx][ny][direction] = new_cost

#     return answer