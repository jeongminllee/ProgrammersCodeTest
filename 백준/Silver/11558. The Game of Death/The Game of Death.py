def dfs(node) :
    for j in arr[node] :
        if lst[j] == 0 :
            lst[j] = lst[node] + 1
            dfs(j)

T = int(input())

for _ in range(T) :
    N = int(input())
    arr = [[] for _ in range(N + 1)]
    for i in range(1, N+1) :
        a = int(input())
        arr[i].append(a)

    lst = [0]*(N+1)
    dfs(1)
    print(lst[N] if lst[N] > 0 else 0)