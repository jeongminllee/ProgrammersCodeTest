import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
jewels = []
bags = []
for _ in range(N) :
    m, v = map(int, input().split())
    heapq.heappush(jewels, (m, v))   # 힙에 푸시

for _ in range(K) :
    bags.append(int(input()))      # 가방 무게 정보
bags.sort()

total_val, capable_jewels = 0, []
for bag in bags :
    while jewels and bag >= jewels[0][0] :      # bag의 무게가 jewels의 무게보다 더 클 경우
        m, v = heapq.heappop(jewels)            # 힙에서 팝
        heapq.heappush(capable_jewels, -v)      # 힙에 푸시
    if capable_jewels :
        total_val -= heapq.heappop(capable_jewels)  # total_val 갱신
    elif not jewels :
        break
print(total_val)