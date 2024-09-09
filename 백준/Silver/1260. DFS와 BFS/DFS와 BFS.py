from collections import deque

# DFS 재귀
# def dfs(c) :
#     ans_dfs.append(c)
#     v[c] = 1
#
#     for n in graph[c] :
#         if not v[n] :
#             dfs(n)

# DFS stack
def dfs(s) :
    stack = [s]

    while stack :
        c = stack.pop()
        if not v[c] :
            v[c] = 1
            ans_dfs.append(c)

            for n in reversed(graph[c]) :
                if not v[n] :
                    stack.append(n)
                    
def bfs(s) :
    q = deque()
    q.append(s)
    ans_bfs.append(s)
    v[s] = 1
    while q :
        c = q.popleft()
        for n in graph[c] :
            if not v[n] :
                q.append(n)
                ans_bfs.append(n)
                v[n] = 1

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M) :
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1, N+1) :
    graph[i].sort()

# 첫 줄에는 DFS
v = [0] * (N + 1)
ans_dfs = []
dfs(V)

# 두번째 줄에는 BFS
v = [0] * (N + 1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)