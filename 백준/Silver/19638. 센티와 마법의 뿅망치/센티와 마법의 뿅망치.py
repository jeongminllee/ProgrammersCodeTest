import heapq

N, H, T = map(int, input().split())
pq = []
cnt = 0

for _ in range(N) :
    giant = int(input())
    heapq.heappush(pq, -giant)

while pq and (T > cnt) :
    G = -heapq.heappop(pq)
    if G >= H :
        G = max(1, G//2)
        cnt += 1
        if G >= H :
            heapq.heappush(pq, -G)
        else :
            continue

if not pq :
    print('YES')
    print(cnt)
else :
    print('NO')
    print(-heapq.heappop(pq))