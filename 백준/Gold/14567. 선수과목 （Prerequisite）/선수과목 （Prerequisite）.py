# N : 과목의 수, M : 선수 조건의 수
N, M = map(int, input().split())

# 선수 조건 그래프 및 진입 차수 배열 초기화
graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)

# 선수 조건 입력 처리
for _ in range(M) :
    A, B = map(int, input().split())
    graph[A].append(B)
    in_degree[B] += 1

# 위상 정렬 수행
q = []
res = [0] * (N + 1)

# 진입 차수가 0인 노드부터 시작
for i in range(1, N + 1) :
    if in_degree[i] == 0 :
        q.append(i)
        res[i] = 1  # 첫 학기부터 수강 가능

while q :
    curr = q.pop(0)

    for neighbor in graph[curr] :
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0 :
            q.append(neighbor)
            res[neighbor] = res[curr] + 1

print(*res[1:])