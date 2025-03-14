import sys
input = sys.stdin.readline

def dfs(node, group, edges, visited) :
    visited[node] = group
    for neighbor in edges[node] :
        if visited[neighbor] == 0 :
            dfs(neighbor, group, edges, visited)
        

def sol_5237() :
    n, k, *arr = map(int,input().split())
    edges = [[] for _ in range(n)]

    for i in range(0, len(arr), 2) :
        p, q = arr[i], arr[i+1]
        edges[p].append(q)
        edges[q].append(p)

    visited = [0] * n
    group = 0
    for i in range(n) :
        if visited[i] == 0 :
            group += 1
            dfs(i, group, edges, visited)
    
    if group == 1:
        print('Connected.')
        return
    else :
        print('Not connected.')
        return

T = int(input())
for _ in range(T) :
    sol_5237()