import heapq

INF = float('inf')  # 무한대 값 설정 (거리 초기화용)

def deijkstra(start):
    distances[start] = 0  # 시작 노드의 거리를 0으로 초기화
    q = []
    heapq.heappush(q, (start, 0))  # 우선순위 큐에 시작 노드 추가

    while q:
        node, weight = heapq.heappop(q)  # 현재 노드와 가중치 가져오기

        # 현재 저장된 거리보다 크면 무시 (이미 더 짧은 경로를 처리함)
        if weight > distances[node]:
            continue

        # 현재 노드와 연결된 모든 인접 노드 확인
        for nxt_node, nxt_weight in edges[node]:
            # 새로운 경로가 기존 경로보다 짧으면 업데이트
            if distances[nxt_node] > nxt_weight + weight:
                distances[nxt_node] = nxt_weight + weight  # 거리 갱신
                prev_node[nxt_node] = node  # 경로 추적을 위한 이전 노드 저장
                heapq.heappush(q, (nxt_node, distances[nxt_node]))  # 우선순위 큐에 추가

n = int(input())    # 도시 개수 (노드 수)
m = int(input())    # 버스 개수 (간선 수)

# 그래프 초기화 (1번 노드부터 n번 노드까지 사용)
edges = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, w = map(int, input().split())  # 시작 노드, 끝 노드, 가중치 입력
    edges[s].append((e, w))  # 방향 그래프 간선 추가

start, end = map(int, input().split())  # 시작 노드와 도착 노드 입력

distances = [INF] * (n + 1)  # 모든 노드의 최단 거리를 무한대로 초기화
prev_node = [0] * (n + 1)  # 경로 추적을 위한 이전 노드 정보 초기화

deijkstra(start)  # 다익스트라 알고리즘 실행

print(distances[end])  # 도착 노드까지의 최단 거리 출력

# 최단 경로 역추적
path = [end]
now = end
while now != start:
    now = prev_node[now]  # 이전 노드를 따라가며 경로 추적
    path.append(now)

path.reverse()  # 경로를 역순으로 정렬 (출발 노드부터 표시되도록)

print(len(path))  # 경로에 포함된 노드 수 출력
print(*path)  # 경로 출력
