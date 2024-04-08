from collections import deque

def solution(n, roads, sources, destination):
    # 그래프 초기화: 각 지역 번호를 키로, 연결된 지역 목록을 값으로 하는 딕셔너리 생성
    graph = {i: [] for i in range(1, n + 1)}

    # 양방향 그래프 구성: roads 배열을 순회하며 각 도로 정보를 바탕으로 그래프에 양방향 연결 추가
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    # visited 배열(v) 초기화: 모든 지역을 -1(방문하지 않음)으로 초기화. destination은 0으로 초기화(출발 지점)
    v = [-1] * (n + 1)
    v[destination] = 0  # 목적지에서 목적지로의 거리는 0
    
    # BFS를 위한 큐 생성 및 목적지를 큐에 추가
    q = deque()
    q.append(destination)

    # BFS 실행: 큐가 빌 때까지 반복
    while q:
        curr = q.popleft()  # 큐에서 현재 위치를 꺼냄
        for node in graph[curr]:  # 현재 위치에서 이동 가능한 모든 지역에 대해
            if v[node] == -1:  # 아직 방문하지 않은 지역이라면
                v[node] = v[curr] + 1  # 현재 위치에서 1만큼 더 멀리 있는 것으로 거리 정보 업데이트
                q.append(node)  # 해당 지역을 큐에 추가하여 나중에 탐색하도록 함

    # 결과 반환: sources 배열의 각 원소에 대해, 해당 지역에서 목적지까지의 최단 거리를 v 배열에서 조회하여 반환
    return [v[i] for i in sources]

