# def find(parent, i) :
#     # 'i'가 속한 집합의 루트 노드 찾기
#     if parent[i] == i :
#         return i
#     # 경로 압축 : 'i'의 부모를 직접 루트로 설정
#     parent[i] = find(parent, parent[i])
#     return parent[i]

# def union(parent, rank, x, y) :
#     # 랭크를 기준으로 두 집합을 합치기
#     xroot = find(parent, x)
#     yroot = find(parent, y)

#     if rank[xroot] < rank[yroot] :
#         # 작은 랭크의 트리를 큰 랭크의 트리 아래에 연결
#         parent[xroot] = yroot
#     elif rank[xroot] > rank[yroot] :
#         parent[yroot] = xroot
#     else :
#         # 랭크가 같은 경우, 한 트리를 다른 트리에 붙이고 랭크 증가
#         parent[yroot] = xroot
#         rank[xroot] += 1
# def solution(n, costs):
#     # 비용을 기준으로 간선을 오름차순으로 정렬
#     costs.sort(key=lambda x:x[2])

#     # 각 노드의 부모를 추적하는 parent 배열 생성
#     parent = [i for i in range(n)]

#     # 각 노드의 트리의 랭크를 추적하는 rank 배열 생성
#     rank = [0] * n

#     min_cost = 0    # 최소 산장 트리의 총 비용
#     edges = 0       # 최소 신장 트리에 포함된 간선의 개수

#     for edge in costs :
#         if edges == n - 1:
#             # n - 1개의 간선이 포함된 경우 중단(최소 신장 트리의 속성)
#             break

#         # 현재 간선의 두 노드가 속한 집합의 루트 찾기
#         x = find(parent, edge[0])
#         y = find(parent, edge[1])

#         if x != y :
#             # 두 노드가 서로 다른 집합에 속한 경우, 집합 합치기
#             union(parent, rank, x, y)
#             # 현재 간선의 비용을 최소 비용에 추가
#             min_cost += edge[2]
#             # 포함된 간선의 개수 증가
#             edges += 1

#     return min_cost

def ancestor(node, parents):
    if parents[node] == node:
        return node  # 자신이 루트 노드일 경우 자신을 반환
    else:
        return ancestor(parents[node], parents)  # 재귀적으로 루트 노드를 찾아 반환

def solution(n, costs):
    answer = 0  # 최종 비용을 저장할 변수 초기화
    edges = sorted([(x[2], x[0], x[1]) for x in costs])  # 비용을 기준으로 간선을 오름차순 정렬
    parents = [i for i in range(n)]  # 각 노드의 부모 노드를 초기화 (자기 자신을 부모로 설정)
    bridges = 0  # 연결된 다리(간선)의 수 초기화
    
    for w, f, t in edges:  # 정렬된 간선 리스트를 순회
        if ancestor(f, parents) != ancestor(t, parents):  # 두 노드의 루트 노드가 다르면(사이클이 형성되지 않으면)
            answer += w  # 해당 간선의 비용을 결과에 추가
            parents[ancestor(f, parents)] = t  # 한 노드의 루트 노드를 다른 노드의 루트 노드로 설정하여 연결
            bridges += 1  # 연결된 다리(간선)의 수 증가

        if bridges == n - 1:  # 모든 노드가 연결되었으면(간선의 수가 노드 수 - 1이면)
            break  # 반복 종료
    return answer  # 최종 비용 반환
