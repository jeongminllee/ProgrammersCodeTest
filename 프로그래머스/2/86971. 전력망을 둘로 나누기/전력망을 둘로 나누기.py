from collections import defaultdict

def solution(n, wires):
    graph = defaultdict(list)
    for v1, v2 in wires:  # 그래프 생성
        graph[v1].append(v2)
        graph[v2].append(v1)

    answer = n
    for v1, v2 in wires:  # 각 전선을 끊어보기
        graph[v1].remove(v2)
        graph[v2].remove(v1)

        # DFS를 이용한 서브그래프 크기 계산
        visited = [0] * (n + 1)
        stack = [1]
        count = 0
        while stack:
            node = stack.pop()
            if visited[node] == 0:
                visited[node] = 1
                count += 1
                stack.extend(graph[node])

        answer = min(answer, abs(n - 2 * count))  # 크기 차이 계산

        graph[v1].append(v2)  # 전선 다시 연결
        graph[v2].append(v1)

    return answer
