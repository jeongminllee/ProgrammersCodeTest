import sys
sys.setrecursionlimit(10**4)

n = int(input())
arr = [[] for _ in range(n + 1)]

# p, c, w = 부모 노드, 자식 노드, 가중치
for _ in range(1, n) :  
    p, c, w = map(int, input().split())
    arr[p].append((c, w))
    arr[c].append((p, w))

lst = [-1] * (n + 1)
lst[1] = 0

def dfs(cv, cw) :
    for nv, nw in arr[cv] :
        if lst[nv] == -1 :
            lst[nv] = cw + nw
            dfs(nv, cw + nw)

dfs(1, 0)
ans = lst.index(max(lst))
lst = [-1] * (n + 1)
lst[ans] = 0

dfs(ans, 0)

print(max(lst))