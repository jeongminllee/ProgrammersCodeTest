def dfs(num) :
    if visited[num] == 0 :
        visited[num] = 1
        for a in adj[num] :

            tmp_up.add(num)
            tmp_down.add(a)

            if tmp_up == tmp_down :
                ans.extend(list(tmp_down))

            dfs(a)

    visited[num] = 0

N = int(input())
adj = [[] for _ in range(N + 1)]
for i in range(1,N+1) :
    num = int(input())
    adj[i].append(num)

ans = []

for i in range(1, N+1) :
    visited = [0] * (N + 1)
    tmp_up = set()
    tmp_down = set()

    dfs(i)

ans = list(set(ans))
ans.sort()

print(len(ans))
for a in ans :
    print(a)