from collections import defaultdict, deque

N = int(input())
items = defaultdict(list)
values = defaultdict(int)

for _ in range(N) :
    a, b = input().split()
    items[a].append(b)
    values[b] += 1

q = deque()
for i in items :
    if values[i] == 0 :
        q.append((i, 0))

res = defaultdict(list)
while q :
    temp, num = q.popleft()
    res[num].append(temp)
    if temp in items :
        for i in items[temp] :
            values[i] -= 1
            if values[i] == 0 :
                q.append((i, num + 1))

for row in res.values() :
    row.sort()

if len(values) == sum(len(row) for row in res.values()) :
    for row in res.values() :
        if row :
            print(*row, sep='\n')

else :
    print(-1)