from collections import defaultdict
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def dfs(cur, parent) :
    global ans
    for child in graph[cur] :
        if child != parent :
            dfs(child, cur)
            dp[cur] += dp[child] + 1

    val = (dp[cur] + 1) * (N - dp[cur] - 1) + (dp[cur] * (dp[cur] + 1) // 2)

    if cur != 1 :
        ans += val

N = int(input())
dp = [0] * (N + 1)
graph = defaultdict(list)
for _ in range(N-1) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
ans = 0
dfs(1, 0)
print(ans)