from collections import defaultdict
import heapq

N = int(input())
item = defaultdict(list)
values = defaultdict(int)
visited = set()

for _ in range(N) :
    a, b = input().split()
    visited.update({a, b})
    item[a].append(b)
    values[b] += 1

buy_item = []
for visit in visited :
    if values[visit] == 0 :
        heapq.heappush(buy_item, visit)

poped_item, tmp = [], []
while buy_item :
    poped_item.append(node:=heapq.heappop(buy_item))
    for nxt_node in sorted(item[node]) :
        values[nxt_node] -= 1
        if values[nxt_node] == 0 :
            heapq.heappush(tmp, nxt_node)

    if not buy_item :
        if not tmp :
            break
        buy_item = tmp
        tmp = []

if len(poped_item) != len(visited) :
    print(-1)
else :
    for x in poped_item :
        print(x)