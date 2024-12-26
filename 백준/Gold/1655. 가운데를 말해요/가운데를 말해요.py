import sys
import heapq

input = sys.stdin.readline
N = int(input())

leftHeap = []
rightHeap = []

for _ in range(N) :
    # num : 백준이가 외치는 정수
    num = int(input())

    if len(leftHeap) == len(rightHeap) :
        heapq.heappush(leftHeap, -num)
    else :
        heapq.heappush(rightHeap, num)

    if rightHeap and rightHeap[0] < -leftHeap[0] :
        leftValue = heapq.heappop(leftHeap)
        rightValue = heapq.heappop(rightHeap)

        heapq.heappush(leftHeap, -rightValue)
        heapq.heappush(rightHeap, -leftValue)

    print(-leftHeap[0])