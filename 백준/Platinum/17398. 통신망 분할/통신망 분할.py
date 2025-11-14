def find(a: int, parent:list[int]) -> int :
    if a != parent[a] :
        parent[a] = find(parent[a], parent)
    return parent[a]

def union(a:int, b:int, parent:list[int]) -> None :
    a = find(a, parent)
    b = find(b, parent)

    if a < b :
        parent[b] = a
        cost[a] += cost[b]
    elif a > b :
        parent[a] = b
        cost[b] += cost[a]

def main() :
    """
    N 개의 통신탑, M개의 연결, Q번 통신탑 간의 연결을 제거함으로써 여러 망으로 분리
    """
    global cost
    N, M, Q = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    tree = []
    edges = [list(map(int, input().split())) for _ in range(M)]

    tmp = [0] * M
    cut = []

    parent = [i for i in range(N+1)]
    cost = [1 for _ in range(N+1)]

    for _ in range(Q) :
        K = int(input()) - 1
        cut.append(K)
        tmp[K] = 1

    for i in range(M) :
        if not tmp[i] :
            x, y = edges[i]
            if find(x, parent) != find(y, parent) :
                union(x, y, parent)

    res = 0

    for i in range(Q-1, -1, -1) :
        x, y = edges[cut[i]]
        if find(x, parent) != find(y, parent) :
            res += cost[find(x, parent)] * cost[find(y, parent)]
            union(x, y, parent)

    return res

if __name__ == "__main__" :
    print(main())