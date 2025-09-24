from collections import defaultdict
import heapq

N = int(input())
items = defaultdict(list)
values = defaultdict(int)
v_set = set()

for _ in range(N) :
    a, b = input().split()
    v_set.update({a, b})
    items[a].append(b)
    values[b] += 1

buy_item = []
for visit in v_set :
    if values[visit] == 0 :
        heapq.heappush(buy_item, visit)

poped_item, tmp = [], []
while buy_item :
    poped_item.append(node:=heapq.heappop(buy_item))
    for nxt_node in sorted(items[node]) :
        values[nxt_node] -= 1
        if values[nxt_node] == 0 :
            heapq.heappush(tmp, nxt_node)

    if not buy_item :
        if not tmp :
            break
        buy_item = tmp
        tmp = []

if len(poped_item) != len(v_set) :
    print(-1)
else :
    for x in poped_item :
        print(x)