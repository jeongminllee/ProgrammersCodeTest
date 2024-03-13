import sys
sys.setrecursionlimit(10 ** 5)
from collections import defaultdict

def dfs(graph, start, visited, order, counter):
    visited[start] = True
    order[start] = counter[0]
    counter[0] += 1

    for next_node in sorted(graph[start]):
        if not visited[next_node]:
            dfs(graph, next_node, visited, order, counter)

def main():
    N, M, R = map(int, input().split())
    graph = defaultdict(list)

    # 그래프 구성
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (N + 1)
    order = [0] * (N + 1)
    counter = [1]  # 방문 순서를 기록하기 위한 카운터, 리스트 형태로 선언하여 참조 전달을 사용

    # 깊이 우선 탐색 시작
    dfs(graph, R, visited, order, counter)

    # 방문 순서 출력
    for i in range(1, N + 1):
        print(order[i])


if __name__ == "__main__":
    main()
