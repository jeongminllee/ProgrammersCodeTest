# 깊이 우선 탐색(DFS)을 사용하여 트리의 지름을 찾는 함수
# n: 노드의 총 개수, e: 시작 노드, flag: 최대 거리 노드 찾기 여부를 결정하는 플래그
def dfs(n, e, flag) :
    # 모든 노드의 거리를 -1로 초기화 (방문하지 않은 상태)
    distance = [-1] * (n + 1)
    
    # 스택에 시작 노드와 초기 거리(0) 추가
    stack = [(e, 0)]
    
    # 스택이 빌 때까지 탐색 진행
    while stack :
        # 현재 노드와 현재까지의 거리를 스택에서 pop
        e, d = stack.pop()
        
        # 현재 노드의 거리 갱신
        distance[e] = d
        
        # 현재 노드와 연결된 모드 인접 노드 탐색
        for node, weight in graph[e] :
            # 아직 방문하지 않은 노드인 경우
            if distance[node] == -1 :
                # 스택에 인접 노드와 거리 추가 (현재 거리 + 간선 가중치)
                stack.append((node, d + weight))
    
    # flag가 True일 경우: 가장 먼 노드의 인덱스 반환
    if flag :
        x = 0
        for i in range(1, n + 1) :
            # 현재까지 가장 먼 노드 찾기
            if distance[x] < distance[i] :
                x = i
        return x
    
    # flag가 False일 경우: 최대 거리 반환
    return max(distance)

# 트리의 노드 개수 입력
n = int(input())

# 그래프를 인접 리스트로 초기화
graph = [[] for _ in range(n + 1)]

# 트리의 간선 정보 입력 (부모-자식-가중치)
for _ in range(1, n) :
    parent, child, weight = map(int, input().split())
    # 양방향 그래프로 간선 추가
    graph[parent].append((child, weight))
    graph[child].append((parent, weight))

# 트리의 지름 계산
# 1. 첫 번째 DFS로 트리에서 가장 먼 노드 찾기
# 2. 그 노드에서 다시 DFS를 수행하여 트리의 지름 계산
print(dfs(n, dfs(n, 1, True), False))