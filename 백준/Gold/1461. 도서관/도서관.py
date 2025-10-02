N, M = map(int, input().split())
lst = list(map(int, input().split()))
pos = []
neg = []
l = []
for i in lst :
    if i > 0 :
        pos.append(i)
    else :
        neg.append(abs(i))

pos.sort(reverse=True)
neg.sort(reverse=True)

for i in range(len(pos)) :
    if i % M == 0 :
        l.append(pos[i])
for i in range(len(neg)) :
    if i % M == 0 :
        l.append(neg[i])
        
l.sort()
res = 2 * sum(l) - l[-1]
print(res)