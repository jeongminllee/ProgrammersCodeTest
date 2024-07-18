from collections import deque

def bfs(s) :
    q = deque()
    q.append(s)

    visited[s] = 1

    while q :
        curr = q.popleft()

        for child in tree[curr] :
            if visited[child] == 0 :
                visited[child] = curr
                q.append(child)

N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N-1) :
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [0] * (N + 1)

bfs(1)
parents = visited[2:]
for i in parents:
    print(i)