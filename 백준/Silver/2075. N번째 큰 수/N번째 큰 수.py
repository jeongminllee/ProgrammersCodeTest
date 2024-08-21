import heapq

N = int(input())
heap = []

for _ in range(N) :
    nums = map(int, input().split())
    for num in nums :
        if len(heap) < N :  # heap의 크기를 N개로 유지
            heapq.heappush(heap, num)
        else :
            if heap[0] < num :
                heapq.heappop(heap)
                heapq.heappush(heap, num)
print(heap[0])