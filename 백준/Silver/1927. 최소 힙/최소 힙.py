import heapq, sys
input = sys.stdin.readline

heap = []
N = int(input())
for _ in range(N) :
    num = int(input())
    if num != 0 :
        heapq.heappush(heap, num)
    else :
        print(heapq.heappop(heap) if heap else 0)