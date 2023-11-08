import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
weight = defaultdict(int)
dct = {}
words = []
ans = 0

for _ in range(N) :
    w = list(input().rstrip())
    words.append(w)
    for i in range(len(w) - 1, -1, -1) :
        weight[w[i]] += 10 ** (len(w) - i)
        
weights = sorted(weight.items(), key=lambda x:x[1], reverse=True)

rank = 9
for i, j in weights :
    dct[i] = str(rank)
    rank -= 1
    
for word in words :
    num = ''
    for j in word :
        num += dct[j]
    ans += int(num)
    
print(ans)