import sys
sys.setrecursionlimit(10**5)

def dfs(node: int, graph: list[list[int]], visited: list[bool], q: list) -> None :
    visited[node] = 1

    for nxt_node in graph[node] :
        if visited[nxt_node] == 0:
            dfs(nxt_node, graph, visited, q)

    q.append(node)

def reverse_dfs(node: int, graph: list[list[int]], visited: list[bool], ssc: list) :
    visited[node] = 1
    ssc.append(node)

    for nxt_node in graph[node] :
        if visited[nxt_node] == 0 :
            reverse_dfs(nxt_node, graph, visited, ssc)

def make_queue(v: int, graph: list[list[int]], visited: list[bool]) -> list:
    q = []

    for node in range(1, v+1) :
        if visited[node] == 0 :
            dfs(node, graph, visited, q)

    return q

def reverse_graph(v: int, graph: list[list[int]]) -> list :
    rev_graph = [[] for _ in range(v+1)]

    for i in range(1, v+1) :
        for j in graph[i] :
            rev_graph[j].append(i)

    return rev_graph

def check_ssc(q: list, graph: list[list[int]], visited: list[int]) -> (int, list) :
    cnt, res = 0, []

    while q :
        ssc = []
        node = q.pop()
        if visited[node] == 0 :
            reverse_dfs(node, graph, visited, ssc)
            res.append(sorted(ssc))
            cnt += 1

    res.sort()
    return cnt, res

def main() :
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1)

    for _ in range(e) :
        a, b = map(int, input().split())
        graph[a].append(b)

    q = make_queue(v, graph, visited)
    graph = reverse_graph(v, graph)
    visited = [0] * (v+1)
    cnt, res = check_ssc(q, graph, visited)

    print(cnt)
    for i in res :
        for j in i :
            print(j, end=' ')
        print(-1)

if __name__ == "__main__" :
    main()