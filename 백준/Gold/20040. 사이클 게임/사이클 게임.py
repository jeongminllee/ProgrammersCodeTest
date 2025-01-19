def union(v1, v2, vertexes) :
    vertexes[max(v1, v2)] = min(v1, v2)

def find(v, vertexes) :
    if v != vertexes[v] :
        vertexes[v] = find(vertexes[v], vertexes)
        return vertexes[v]

    return vertexes[v]


n, m = map(int, input().split())
vertexes = [i for i in range(n)]

for i in range(m) :
    v1, v2 = map(int, input().split())

    root_v1 = find(v1, vertexes)
    root_v2 = find(v2, vertexes)

    if root_v1 == root_v2 :
        print(i + 1)
        exit()
    else :
        union(root_v1, root_v2, vertexes)

print(0)