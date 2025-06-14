MOD = 10**9 + 7

def comb3(k) :
    if k < 3 :
        return 0
    return (k * (k - 1) * (k - 2)) // 6

# n: 정점, m: 간선
n, m = map(int, input().split())

edges = [list(map(int, input().split())) for _ in range(m)]
degree = [0] * (n + 1)

# 4개의 정점, 3개의 간선을 가짐
# 루트 : 하나의 정점, 리프 : 나머지 3개의 정점
# 3개의 간선이 각각의 리프와 루트를 연결

for u, v in edges :
    degree[u] += 1
    degree[v] += 1

res = 0
for d in degree :
    res = (res + comb3(d)) % MOD

print(res)