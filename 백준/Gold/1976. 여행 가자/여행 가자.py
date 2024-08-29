def find(x) :
    if parents[x] == x :
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y) :
    x = find(x)
    y = find(y)

    if x > y :
        parents[x] = y
    else :
        parents[y] = x


N = int(input())    # 도시의 수
M = int(input())    # 여행 계획에 속한 도시의 수
parents = [i for i in range(N)]
for i in range(N) :
    link = list(map(int, input().split()))
    for j in range(N) :
        if link[j] == 1 :
            union(i, j)

parents = [-1] + parents
path = list(map(int, input().split()))
start = parents[path[0]]
for i in range(1, M) :
    if parents[path[i]] != start :
        print("NO")
        break
else :
    print("YES")