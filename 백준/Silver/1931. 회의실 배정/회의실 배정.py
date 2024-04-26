T = int(input())
arr = [list(map(int, input().split())) for _ in range(T)]
arr.sort(key=lambda x:(x[1],x[0]))
cnt = 0
last = 0
for s, e in arr :
    if last <= s :
        cnt += 1
        last = e

print(cnt)