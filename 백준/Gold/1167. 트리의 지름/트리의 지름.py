def dfs(s, arr, v) :
    stack = [(s, 0)]
    v[s] = 0

    while stack :
        node, dist = stack.pop()
        for next_node, next_dist in arr[node] :
            if v[next_node] == -1 :
                v[next_node] = dist + next_dist
                stack.append((next_node, v[next_node]))

n = int(input())
arr = [[] for _ in range(n + 1)]

for _ in range(n) :
    line = list(map(int, input().split()))
    node = line[0]
    for i in range(1, len(line) - 2, 2) :
        arr[node].append((line[i], line[i + 1]))

v = [-1] * (n + 1)
v[1] = 0
dfs(1, arr, v)

max_node = v.index(max(v))

v = [-1] * (n + 1)
v[max_node] = 0
dfs(max_node, arr, v)

print(max(v))