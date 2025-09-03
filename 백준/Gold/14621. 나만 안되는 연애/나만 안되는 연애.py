def find(a, parent) :
    while a != parent[a] :
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a

def union(a, b, parent, size) :
    fa, fb = find(a, parent), find(b, parent)
    if fa == fb :
        return False

    if size[fa] < size[fb] :
        fa, fb = fb, fa
    parent[fb] = fa
    size[fa] += size[fb]
    return True
    
def solution(N, M, schools, edges) :
    schools = ['O'] + schools    # 패딩 처리
    new_edges = []
    for u, v, d in edges :
        if schools[u] != schools[v] :
            new_edges.append((d, u, v))

    new_edges.sort()

    # DSU
    parent = list(range(N + 1))
    size = [1] * (N + 1)

    total = 0
    used = 0
    for w, u, v in new_edges :
        if union(u, v, parent, size) :
            total += w
            used += 1
            if used == N - 1 : 
                break

    return total if used == N - 1 else -1
    
        

if __name__ == "__main__" :
    N, M = map(int, input().split())
    schools = list(input().split())    
    edges = []
    for _ in range(M) :
        u, v, d = map(int, input().split())
        edges.append((u, v, d))
            
    print(solution(N, M, schools, edges))