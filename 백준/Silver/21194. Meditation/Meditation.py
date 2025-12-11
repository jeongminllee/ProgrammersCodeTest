import heapq

n, k = map(int, input().split())
exercises = list(int(input()) for _ in range(n))

heap_exercises = []
for exer in exercises :
    heapq.heappush(heap_exercises, (-exer, exer))

res = 0
for _ in range(k) :
    maximal_score = heapq.heappop(heap_exercises)
    res += maximal_score[1]

print(res)