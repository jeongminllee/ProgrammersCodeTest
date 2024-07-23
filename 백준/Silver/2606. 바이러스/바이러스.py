def dfs(c) :
    v.add(c)

    for n in graph[c] : 
        if n not in v :
            dfs(n)

com = int(input())
network = int(input())

graph = [[] for _ in range(com + 1)]
v = set()

for _ in range(network) :
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

dfs(1)
print(len(v) - 1)