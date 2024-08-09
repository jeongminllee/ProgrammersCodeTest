from sys import setrecursionlimit
setrecursionlimit(100500)
import io
input = io.BufferedReader(io.FileIO(0), 1<<18).readline

t = int(input())
M_N = 100000
M_X = 1000000000
tree = [[] for _ in range(M_N+1)]

def dfs(v):
    for u in tree[v]:
        if vis[u] == 0:
            vis[u] = 1
            p[u] = v
            dfs(u)

def f(v, x):
    tmp = []
    c = 0; total = 0
    for u in tree[v]:
        if p[u] != v: continue
        val = f(u, x)
        c += val[0]
        total += val[1]
        tmp.append(val[1])
    
    tmp.sort()
    while tmp and total + a[v] > x:
        c += 1
        total -= tmp.pop()
    return c, total + a[v]

for _ in range(t):
    n, k = map(int, input().split())
    a = [0]+list(map(int, input().split()))
    for i in range(M_N+1): tree[i].clear()
    for _ in range(n-1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    p = [0]*(n+1)
    vis = [0]*(n+1)
    vis[1] = 1; dfs(1)

    l, r = max(a), M_X*n
    while l < r:
        mid = (l+r) // 2
        tmp = f(1, mid)[0]
        if tmp <= k:
            r = mid
        else:
            l = mid+1
    
    print(l)