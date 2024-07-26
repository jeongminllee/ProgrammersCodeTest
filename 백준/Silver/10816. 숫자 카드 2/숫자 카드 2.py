N = int(input())
arr = list(map(int, input().split()))
M = int(input())
lst = list(map(int, input().split()))
ans = []

hashMap = {}
for i in arr :
    if i in hashMap :
        hashMap[i] += 1
    else :
        hashMap[i] = 1

for j in lst :
    if j in hashMap :
        ans.append(hashMap[j])
    else :
        ans.append(0)

print(*ans)