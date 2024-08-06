import sys
from collections import defaultdict

def is_bipartite(graph, start, colors):
    stack = [(start, 1)]
    while stack:
        node, color = stack.pop()
        if node in colors:
            if colors[node] != color:
                return False
            continue
        colors[node] = color
        for neighbor in graph[node]:
            stack.append((neighbor, -color))
    return True

def solve():
    K = int(sys.stdin.readline())
    for _ in range(K):
        V, E = map(int, sys.stdin.readline().split())
        graph = defaultdict(list)
        for _ in range(E):
            u, v = map(int, sys.stdin.readline().split())
            graph[u].append(v)
            graph[v].append(u)
        
        colors = {}
        is_bipartite_graph = all(is_bipartite(graph, node, colors) for node in range(1, V+1) if node not in colors)
        print("YES" if is_bipartite_graph else "NO")

if __name__ == "__main__":
    solve()