import sys
input = sys.stdin.readline

import heapq

N, K = map(int, input().split())
jewels = []
bags = []

for _ in range(N) :
    m, v = map(int, input().split())
    heapq.heappush(jewels, (m, v))

for _ in range(K) :
    bags.append(int(input()))

bags.sort()

total_val = 0
capable_jewels = []

for bag in bags :
    while jewels and bag >= jewels[0][0] :
        m, v = heapq.heappop(jewels)
        heapq.heappush(capable_jewels, -v)
    if capable_jewels :
        total_val -= heapq.heappop(capable_jewels)
    elif not jewels :
        break

print(total_val)