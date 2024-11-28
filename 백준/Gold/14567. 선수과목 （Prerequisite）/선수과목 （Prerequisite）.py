from collections import deque

# N : 과목의 수, M : 선수 조건의 수
N, M = map(int, input().split())

# 선수 조건 그래프 및 진입 차수 배열 초기화
graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)

# 선수 조건 입력 처리
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    in_degree[B] += 1

# 위상 정렬 수행
queue = deque()
result = [0] * (N + 1)

# 진입 차수가 0인 노드부터 시작
for i in range(1, N + 1):
    if in_degree[i] == 0:
        queue.append(i)
        result[i] = 1  # 첫 학기부터 수강 가능

while queue:
    current = queue.popleft()
    
    for neighbor in graph[current]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.append(neighbor)
            result[neighbor] = result[current] + 1

# 결과 출력
print(*result[1:])
