def dfs(c) :
    global cnt
    cnt += 1
    v[c] = 1

    for n in adj[c] :
        if not v[n] :
            dfs(n)

N = int(input())    # 컴퓨터의 수
pairs = int(input())# 컴퓨터 쌍의 수
adj = [[] for _ in range(N + 1)]
for _ in range(pairs) :
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

cnt = 0
v = [0] * (N + 1)
dfs(1)
print(cnt - 1)