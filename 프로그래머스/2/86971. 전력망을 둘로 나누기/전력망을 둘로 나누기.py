# from collections import defaultdict
#
# def solution(n, wires):
#     graph = defaultdict(list)
#     for v1, v2 in wires:  # 그래프 생성
#         graph[v1].append(v2)
#         graph[v2].append(v1)
#
#     answer = n
#     for v1, v2 in wires:  # 각 전선을 끊어보기
#         graph[v1].remove(v2)
#         graph[v2].remove(v1)
#
#         # DFS를 이용한 서브그래프 크기 계산
#         visited = [0] * (n + 1)
#         stack = [1]
#         count = 0
#         while stack:
#             node = stack.pop()
#             if visited[node] == 0:
#                 visited[node] = 1
#                 count += 1
#                 stack.extend(graph[node])
#
#         answer = min(answer, abs(n - 2 * count))  # 크기 차이 계산
#
#         graph[v1].append(v2)  # 전선 다시 연결
#         graph[v2].append(v1)
#
#     return answer

def solution(n, wires):
    # 1. 그래프 생성
    graph = [[] for _ in range(n + 1)]
    for a, b in wires :
        graph[a].append(b)
        graph[b].append(a)

    # 2. 깊이 우선 탐색 함수
    def dfs(node, parent) :
        cnt = 1
        for child in graph[node] :  # 3. 현재 노드의 자식 노드들에 방문
            if child != parent :    # 4. 부모 노드가 아닌 경우에만 탐색
                cnt += dfs(child, node)
        return cnt

    min_diff = float('inf')
    for a, b in wires :
        # 5. 간선 제거
        graph[a].remove(b)
        graph[b].remove(a)

        # 6. 각 전력망 송전탑 개수 계산
        cnt_a = dfs(a, b)
        cnt_b = n - cnt_a

        # 7. 최솟값 갱신
        min_diff = min(min_diff, abs(cnt_a - cnt_b))

        # 8. 간선 복원
        graph[a].append(b)
        graph[b].append(a)

    return min_diff