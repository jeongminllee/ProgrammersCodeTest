import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []
for i in range(N) :
    x = int(input())
    if x != 0 :
        heapq.heappush(heap, (x, x))
    else :
        try :
            print(heapq.heappop(heap)[1])
        except :
            print(0)