import heapq

class UnionFind() :
    def __init__(self, n):
        self.dp = [-1] * n

    def find(self, i) :
        if self.dp[i] < 0 :
            return i
        self.dp[i] = self.find(self.dp[i])

        return self.dp[i]

    def union(self, a, b):
        if a==b :
            return False

        ra, rb = self.find(a), self.find(b)
        if ra == rb :
            return False

        if self.dp[ra] < self.dp[rb] :
            self.dp[ra] += self.dp[rb]
            self.dp[rb] = ra
        else :
            self.dp[rb] += self.dp[ra]
            self.dp[ra] = rb

        return True

    def get_size(self, i) :
        return -self.dp[self.find(i)]

def sol(coor, uf) :
    L = len(coor)
    heap = []

    for i in range(1, L-1) :
        ay = coor[i][0]
        ax = coor[i][1]
        group = uf.find(i)

        for j in range(i + 1, L) :
            if uf.find(j) == group:
                continue
            d = (ay - coor[j][0])**2 + (ax - coor[j][1])**2
            heapq.heappush(heap, (d, i, j))

    cost = 0.0
    cnt = L - 1

    while True :
        v, i, j = heapq.heappop(heap)

        if uf.union(i, j) :
            cost += v**(0.5)

            if uf.get_size(i) == cnt :
                break

    return cost

N, M = map(int, input().split())

coor = [0] + [list(map(int, input().split())) for _ in range(N)]
uf = UnionFind(N+1)

for _ in range(M) :
    uf.union(*map(int, input().split()))

print(f"{sol(coor, uf):.2f}")