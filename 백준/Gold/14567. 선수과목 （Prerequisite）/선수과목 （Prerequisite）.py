from collections import deque

def calculate_min_semesters(N, M, prerequisites):
    # 그래프와 진입 차수 초기화
    graph = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1)
    
    for A, B in prerequisites:
        graph[A].append(B)
        in_degree[B] += 1
    
    # 큐 초기화 및 학기 저장 리스트
    queue = deque()
    semesters = [0] * (N + 1)
    
    # 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            queue.append(i)
            semesters[i] = 1  # 첫 학기에 들을 수 있음
    
    # 위상 정렬 수행
    while queue:
        current = queue.popleft()
        for next_course in graph[current]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)
                semesters[next_course] = semesters[current] + 1
    
    # 결과 반환
    return semesters[1:]  # 1번 과목부터 N번 과목까지

# 입력 처리
N, M = map(int, input().split())
prerequisites = [tuple(map(int, input().split())) for _ in range(M)]

# 결과 계산
result = calculate_min_semesters(N, M, prerequisites)

# 결과 출력
print(" ".join(map(str, result)))
