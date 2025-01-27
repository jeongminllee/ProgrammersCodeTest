from collections import deque

def main() :
    N, M = map(int, input().split())

    in_degree = {v : 0 for v in range(1, N + 1)}
    edges_fr_to = {v : [] for v in range(1, N + 1)}
    for _ in range(M) :
        fr, to = map(int, input().split())
        edges_fr_to[fr].append(to)
        in_degree[to] += 1
    q = deque()

    for i in range(1, N + 1) :
        if in_degree[i] == 0 :
            q.append(i)

    res = []

    while q :
        node = q.popleft()
        res.append(node)

        for nxt in edges_fr_to[node] :
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0 :
                q.append(nxt)

    print(*res)
    
main()