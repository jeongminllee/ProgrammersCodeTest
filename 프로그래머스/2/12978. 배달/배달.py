# n은 마을 개수
# k는 k시간 이하로 배달이 가능한 마을에서만 주문을 받으려고 함.
# 1번 마을에서 배달이 가능한 총 마을 갯수를 선정하여라.
# 최소 비용을 알려주는 다익스트라 알고리즘을 활용하면 될 듯.
# 그런다음 최소 비용을 구하고 1번 마을에서 해당 마을까지의 최소 비용이 k 이하인 마을의 개수를 모두 구함.
import heapq

def dijkstra(V, edges, src):
    distance = [float('inf')] * (V+1)  # 인덱스를 1부터 사용하기 위해 V+1 크기의 리스트를 생성합니다.
    distance[src] = 0

    graph = [[] for _ in range(V+1)]  # 인덱스를 1부터 사용하기 위해 V+1 크기의 리스트를 생성합니다.
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))  # 도로가 양방향이므로 u에서 v로 가는 길과 v에서 u로 가는 길을 모두 추가합니다.

    pq = [(0, src)]
    while pq:
        dist, node = heapq.heappop(pq)

        if dist > distance[node]:
            continue

        for neighbor, weight in graph[node]:
            if dist + weight < distance[neighbor]:
                distance[neighbor] = dist + weight
                heapq.heappush(pq, (distance[neighbor], neighbor))

    return distance


def solution(N, road, K):
    result = dijkstra(N, road, 1)

    answer = sum(1 for dist in result if dist <= K)
    return answer