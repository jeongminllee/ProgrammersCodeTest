from collections import deque

def find_parents(tree, N, s) :
    q = deque()
    q.append(s)

    while q :
        curr = q.popleft()
        for child in tree[curr] :
            if visited[child] == 0 :
                visited[child] = curr
                q.append(child)

    return visited[2:]

N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1) :
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [0] * (N + 1)

parents = find_parents(tree, N, 1)
for i in parents :
    print(i)