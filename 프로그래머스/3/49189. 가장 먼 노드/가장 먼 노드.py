# 1번 노드가 루트 노드 => 에서 가장 먼 노드를 찾아라
from collections import deque

def bfs(graph, start, distance) :
    q = deque([1])  # BFS를 위한 queue, 출발 노드 = 1
    distance[1] = 0  # 출발 노드의 최단 거리를 0으로

    # BFS 수행
    while q:
        curr = q.popleft()  # 현재 노드

        # 현재 노드에서 이동할 수 있는 모든 노드 확인
        for i in graph[curr]:
            if distance[i] == -1:  # 아직 방문하지 않은 노드라면,
                q.append(i)  # q에 추가
                distance[i] = distance[curr] + 1  # 최단 거리 갱신

def solution(n, edge):
    answer = 0

    # 연결된 노드 정보
    graph = [[] for _ in range(n + 1)]
    # 각 노드의 최단 거리 리스트
    distance = [-1] * (n + 1)

    # 연결된 노드 정보 추가
    for e in edge :
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])    # 양방향

    bfs(graph, 1, distance)

    # 가장 멀리 떨어진 노드 개수 구하기
    for d in distance :
        if d == max(distance) :
            answer += 1

    return answer