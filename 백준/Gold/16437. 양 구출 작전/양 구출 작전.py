N = int(input())

children = [[] for _ in range(N + 1)]
typ = [''] * (N + 1)    # S or W 
nums = [0] * (N + 1)    # 해당 섬의 양/늑대 수

for i in range(2, N + 1) :
    t, a, p = input().split()
    a = int(a)
    p = int(p)
    typ[i] = t
    nums[i] = a
    children[p].append(i)

# 후위 순회 : dp[u] = u 서브트리에서 부모로 올릴 수 있는 양의 수
dp = [0] * (N + 1)
stack = [(1, 0)]    # 노드, 방문표시
while stack :
    u, visit = stack.pop()
    if not visit :
        stack.append((u, 1))
        for v in children[u] :
            stack.append((v, 0))
    else :
        total = 0
        for v in children[u] :
            total += dp[v]
        if typ[u] == 'S' :
            total += nums[u]
        elif typ[u] == 'W' :
            total = max(0, total - nums[u])

        dp[u] = total
        
print(dp[1])