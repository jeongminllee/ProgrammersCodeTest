import sys
sys.setrecursionlimit(10**5)
def make_queue(N: int, graph: list[list[int]], visited: list[int]) -> list :
    queue = []

    for node in range(1, N+1) :
        if visited[node] == 0 :
            dfs(node, graph, visited, queue)
    return queue

def check_scc(queue: list, graph : list[list[int]], visited: list[int], graph_in_degree: list[int]) -> int:
    cnt = 0

    while queue :
        node = queue.pop()
        if visited[node] == 0 :
            cnt += 1
            reverse_dfs(node, graph, visited, graph_in_degree, cnt)
    return cnt

def dfs(node: int, graph: list[list[int]], visited: list[int], queue: list) -> None :
    visited[node] = 1

    for nxt_node in graph[node] :
        if visited[nxt_node] == 0 :
            dfs(nxt_node, graph, visited, queue)
    queue.append(node)

def reverse_dfs(node: int, graph: list[list[int]], visited: list[int], graph_in_degree: list[int], cnt: int) -> None:
    visited[node] = 1
    graph_in_degree[node] = cnt

    for nxt_node in graph[node] :
        if visited[nxt_node] == 0 :
            reverse_dfs(nxt_node, graph, visited, graph_in_degree, cnt)

def main() :
    N, M = map(int, input().split())    # 도미노 개수, 관계 개수
    graph = [[] for _ in range(N+1)]
    rev_graph = [[] for _ in range(N+1)]
    visited = [0] * (N+1)

    for _ in range(M) :
        x, y = map(int, input().split())
        graph[x].append(y)
        rev_graph[y].append(x)

    queue = make_queue(N, graph, visited)
    visited = [0] * (N+1)   # visited 리셋
    graph_in_degree = [0] * (N+1)

    cnt = check_scc(queue, rev_graph, visited, graph_in_degree)
    scc_in_degree = [0] * (cnt + 1) # scc 위상정렬

    for idx in range(1, N+1) :
        for parent in graph[idx] :
            if not (graph_in_degree[idx] == graph_in_degree[parent]) :
                scc_in_degree[graph_in_degree[parent]] += 1
    result = 0
    for node in range(1, len(scc_in_degree)) :
        if scc_in_degree[node] == 0 :
            result += 1
    print(result)


if __name__ == "__main__" :
    T = int(input())    # test_case
    for _ in range(T) :
        main()