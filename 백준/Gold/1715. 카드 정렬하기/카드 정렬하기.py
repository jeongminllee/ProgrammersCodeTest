import sys
import heapq
input=sys.stdin.readline

N = int(input())
arr = []
for i in range(N) :
    heapq.heappush(arr, int(input()))

ans = 0
while len(arr) > 1 :
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    sum_value = a + b

    ans += sum_value
    heapq.heappush(arr, sum_value)

print(ans)